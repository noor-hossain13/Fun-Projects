# 🎬 Universal Media Downloader

A simple, fast, and user-friendly desktop application to download videos from any supported platform in MP4 format or extract audio as MP3.

## ✨ Features

- 📥 **Download Videos** - Save online videos in MP4 format
- 🎵 **Extract Audio** - Convert video streams to MP3 audio files
- 📂 **Custom Save Location** - Choose where to save downloaded files
- 🖥️ **Desktop App** - Beautiful UI with dark theme
- ⚡ **Fast & Reliable** - Powered by yt-dlp

## 📋 Requirements

- Python 3.8 or higher
- FFmpeg (required for MP3 conversion)

### Install FFmpeg

**Windows:**
- Download from: https://ffmpeg.org/download.html
- Or use Chocolatey: `choco install ffmpeg`
- Or use Winget: `winget install FFmpeg.FFmpeg`

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/universal-media-downloader.git
cd universal-media-downloader
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

**Activate virtual environment:**
- **Windows:** `.\venv\Scripts\Activate.ps1`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application

**Option A - Desktop App (Recommended):**
```bash
python desktop.py
```
This opens a beautiful desktop window with the app.

**Option B - Web Browser:**
```bash
python app.py
```
Then open your browser and go to: `http://127.0.0.1:5000`

## 🎯 Usage

1. Paste your YouTube URL
2. Choose format:
   - **MP4 Video** - Download the full video
   - **MP3 Audio** - Extract audio only
3. (Optional) Set custom save location
4. Click **DOWNLOAD**
5. Your file will be saved and automatically downloaded

## 📁 Project Structure

```
universal-media-downloader/
├── app.py                 # Flask backend
├── desktop.py             # Desktop application launcher
├── requirements.txt       # Python dependencies
├── run.bat               # Quick start for Windows
├── templates/
│   └── index.html        # Web UI
└── downloads/            # Downloaded files (default)
```

## 🔧 How It Works

- **Flask** - Handles the web server and download logic
- **yt-dlp** - Downloads videos from YouTube
- **FFmpeg** - Converts audio formats (MP3)
- **PyWebView** - Creates the native desktop window

## 📝 Troubleshooting

**"Something went wrong" error:**
- Make sure FFmpeg is installed and in your PATH
- Check that the save folder has write permissions
- Ensure you have a stable internet connection

**Module not found errors:**
- Make sure you're in the virtual environment
- Run: `pip install -r requirements.txt`

**Path issues on Windows:**
- Run the .bat file: `run.bat`

## ⚠️ Important Notes

- **Legal**: Only download content you have permission to download
- **Terms of Service**: Respect YouTube's Terms of Service
- **Stability**: Video availability and download capabilities may change
- **Performance**: Downloads depend on your internet speed and video quality

## 📜 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork the repository
- Create a feature branch
- Submit a pull request

## 💬 Support

If you encounter issues:
1. Check the Troubleshooting section
2. Verify FFmpeg is installed
3. Make sure you're using the latest yt-dlp version
4. Open an issue on GitHub

## 🌟 Show Your Support

If this project helps you, please give it a ⭐ on GitHub!

---

**Made with ❤️ for YouTube lovers**
