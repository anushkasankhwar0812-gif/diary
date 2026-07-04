# 📔 Diary Entry App

A simple and secure personal diary web application built with **Python (Flask)** on the backend and **HTML/CSS** on the frontend. Users can register, log in, and manage their own private diary entries.

## ✨ Features

- 🔐 **User Registration & Login** – Secure authentication system for individual users
- 📝 **Create Diary Entries** – Write and save your daily thoughts
- 👀 **View Entries** – Browse all your saved diary entries
- ✏️ **Edit Entries** – Update existing entries anytime
- 🗑️ **Delete Entries** – Remove entries you no longer want
- 💾 **Persistent Storage** – Entries are saved and available across sessions

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Storage:** JSON file / Database (update based on your implementation)

## 📂 Project Structure

```
diary-app/
├── app.py                 # Main Flask application
├── templates/              # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── diary.html
│   └── edit.html
├── static/                 # CSS, JS, images
│   └── style.css
├── data/                    # Stored diary entries
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- pip package manager

### Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/diary-app.git
cd diary-app
```

2. Install dependencies
```bash
pip install flask
```

3. Run the application
```bash
python app.py
```

4. Open your browser and go to:
```
http://127.0.0.1:5000
```

## 📖 Usage

1. **Register** a new account or **log in** with existing credentials
2. **Create** a new diary entry from the dashboard
3. **View** all your past entries in one place
4. **Edit** any entry to update its content
5. **Delete** entries you no longer need

## 🔮 Future Improvements

- Add search/filter by date or keyword
- Add rich text formatting for entries
- Add mood tags or tags for entries
- Deploy live version

## 👩‍💻 Author

Built by Anushka as part of a self-directed learning project.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
