import pyttsx3
import time
engine = pyttsx3.init()
name = input("Enter your name for the water drinking reminder: ")
def main():
  if not name:
    name = "User"
text = f"It's time to drink water! {name}"
def remind_to_drink_water():
     engine.say(text)
     engine.runAndWait()
try:
     while True:
      remind_to_drink_water()
      time.sleep(3600)  # Remind every hour
except KeyboardInterrupt:
    print("Water drinking reminder stopped.")
main()