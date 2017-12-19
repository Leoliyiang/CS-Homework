import turtle
wn = turtle.Screen()
lo = turtle.Turtle()
#for (angle,distance) in [(160, 20), (-43, 10), (270, 8), (-43, 12)]:
 #    lo.left(angle)
  #   lo.forward(distance)
 
for (angle_house,distance_house) in [(60, 100), (-120, 100), (-120, 100), (90,100),(90,100),(90,100),(135,100*2**(1/2)),(135,100),(135,100*2**(1/2))]:
     lo.left(angle_house)
     lo.forward(distance_house)
print(lo.heading())  
wn.mainloop()
