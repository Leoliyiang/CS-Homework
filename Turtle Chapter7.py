import turtle
wn = turtle.Screen()
lo = turtle.Turtle()
#for (angle,distance) in [(160, 20), (-43, 10), (270, 8), (-43, 12)]:
 #    lo.left(angle)
  #   lo.forward(distance)
s=100
r=(s**2/2)**0.5
d=(2*s**2)**.5
 
path = [(90,s),(-45,r),(-90,r),(-45,s),(-135,d),(-135,s),(-135,d),(135,s)]
for (angle_house,distance_house) in path:
     lo.left(angle_house)
     lo.forward(distance_house)

print(lo.heading())  
wn.mainloop()
