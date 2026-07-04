import sqlite3

from flask import Flask, redirect , render_template, request, session
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def home():
    return render_template('kk.html')

def create_table():
    conn = sqlite3.connect("diary.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

create_table()

def create_diary_table():
    conn = sqlite3.connect("diary.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS diary(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            content TEXT
        )
    """)

    conn.commit()
    conn.close()

create_diary_table()



@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        conn = sqlite3.connect("diary.db")
        c = conn.cursor()

    try:
         c.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password)
        )
         conn.commit()
         return "Registration Successful!"
 
    except sqlite3.IntegrityError:
      return "Username or Email already exists."

    finally:
     conn.close()
    return render_template("kk.html")

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        email = request.form.get("email")
        password = request.form.get("password")

        conn = sqlite3.connect('diary.db')
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = c.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect("/diary")
        else:
            return "Invalid email or password!"

    return render_template("kk.html")

@app.route("/diary")
def diary():

    conn = sqlite3.connect("diary.db")
    c = conn.cursor()

    c.execute("SELECT * FROM diary WHERE user_id=? ORDER BY id DESC", (session["user_id"],))

    entries = c.fetchall()

    conn.close()

    return render_template("diary.html",entries=entries)

@app.route("/save", methods=["POST"])
def save():

    title = request.form.get("title")
    content = request.form.get("content")

    conn = sqlite3.connect("diary.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO diary(user_id, title, content) VALUES(?,?,?)",
        (session["user_id"], title, content)
    )

    conn.commit()
    conn.close()

    return redirect("/diary")

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    conn = sqlite3.connect("diary.db")
    c = conn.cursor()

    c.execute(
        "DELETE FROM diary WHERE id=? AND user_id=?",
        (id, session["user_id"])
    )

    conn.commit()
    conn.close()

    return redirect("/diary")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):

    conn = sqlite3.connect("diary.db")
    c = conn.cursor()

    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")

        c.execute(
            """
            UPDATE diary
            SET title=?, content=?
            WHERE id=? AND user_id=?
            """,
            (
                title,
                content,
                id,
                session["user_id"]
            )
        )

        conn.commit()
        conn.close()

        return redirect("/diary")

    c.execute(
        "SELECT * FROM diary WHERE id=? AND user_id=?",
        (id, session["user_id"])
    )

    entry = c.fetchone()

    conn.close()

    return render_template("edit.html", entry=entry)

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
