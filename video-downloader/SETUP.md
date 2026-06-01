# 🔧 Setup Guide for Developers

## Prerequisites

- **Python 3.8+** - Download from https://www.python.org
- **FFmpeg** - Download from https://ffmpeg.org/download.html
- **Git** - Download from https://git-scm.com

## Step-by-Step Installation

### 1. Verify Python Installation
```bash
python --version
```
Should show Python 3.8 or higher.

### 2. Verify FFmpeg Installation
```bash
ffmpeg -version
```
If not found, install FFmpeg and add it to your system PATH.

### 3. Clone the Repository
```bash
git clone https://github.com/yourusername/universal-media-downloader.git
cd universal-media-downloader
```

### 4. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run the Application

**Desktop App:**
```bash
python desktop.py
```

**Web Server:**
```bash
python app.py
# Then visit http://127.0.0.1:5000
```

## 🐛 Troubleshooting Setup

### Python not found
- Make sure Python is installed and added to PATH
- Restart your terminal after installing Python

### FFmpeg not found
- Install FFmpeg from https://ffmpeg.org
- Add FFmpeg to system PATH
- Restart terminal

### Virtual environment won't activate
- Try: `python -m venv venv --upgrade`
- Delete venv folder and recreate it

### Permission denied on activate.ps1
- Run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`

### Port 5000 already in use
- Edit `app.py` line: `app.run(debug=True, port=5001)`
- Or kill process using port 5000

## 📦 Project Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| flask | 3.1.3 | Web framework |
| yt-dlp | 2026.3.17 | YouTube downloader |
| pywebview | 6.2.1 | Desktop app UI |

## 🎨 Customization

### Change Port
Edit `app.py`:
```python
app.run(debug=True, port=8000)  # Change 8000 to your port
```

### Change Window Size
Edit `desktop.py`:
```python
webview.create_window(
    title="Media Downloader",
    url="http://127.0.0.1:5000",
    width=800,      # Change width
    height=600,     # Change height
    resizable=True  # Allow resizing
)
```

### Change Default Download Folder
Edit `app.py`:
```python
DOWNLOAD_FOLDER = "C:/MyDownloads"  # Your custom path
```

## 📝 Before Sharing

- [ ] Update README.md with your GitHub username
- [ ] Test on another computer
- [ ] Verify all features work
- [ ] Create .gitignore (included)
- [ ] Add requirements.txt (included)
- [ ] Document any custom changes
- [ ] Add MIT License file

## 🚀 Publishing to GitHub

```bash
git add .
git commit -m "Initial commit: Universal Media Downloader"
git branch -M main
git remote add origin https://github.com/yourusername/universal-media-downloader.git
git push -u origin main
```

## 📱 LinkedIn Post Template

```
🎬 Just released: Universal Media Downloader

A simple desktop app to download videos from multiple platforms (MP4) 
or extract audio (MP3) with a beautiful dark UI.

✨ Features:
- MP4 video & MP3 audio download
- Custom save locations
- Lightning-fast downloads
- Beautiful desktop interface

📦 Open source on GitHub
🔗 [Link to your repo]

Tech: Python, Flask, yt-dlp, PyWebView

⭐ If useful, please star on GitHub!

#Python #OpenSource #Automation
```

## 🎯 Next Steps

1. Test the application thoroughly
2. Create GitHub repository
3. Push code to GitHub
4. Share on LinkedIn with the template above
5. Gather feedback from users
6. Improve based on comments

---

Happy sharing! 🚀
