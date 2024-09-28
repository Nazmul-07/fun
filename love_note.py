import time
import os

def clear_screen():
    # This function clears the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def love_note():
    notes = [
        "❤️ You make my heart smile! ❤️",
        "🌹 Every moment with you is precious! 🌹",
        "💖 You are my sunshine on a cloudy day! 💖",
        "🌟 I cherish every moment spent with you! 🌟",
        "💞 Together, we can conquer the world! 💞"
    ]
    
    print("💌 Sending you a love note! 💌")
    time.sleep(1)

    for note in notes:
        clear_screen()  # Clear the screen before showing the next note
        print(f"\n{note}\n")
        time.sleep(2)  # 3 seconds delay between each note

    print("💖 Thank you for being you! 💖")
    
if __name__ == "__main__":
    love_note()
