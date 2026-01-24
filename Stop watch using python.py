# lets make a stop watch 
import time

my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0, -1):
    second = x % 60
    minute = (x // 60) % 60
    hour = (x // 3600) % 24
    day = (x // 86400)
    print(f"{day} days {hour:02}:{minute:02}:{second:02}", end="\r")

    time.sleep(1)

print("Times UP")