def welcome():
    print('1) Square')
    print('2) Rectangle')
    print('3) Triangle')
    print('4) Circle')
   
welcome()
shape = int(input('Please choose the number associated with what shape you want the area of: '))
 
if shape == 1:
    side = int(input('What is the length of one side? '))
    area = side ** 2
    print(area)
elif shape == 2:
    length = int(input('What is the length of the rectangle? '))
    width = int(input('What is the width of the rectangle?'))
    area = length * width
    print(area)
elif shape == 3:
    base = int(input('What is the base of the triangle? '))
    height = int(input('What is the height of the triangle? '))
    area = (base * height)/2
    print(area)
elif shape == 4:
    PI = 3.14
    radius = int(input('What is the radius of the circle? '))
    area = PI * (radius ** 2)
    print(area)
else:
    print('Please enter a vaild number')