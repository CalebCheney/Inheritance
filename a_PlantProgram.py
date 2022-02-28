import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

#subclass can draw attiributes from superclass to works
print(sunflower.get_color())
print(sunflower.get_petals())

#instance in superclass so wont work
#print(primrose.get_petals())
