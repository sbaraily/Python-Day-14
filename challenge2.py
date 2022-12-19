import time

t = time.localtime()
current_time = time.strftime('%H:%M:%S',t)
print("The Current time is: " + current_time)
hour = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))

if (hour>=0 and hour <12):
  print("Good Morning!!")
elif (hour >=12 and hour <= 17):
  print("Good Afternoon!!")
elif(hour > 17 and hour < 19):
  print("Good Evening!!")
else:
  print("Good Night!!")
