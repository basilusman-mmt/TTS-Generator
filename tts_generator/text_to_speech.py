import os
import sys
import time
import pyttsx3

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_voices():
    try:
        driver = 'sapi5' if os.name == 'nt' else None
        engine = pyttsx3.init(driver)
        voices = engine.getProperty('voices')
        engine.stop()
        del engine
        return voices
    except Exception as e:
        print(f"{Colors.RED}[!] Error initializing TTS engine: {e}{Colors.RESET}")
        sys.exit(1)

def speak_text(text, voice_id=None, rate=160):
    driver = 'sapi5' if os.name == 'nt' else None
    engine = pyttsx3.init(driver)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', 1.0)
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine

def save_audio(text, filename, voice_id=None, rate=160):
    driver = 'sapi5' if os.name == 'nt' else None
    engine = pyttsx3.init(driver)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', 1.0)
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.save_to_file(text, filename)
    engine.runAndWait()
    engine.stop()
    del engine

def print_banner(rate, voice_name):
    clear_terminal()
    print(f"""{Colors.CYAN}{Colors.BOLD}
  ╔══════════════════════════════════════════════════════════╗
  ║             🎙️  AI VOICE STUDIO (TTS v2.0)                ║
  ╚══════════════════════════════════════════════════════════╝{Colors.RESET}
  {Colors.DIM}Turn your text into crisp, live speech for videos & promos.{Colors.RESET}

  {Colors.YELLOW}Current Settings:{Colors.RESET}
   • {Colors.BOLD}Voice:{Colors.RESET} {voice_name}
   • {Colors.BOLD}Speed:{Colors.RESET} {rate} WPM

  {Colors.GREEN}Commands:{Colors.RESET}
   • Type any text and press {Colors.BOLD}[ENTER]{Colors.RESET} to speak
   • Type {Colors.BOLD}/voice{Colors.RESET} to switch voices
   • Type {Colors.BOLD}/speed{Colors.RESET} to change speaking rate
   • Type {Colors.BOLD}/save{Colors.RESET}  to export text to an audio file
   • Type {Colors.BOLD}/exit{Colors.RESET}  to quit
  {Colors.DIM}────────────────────────────────────────────────────────────{Colors.RESET}""")

def main():
    if os.name == 'nt':
        os.system('')

    voices = get_voices()
    current_voice_idx = 0
    current_rate = 160

    while True:
        voice_name = voices[current_voice_idx].name if voices else "Default"
        voice_id = voices[current_voice_idx].id if voices else None
        print_banner(current_rate, voice_name)

        try:
            user_input = input(f"\n  {Colors.CYAN}❯ Enter text or command:{Colors.RESET} ").strip()
        except KeyboardInterrupt:
            print(f"\n\n  {Colors.YELLOW}Exiting Voice Studio. Goodbye!{Colors.RESET}")
            break

        if not user_input:
            continue

        if user_input.lower() in ['/exit', 'exit', 'quit']:
            print(f"\n  {Colors.YELLOW}Shutting down Voice Studio...{Colors.RESET}")
            time.sleep(0.5)
            break

        elif user_input.lower() == '/voice':
            if len(voices) > 1:
                current_voice_idx = (current_voice_idx + 1) % len(voices)
                print(f"\n  {Colors.GREEN}✔ Switched voice to: {voices[current_voice_idx].name}{Colors.RESET}")
            else:
                print(f"\n  {Colors.RED}[!] Only one system voice found.{Colors.RESET}")
            time.sleep(1.2)

        elif user_input.lower() == '/speed':
            try:
                new_rate = int(input(f"\n  {Colors.YELLOW}Enter new speed (100 = slow, 160 = normal, 220 = fast): {Colors.RESET}"))
                if 50 <= new_rate <= 400:
                    current_rate = new_rate
                    print(f"  {Colors.GREEN}✔ Speed updated to {current_rate} WPM.{Colors.RESET}")
                else:
                    print(f"  {Colors.RED}[!] Please choose a number between 50 and 400.{Colors.RESET}")
            except ValueError:
                print(f"  {Colors.RED}[!] Invalid number.{Colors.RESET}")
            time.sleep(1.2)

        elif user_input.lower() == '/save':
            text_to_save = input(f"\n  {Colors.YELLOW}Enter text to save to audio: {Colors.RESET}").strip()
            filename = input(f"  {Colors.YELLOW}Enter filename (e.g., intro.wav): {Colors.RESET}").strip()
            if text_to_save and filename:
                if not filename.endswith(('.wav', '.mp3')):
                    filename += '.wav'
                save_audio(text_to_save, filename, voice_id, current_rate)
                print(f"  {Colors.GREEN}✔ Saved audio to '{filename}'!{Colors.RESET}")
            time.sleep(1.5)

        else:
            print(f"\n  {Colors.BLUE}🔊 Speaking...{Colors.RESET}", end="\r")
            speak_text(user_input, voice_id, current_rate)
            print(f"  {Colors.GREEN}✔ Done!       {Colors.RESET}")
            time.sleep(0.5)

if __name__ == "__main__":
    main()
