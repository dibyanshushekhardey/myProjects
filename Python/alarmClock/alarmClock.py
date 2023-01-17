import datetime
import time

alarm_time = input("What time would you like to set the alarm for (HH:MM)?")

while True:
	current_time = datetime.datetime.now().strftime("%H:%M")
	if current_time == alarm_time:
		print("Wake Up!")
		break
	else:
		time.sleep(1)
