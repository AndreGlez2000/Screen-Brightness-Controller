# 🖥️ Screen Brightness Control

A retro-styled desktop application for controlling brightness across multiple monitors with ease.

![Demo](./screenshots/retro.gif)

## 🎯 Motivation

Managing brightness on multiple monitors can be tedious - constantly switching between physical monitor buttons or diving into display settings. This tool was created to simplify that process by providing a centralized, intuitive interface to control the brightness of all connected displays from one place.

## ✨ Features

- 🎮 **Retro 80's Cyberpunk UI** - Eye-catching neon aesthetic with purple/cyan gradients
- 🖥️ **Multi-Monitor Support** - Control brightness for each connected display individually
- 🎚️ **Real-time Adjustment** - Smooth slider control from 1-100%
- ⚡ **Instant Feedback** - Live brightness percentage display
- 🎨 **Modern PyQt5 Interface** - Responsive and visually appealing design

## 🚀 Installation

### Option 1: Download Pre-built Executable (Recommended)

**[⬇️ Download screen-brightness.exe](https://github.com/AndreGlez2000/Screen-Brightness-Controller/raw/main/screen-brightness.exe)**

Simply download and run the executable - no installation required!

### Option 2: Run from Source

#### Prerequisites

- Python 3.8 or higher
- Windows 10/11 (required for brightness control API)

#### Setup

1. Clone the repository:
```bash
git clone https://github.com/AndreGlez2000/Screen-Brightness-Controller.git
cd Screen-Brightness-Controller
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install PyQt5 screen-brightness-control
```

3. Run the application:
```bash
python main.py
```

## 📦 Building Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name screen-brightness main.py
```

The executable will be generated in the `dist/` folder.

## 🎮 Usage

1. Launch the application
2. Select your desired monitor from the list of available displays
3. Adjust the brightness using the slider (1-100%)
4. The changes apply instantly to the selected monitor
5. Switch between monitors as needed

## 🛠️ Technologies Used

- **Python** - Core programming language
- **PyQt5** - Modern GUI framework
- **screen-brightness-control** - Cross-platform brightness control library
- **Courier New** - Retro terminal-style font

## 📋 Requirements

```
PyQt5>=5.15.0
screen-brightness-control>=0.20.0
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- The application requires Windows 10/11 for proper brightness control functionality
- Some monitors may not support software-based brightness control

## 👨‍💻 Author

Created with ❤️ by [AndreGlez2000](https://github.com/AndreGlez2000)

## 🙏 Acknowledgments

- Inspired by the need for better multi-monitor brightness management
- Retro UI design influenced by 80's cyberpunk aesthetics
- Built with the amazing Python community libraries

---

⭐ If you find this project useful, please consider giving it a star!
