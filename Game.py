# Possible options for user input referanced in game loop
building_types = ["house", "office", "factory"]
positions = [1, 2, 3, 4]
narcos = ["exit", "build", "destroy", "check"]
buildings = []

# Class used to create building objects and alter them with methods
class plot: 

    def __init__(self, position, building_type, population, land_value):
        self.position = position
        self.building_type = building_type
        self.population = population
        self.land_value = land_value
        
    def Get_attributes(self):
        return self.position, self.building_type, self.population, self.land_value

    def Set_attributes(self, building_type):
        if (building_type in building_types):
            self.building_type = building_type

    def Destroy_attributes(self):
        self.position = 0
        self.building_type = ""
        self.population = 0
        self.land_value = 0
    
    def Set_land_value(self):
        self.land_value = self.population * self.building_type

# Building objects
Building1 = plot(0, "", 0, 0)
Building2 = plot(1, "", 0, 0)
buildings.append(Building1)
buildings.append(Building2)

# Game loop used to alter building objects and exit game
while(True):
    buildin = int(input("what building number: "))
    narco = str(input("What do you want to do: "))
    if narco in narcos:
        if narco == "exit":
            exit()
        elif narco == "build":
            buildings[buildin - 1].Set_attributes(str(input("What building type: ")), )
        elif narco == "check":
            print(buildings[buildin - 1].Get_attributes())
        elif narco == "destroy":
            buildings[buildin - 1].Destroy_attributes()
    else:
        pass