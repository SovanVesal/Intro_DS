#solution2
#convert the second into hour,minute and s

seconds1 = 86399

hour = seconds1//3600

minute =  (seconds1%3600)//60

s= seconds1%60
print(hour,"h",minute,"mn"
      ,s,"s")


