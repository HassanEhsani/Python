sec = int(input())
h = sec // 3600
m = (sec-h*3600) // 60
s = sec % 60
print(h,'hour',m,'min',s,'sec' )

