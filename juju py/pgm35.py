s=int(input("enter the lenght of square:"))
area=lambda s:s*s
print(area(s))
rect_l=int(input("enter the lenght of rectagle:"))
rect_b=int(input("enter the breadth of rectagle:"))
area=lambda rect_l,rect_b:rect_l*rect_b
print(area(rect_l,rect_b))
tri_l=int(input("enter the lenght of triangle:"))
tri_h=int(input("enter the height of triangle:"))
area=lambda tri_l,tri_h:1/2*tri_l*tri_h
print(area(tri_l,tri_h))
