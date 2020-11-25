class movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
matrix =movie('The matrix', 6432) 
print(matrix.name)


class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        returnlen(self.cars)
    
    def __getitem__(self,i):

