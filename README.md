# 🔐 Password Manager

A secure password generator and manager built with Python's `tkinter` module and `pyperclip`. This project is part of my **100 Days of Code** challenge.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![100DaysOfCode](https://img.shields.io/badge/100DaysOfCode-orange)

## About

Keep your logins organized and secure! Enter a website and email, generate a strong random password with one click, and save your credentials locally. The app combines letters, numbers, and symbols to create secure passwords, copies them straight to your clipboard, and stores your saved entries in a simple text file for quick reference.

## Features

- Graphical interface built with `tkinter`, including a custom logo
- One-click random password generator (letters, numbers, and symbols)
- Generated passwords are automatically copied to the clipboard
- Input validation warns you if the website or password field is left empty
- Confirmation dialog shows entered details before saving
- Saved credentials are appended to `data.text` for later reference

## How to Use

- Enter the **website** name in the input field
- Enter your **email/username** (pre-filled with a placeholder you can overwrite)
- Click **"Generate Password"** to create a strong password, or type your own
- Click **"Add"** to save your entry
- Confirm the details in the popup dialog to complete the save
- Your saved credentials appear in `data.text` in the format: `website | email | password`

## Project Structure
- main.py                  # App logic, UI setup, and password generation
- logo.png                 # Logo image displayed in the app window
- data.text                # Generated on save — stores saved credentials

## Built With

- [Python](https://www.python.org/) — programming language
- [tkinter](https://docs.python.org/3/library/tkinter.html) — built-in GUI library
- [pyperclip](https://pypi.org/project/pyperclip/) — clipboard access for copying generated passwords
- [random](https://docs.python.org/3/library/random.html) — built-in module

## Part of 100 Days of Code

This project was built as part of the **100 Days of Code** challenge, a commitment to code every day for 100 days while building real projects to practice and improve Python skills.

## 📝 Note

This is a learning project — passwords are stored **without encryption** in a plain text file, so it is **not recommended** for storing real credentials.