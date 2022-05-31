import random
# Possible options for user input referanced in game loop
building_types = ["house", "office", "factory"]
positions = [1, 2, 3, 4]
narcos = ["exit", "build", "destroy", "check", "taxes"]

# building values for adjacent buildings
building_values = {
    "house": 100,
    "office": 150,
    "factory": 200
}
house_building_values = {
    "h": 1.25,
    "o": 1,
    "f": 0.75
}
office_building_values = {
    "h": 1.25,
    "o": 1.25,
    "f": 0.75
}
factory_building_values = {
    "h": 0.75,
    "o": 0.75,
    "f": 1.25
}
currency = 0
population = 0

# Class used to create building objects and alter them with methods
class plot: 

    def __init__(self, position, building_type, population, land_value, tax, is_building = False):
        self.position = position
        self.building_type = building_type
        self.population = population
        self.land_value = land_value
        self.tax = tax
        self.is_building = is_building
    def Get_attributes(self):
        return self.position, self.building_type, self.population, self.land_value

    def Set_attributes(self, building_type):
        if (building_type in building_types):
            self.building_type = building_type
        self.population = random.randrange(1, 4)
        self.tax = building_values[self.building_type]
        self.is_building = True

    def Destroy_attributes(self):
        self.position = 0
        self.building_type = ""
        self.population = 0
        self.land_value = 0
        self.is_building = False

buildings: list[plot] = []


# Building objects
Building1 = plot(0, "", 0, 0, 0, False)
Building2 = plot(1, "", 0, 0, 0, False)
Building3 = plot(2, "", 0, 0, 0, False)
Building4 = plot(3, "", 0, 0, 0, False)
Building5 = plot(4, "", 0, 0, 0, False)
Building6 = plot(5, "", 0, 0, 0, False)
Building7 = plot(6, "", 0, 0, 0, False)
Building8 = plot(7, "", 0, 0, 0, False)
Building9 = plot(8, "", 0, 0, 0, False)
Building10 = plot(9, "", 0, 0, 0, False)
Building11 = plot(10, "", 0, 0, 0, False)
Building12 = plot(11, "", 0, 0, 0, False)
Building13 = plot(12, "", 0, 0, 0, False)
Building14 = plot(13, "", 0, 0, 0, False)
Building15 = plot(14, "", 0, 0, 0, False)
Building16 = plot(15, "", 0, 0, 0, False)
Building17 = plot(16, "", 0, 0, 0, False)
Building18 = plot(17, "", 0, 0, 0, False)
Building19 = plot(18, "", 0, 0, 0, False)
Building20 = plot(19, "", 0, 0, 0, False)
Building21 = plot(20, "", 0, 0, 0, False)
Building22 = plot(21, "", 0, 0, 0, False)
Building23 = plot(22, "", 0, 0, 0, False)
Building24 = plot(23, "", 0, 0, 0, False)
Building25 = plot(24, "", 0, 0, 0, False)
buildings.append(Building1)
buildings.append(Building2)
buildings.append(Building3)
buildings.append(Building4)
buildings.append(Building5)
buildings.append(Building6)
buildings.append(Building7)
buildings.append(Building8)
buildings.append(Building9)
buildings.append(Building10)
buildings.append(Building11)
buildings.append(Building12)
buildings.append(Building13)
buildings.append(Building14)
buildings.append(Building15)
buildings.append(Building16)
buildings.append(Building17)
buildings.append(Building18)
buildings.append(Building19)
buildings.append(Building20)
buildings.append(Building21)
buildings.append(Building22)
buildings.append(Building23)
buildings.append(Building24)
buildings.append(Building25)


# Function used to tax the poor
def Tax():
    
    total_taxed = 0
    for i in range(len(buildings)):
        count = 0
        tax_amount = 0
        building = buildings[i]
        if not building.is_building:
            continue

        if i > 4:
            above = buildings[i - 5]
            if above.is_building:
                count += 1
                if above.building_type == "house":
                    tax_amount += house_building_values[above.building_type[0]]
                elif above.building_type == "office":
                    tax_amount += office_building_values[above.building_type[0]]
                else:
                    tax_amount += factory_building_values[above.building_type[0]]

        if i != 0 and i % 5 != 0:
            left = buildings[i - 1]
            if left.is_building:
                count += 1
                if left.building_type == "house":
                    tax_amount += house_building_values[left.building_type[0]]
                elif left.building_type == "office":
                    tax_amount += office_building_values[left.building_type[0]]
                else:
                    tax_amount += factory_building_values[left.building_type[0]]

        if i != 4 and i % 4 != 0:
            right = buildings[i + 1]
            if right.is_building:
                count += 1
                if right.building_type == "house":
                    tax_amount += house_building_values[right.building_type[0]]
                elif right.building_type == "office":
                    tax_amount += office_building_values[right.building_type[0]]
                else:
                    tax_amount += factory_building_values[right.building_type[0]]

        if i < 19:
            bottom = buildings[i + 5]
            if bottom.is_building:
                count += 1
                if bottom.building_type == "house":
                    tax_amount += house_building_values[bottom.building_type[0]]
                elif bottom.building_type == "office":
                    tax_amount += office_building_values[bottom.building_type[0]]
                else:
                    tax_amount += factory_building_values[bottom.building_type[0]]
                    
        if tax_amount < 1:
            tax_amount = 1
        else:
            tax_amount /= count
        print(tax_amount)

        taxed = building_values[building.building_type] * tax_amount
        total_taxed += taxed

    return total_taxed

# function used to gather all population values from instances of building class
def Population():
    houses_population = 0
    for house in buildings:
        houses_population += house.population
    return houses_population





# Game loop used to alter building objects and exit game
while(True):
    print(f"Money: {currency} Population: {Population()}\n01, 02, 03, 04, 05\n06, 07, 08, 09, 10\n11, 12, 13, 14, 15\n16, 17, 18, 19, 20\n21, 22, 23, 24, 25")
    narco = str(input("What do you want to do: "))
    if narco in narcos:
        if narco == "exit":
            exit()
        elif narco == "build":
            building_number = int(input("what building number: "))
            buildings[building_number - 1].Set_attributes(str(input("What building type: ")), )
        elif narco == "check":
            building_number = int(input("what building number: "))
            print(buildings[building_number - 1].Get_attributes())
        elif narco == "destroy":
            building_number = int(input("what building number: "))
            buildings[building_number - 1].Destroy_attributes()
        elif narco == "taxes":
            currency = currency + Tax()
            print(currency)
    else:
        pass