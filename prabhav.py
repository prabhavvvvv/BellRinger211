from datetime import datetime

current_time = datetime.now() # displays the current time (military format)
print("The current time is" ,current_time, )

def hours():
    end_time = datetime(current_time, 2, 14, 25) # format is month, day, and year
    if current_time > end_time:
        return (end_time - current_time).seconds / 3600 # 3600 seconds in one hour. so this is an appropriate calculation

print(f"The difference in hours is {hours()} hours")
