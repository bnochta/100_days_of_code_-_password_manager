# 🔐 Password Manager

A secure password generator and manager built with Python's `tkinter` module and `pyperclip`. This project is part of my **100 Days of Code** challenge.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![100DaysOfCode](https://img.shields.io/badge/100DaysOfCode-orange)

## About

Keep your logins organized and secure! Enter a website and email, generate a strong random password with one click, and save your credentials locally. The app combines letters, numbers, and symbols to create secure passwords, copies them straight to your clipboard, and stores your saved entries locally in a JSON file for quick lookup by website name.

## Features

- Graphical interface built with `tkinter`, including a custom logo
- One-click random password generator (letters, numbers, and symbols)
- Generated passwords are automatically copied to the clipboard
- Input validation warns you if the website or password field is left empty
- Confirmation dialog shows entered details before saving
- Saved credentials are stored in `data.json`, keyed by website name
- **Search** for a saved website to instantly retrieve its email and password

## How to Use

### Adding a new entry
- Enter the **website** name in the input field
- Enter your **email/username** (pre-filled with a placeholder you can overwrite)
- Click **"Generate Password"** to create a strong password, or type your own
- Click **"Add"** to save your entry
- Confirm the details in the popup dialog to complete the save
- Your credentials are saved in `data.json`, keyed by the website name

### Searching for an entry
- Type the **website** name into the input field
- Click **"Search"**
- A popup will display the saved email and password for that website
- If no entry exists for that website, a warning message is shown instead

## Project Structure
- main.py                  # App logic, UI setup, password generation, and search
- logo.png                 # Logo image displayed in the app window
- data.json                # Generated on save — stores saved credentials as JSON

## Data Format

Credentials are stored in `data.json`, with each website as a key:

```json
{
    "test": {
        "email": "your.email@email.com",
        "password": "12345"
    }
}
```

## Built With

- [Python](https://www.python.org/) — programming language
- [tkinter](https://docs.python.org/3/library/tkinter.html) — built-in GUI library
- [pyperclip](https://pypi.org/project/pyperclip/) — clipboard access for copying generated passwords
- [json](https://docs.python.org/3/library/json.html) — built-in module for reading/writing saved credentials
- [random](https://docs.python.org/3/library/random.html) — built-in module

## Part of 100 Days of Code

This project was built as part of the **100 Days of Code** challenge, a commitment to code every day for 100 days while building real projects to practice and improve Python skills.

## 📝 Note

This is a learning project — passwords are stored **without encryption** in a plain JSON file, so it is **not recommended** for storing real credentials.