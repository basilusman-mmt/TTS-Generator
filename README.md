# 🎙️ AI Voice Studio (TTS v2.0)

**A lightweight, zero-cost, offline Text-to-Speech (TTS) CLI studio built in Python.**  
Turn raw scripts into live speech or exportable audio files for YouTube voiceovers, ad prototypes, and accessibility testing—without API fees, internet dependency, or driver crashes.

---

## 🎯 The Client Problem & Solution

### The Problem
Content creators, indie developers, and marketing agencies face three common bottlenecks when producing quick voiceovers or audio prototypes:
1. **Recurring API Costs & Privacy Risks:** Cloud TTS tools charge per character, require internet access, and send proprietary scripts to third-party servers.
2. **Bloated Workflows:** Opening heavy DAWs or web dashboards just to test how a 10-second ad copy sounds slows down creative iteration.
3. **Python TTS Driver Locks:** Standard offline Python scripts using `pyttsx3` frequently freeze or crash on Windows (`sapi5`) after speaking a single sentence, breaking continuous studio workflows.

### The Solution
**AI Voice Studio (TTS v2.0)** solves these issues with an instant, terminal-based audio booth:
* **100% Offline & Free:** Uses native OS speech engines—zero API keys, zero subscriptions, and total script privacy.
* **Rapid Prototyping:** Test pacing, switch voices, and export `.wav`/`.mp3` files in seconds directly from the command line.
* **Engineered for Stability:** Implements a per-utterance driver re-initialization loop that eliminates Windows `sapi5` audio locks for uninterrupted sessions.

---

## ✨ Key Features

* **⚡ Live Speech Preview:** Type any sentence and hear it spoken aloud immediately.
* **🗣️ On-the-Fly Voice Switching:** Cycle through all installed OS voices (Male/Female/Regional) mid-session.
* **🎚️ Precision Pacing Control:** Fine-tune speaking rates from `50` to `400` Words Per Minute (WPM) to match video cuts or ad timings.
* **💾 Instant Audio Export:** Render scripts directly to `.wav` or `.mp3` files for immediate import into Premiere Pro, CapCut, or Audacity.
* **🛡️ Crash-Free Engine Loop:** Automatically resets the TTS driver after each utterance to prevent OS audio buffer deadlocks.
* **💻 Cross-Platform CLI:** Runs smoothly on Windows, macOS, and Linux with clean ANSI terminal styling.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.7+**
* `pyttsx3` library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd tts_generator
   ```

2. **Install dependencies:**
   ```bash
   pip install pyttsx3
   ```
   > **Linux Users:** Ensure `espeak` or `libespeak1` is installed via your system package manager (e.g., `sudo apt install espeak`).

3. **Launch the studio:**
   ```bash
   python text_to_speech.py
   ```

---

## 🎮 Studio Commands

Type any text and press **Enter** to audition it live, or use the slash commands below to control the studio:

| Command | Action | Use Case |
| :--- | :--- | :--- |
| `<any text>` | Speaks text aloud using active settings | Rapidly auditioning script lines and pacing |
| `/voice` | Cycles to the next available system voice | Comparing narrator tones (e.g., Male vs. Female) |
| `/speed` | Sets speaking rate (`50` – `400` WPM) | Fitting voiceovers into strict ad time limits |
| `/save` | Prompts for text & filename to export audio | Generating ready-to-edit `.wav` or `.mp3` assets |
| `/exit` | Safely closes the studio (`exit`, `quit`, `Ctrl+C`) | Cleanly releasing system audio resources |

---

## 🛠️ Default Studio Configuration

* **Default Speaking Rate:** `160 WPM` *(Standard conversational/YouTube narration pace)*
* **Volume Level:** `100%` (`1.0`)
* **Default Export Format:** `.wav` *(Applied automatically if no extension is typed)*

---


## Photos

<img width="835" height="449" alt="image" src="https://github.com/user-attachments/assets/6d6c471f-8cf2-4f97-80fc-87ab6e3e2395" />
<img width="1062" height="453" alt="image" src="https://github.com/user-attachments/assets/d8747b82-f673-4bc6-986d-cee057643c94" />
