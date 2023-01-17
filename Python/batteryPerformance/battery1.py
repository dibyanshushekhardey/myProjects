import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged:
	print("Battery is charging at {}%".format(percent))
else:
	print("Battery is at {}%".format(percent))

