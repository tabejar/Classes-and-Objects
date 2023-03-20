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

  def printOut():
    print(f'this house has {windows} windows, the color is {color} and {floors} floors')

    
redHouse = House(3, 15, 20, "red", 2, True)
print(redHouse.area(34, 56))
print(redHouse.printOut())

blueHouse = House(5, 40, 65, "blue", 3, True)
print(blueHouse.area(54,25))
print(blueHouse.printOut())

orangeHouse = House(5, 15, 25, "orange", 1, False)
print(orangeHouse.area(51, 47))
print(orangeHouse.printOut())
