from plyer import notification
import time

name = input("Enter your name for the water drinking reminder: ").strip()
if not name:
    name = "User"

def remind_to_drink_water(name):
    notification.notify(
        title="Water Drinking Reminder",
        message=f"It's time to drink water, {name}! Stay hydrated.",
        app_name="Water Drinking Reminder",
        timeout=10
    )

try:
    while True:
        remind_to_drink_water(name)
        time.sleep(3600)  # Remind every hour
except KeyboardInterrupt:
    print("Water drinking reminder stopped.")

