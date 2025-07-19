import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print("Enter names to shout out (type 'done' when finished):")

while True:
    name = input("Name: ")
    if name.lower() == "done":
        print("All shout-outs complete! 🎉")
        break
    text = f"Shout out to {name}!"
    print(text)  # Optional: shows what's being said
    engine.say(text)
    engine.runAndWait()