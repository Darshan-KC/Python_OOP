## Exercies 11 - Drink water Remainder
# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

# firts install plyer through pip
# pip install plyer

import time
from plyer import notification

def remind_to_drink_water():
    notification.notify(
        title='Hydration Reminder',
        message='Time to drink water! Stay hydrated.',
        app_name='Water Reminder',
        timeout=10  # notification will disappear after 10 seconds
    )

def main():
    interval = 60 * 60  # 1 hour in seconds
    while True:
        remind_to_drink_water()
        time.sleep(interval)

if __name__ == "__main__":
    main()

