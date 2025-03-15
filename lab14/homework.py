from datetime import datetime, timedelta
import time
import calendar

# Lab Exercise 1: Displaying the Current Date and Time
current_time = datetime.now()
print("Current Date and Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Lab Exercise 2: Calculating the Difference Between Two Dates
new_years_eve = datetime(current_time.year, 12, 31)
days_remaining = (new_years_eve - current_time).days
print("Days until New Year's Eve:", days_remaining)

# Lab Exercise 3: Implementing a Countdown Timer
def countdown_timer(seconds):
    end_time = datetime.now() + timedelta(seconds=seconds)
    while datetime.now() < end_time:
        remaining_time = (end_time - datetime.now()).seconds
        print(f"Time remaining: {remaining_time} seconds", end='\r')
        time.sleep(1)
    print("Timer finished!")

# Uncomment the line below to test the countdown timer
# countdown_timer(10)

# Lab Exercise 4: Creating a Simple Month Calendar
def display_calendar(year, month):
    print(calendar.month(year, month))

# Example: February 2025
display_calendar(2025, 2)
