# Python Keylogger

## 📌 Project Overview
This is a **Python-based keylogger** designed for cybersecurity research and ethical security analysis. The script records keystrokes in the background and saves them to a log file (`keylog.txt`).

### 🔹 Features:
- Runs **silently in the background**.
- Logs **all keystrokes**, including special keys.
- Uses **threading** to avoid blocking other tasks.
- Stores logs in a **timestamped format**.
- Easy to **extend and modify** for additional monitoring.

---

## 🚀 How It Works
1. The keylogger script (`Python_Keylogger.py`) starts a background listener for keypress events.
2. Every key press is logged in **keylog.txt** with a timestamp.
3. The script runs **continuously in a separate thread** to avoid slowing down the system.
4. The recorded logs can be reviewed later for analysis.

---

## 📂 Project Structure
```
Keylogger/
│-- keylogger-env/         # Virtual environment (optional)
│-- keylog.txt             # Log file where key presses are stored
│-- Python_Keylogger.py    # Main keylogger script
│-- README.md              # Project documentation
```

---

## 📜 Usage Guide
### 1️⃣ Running the Keylogger
Navigate to the project folder and execute:
```bash
python3 Python_Keylogger.py
```
This will start the keylogger in the background, logging all keystrokes to `keylog.txt`.

### 2️⃣ Checking the Log File
Once the keylogger is running, you can inspect the recorded keystrokes by opening `keylog.txt`:
```bash
cat keylog.txt  # macOS/Linux
notepad keylog.txt  # Windows
```

### 3️⃣ Stopping the Keylogger
- If running in a terminal, stop it using `CTRL + C`.
- If running as a background process, use:
```bash
pkill -f Python_Keylogger.py  # macOS/Linux
```

---

## 📁 Attached Files
1. ✅ **GitHub Repository**: [View the Project on GitHub](https://github.com/Shivansh1811/Keylogger)
2. ✅ **Python Script**: `Python_Keylogger.py` (Keylogger logic)
3. ✅ **Output File**: `keylog.txt` (Captured keystrokes with timestamps)

---

## ⚠ Legal & Ethical Considerations
- **Use only with explicit permission**. Unauthorized use may be illegal.
- Designed for **ethical hacking and security research**.
- Always follow ethical guidelines when using monitoring tools.

---


