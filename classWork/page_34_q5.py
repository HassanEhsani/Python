n = int(input())

start_time = 480+30
lesson = 45
breake = 10
if(n == 1):
    tk = start_time+lesson
else:
    tk = start_time+lesson+(n-1)*(lesson+breake)
h = tk // 60
m = tk % 60
print(h, ':', m)
