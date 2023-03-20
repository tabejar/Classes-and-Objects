#create a house class
class House:
  #constructor method (functions are called methods)
  #variables in classes are called attributes
  def __init__(self, windows, width, height, color, floors, occupied):
    # self.area = area
    self.windows = windows
    self.width = width
    self.height = height
    self.color = color
    self.floors = floors
    self.occupied = occupied

  def area(self, width, height):
    return width * height
  
redHouse = House(3, 15, 20, "red", 2, True)
print(redHouse.area(34, 56))
blueHouse = House(5, 40, 65, "blue", 3, True)
print(blueHouse.area(54,25))