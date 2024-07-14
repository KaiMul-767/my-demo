class Triangle:
    def __init__(self,base,hight):
        self.base = base
        self.hight = hight
    def calculate_area(self):
        area = 0.5 * self.base*self.hight
        print('the area is : ',area)

t1 = Triangle(10,20)
t1.calculate_area()
