# برنامه ای که شعاع و ارتفاع استوانه ای را خوانده و حجم و مساحت کل استاوانه رامحسابه می کند.
from math import radians


pi = 22/7
height = float(input("height of cylinder: "))
radian = float(input("radius of cylinder: "))
volume = pi * radian * radian * height
sur_area = ((2*pi*radian)*height)+((pi*radian ** 2)*2)
print("volume is :", volume)
print("surface Area is: ", sur_area)
