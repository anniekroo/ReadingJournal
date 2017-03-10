minuteTimeStart = (6*60) + 52
mileSlow = 8 + (15/60)
milesFast =7 + (12/60)
totalMinutes = minuteTimeStart + mileSlow * 2 + milesFast * 3
hours = int(totalMinutes/60)
minutes = int(totalMinutes % 60)
seconds = int((totalMinutes*60)%60)
print('Time = ', hours, ':', minutes,':', seconds)
