building_types = ["house", "office", "factory"]
positions = [1, 2, 3, 4]
narcos = ["exit", "build", "destroy", "check"]
class land():
    pass

class plot: 

    def __init__(self, position, building_type, quality, size, population, land_value):
        self.position = position
        self.building_type = building_type
        self.quality = quality
        self.size = size
        self.population = population
        self.land_value = land_value
        
    def Get_attributes(self):
        return self.position, self.building_type, self.quality, self.size, self.population, self.land_value

    def Set_attributes(self, position, building_type):
        if (position in positions):
            self.position = position
        if (building_type in building_types):
            self.building_type = building_type

    def Destroy_attributes(self):
        self.position = 0
        self.building_type = ""
        self.quality = 0
        self.size = 0
        self.population = 0
        self.land_value = 0
House1 = plot(0, "", 0, 0, 0, 0)

while(True):
    narco = str(input("What do you want to do: "))
    if narco in narcos:
        if narco == "exit":
            exit()
        elif narco == "build":
            House1.Set_attributes(int(input("What location: ")), str(input("What building type: ")))
        elif narco == "check":
            print(House1.Get_attributes())
        elif narco == "destroy":
            House1.Destroy_attributes()
    else:
        pass