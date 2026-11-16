# 🎙️ AI Voice Studio (TTS v2.0)

A lightweight, command-line Text-to-Speech (TTS) studio built in Python. Turn any text into live speech or exportable audio files for YouTube voiceovers, brand promotions, and quick audio prototyping—completely offline.

---

## ✨ Features

* **Live Text-to-Speech:** Type any sentence and hear it spoken aloud instantly.
* **Voice Switching:** Cycle through all system-installed voices (e.g., Male/Female) on the fly.
* **Custom Speech Rate:** Adjust speaking speed anywhere from `50` to `400` Words Per Minute (WPM).
* **Audio Export:** Save spoken text directly to `.wav` or `.mp3` files.
* **Crash-Free Engine Loop:** Re-initializes the TTS driver per utterance to prevent Windows `sapi5` audio locks during continuous use.
* **Cross-Platform:** Works seamlessly on Windows, macOS, and Linux with ANSI terminal styling.

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.7+**
* `pyttsx3` library

### Installation

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com
   cd tts_generator
   ```

2. Install the required dependency:
   ```bash
   pip install pyttsx3
   ```
   *(Note: On Linux, you may also need `espeak` or `libespeak1` installed via your package manager.)*

3. Run the application:
   ```bash
   python main.py
   ```

---

## 🎮 Commands

Once inside the studio, simply type your text and press **Enter** to hear it spoken, or use any of the built-in slash commands:

| Command | Description |
| :--- | :--- |
| `<any text>` | Speaks the entered text out loud using current settings |
| `/voice` | Cycles to the next available system voice |
| `/speed` | Prompts you to set a new speaking rate (`50` – `400` WPM) |
| `/save` | Prompts for text and a filename to export speech to an audio file |
| `/exit` | Cleanly closes the application (also supports `exit`, `quit`, or `Ctrl+C`) |

---

## 🛠️ Default Settings

* **Speed:** `160 WPM`
* **Volume:** `100%` (`1.0`)
* **Default Export Format:** `.wav` (if no file extension is specified)

---
