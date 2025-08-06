# Shutdown-GUI-App

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)

## ✅ Features

1. Simple and custom-built GUI for system control operations.
2. One-click buttons to:
   - Shutdown the system
   - Restart the system
   - Restart with a 20-second delay
   - Log out / suspend the system
3. Works instantly without confirmation prompts or warnings.
4. Built using Python's `tkinter` and `os` modules.
5. Lightweight and easy to use – acts like a standalone software tool.

## 🛠️ How It Works

```python
from tkinter import *
import os

def shutdown():
    os.system("shutdown /s /t 1")
```
The app uses os.system() to execute system-level shutdown and restart commands on Windows OS. The interface is created using tkinter, providing clickable buttons for each operation.

## 📋 Requirements
- Python 3.7+
- tkinter (standard library)
- os (standard library)
- Windows OS (required for shutdown, restart, and log-out commands to work)


## 🚀 How to Run
```
# Clone the repository
git clone https://github.com/your-username/Shutdown-GUI-App.git
cd Shutdown-GUI-App

# Run the script (Windows only)
python shutdown_app.py
```
⚠️ Note: Make sure to save all your work before clicking any action button – the app executes the command immediately.


## 🧠 Lessons Learned
* How to use tkinter for building Python GUIs.
* How to perform system-level operations using os.system() in Python.
* How to create a functional app with shutdown/restart capabilities.


## 📄 License
This project is licensed under the MIT License. See the LICENSE file for full details.
