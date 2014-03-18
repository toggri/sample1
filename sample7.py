# Getting the Current Date and Time

from datetime import datetime

now = datetime.now()

print now
print now.year
print now.month
print now.day

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
