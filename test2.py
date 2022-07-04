
string1 = f"\033[1;32m Bright Green"
narco = ""
dictionary = {
    "a1": {"btype": "#","position": ""},
    "a2": {"btype": "#","position": ""},
    "a3": {"btype": "#","position": ""},
}

def Build():
    building_position = str(input("Please input a position: "))
    building_type = str(input("Please input a type: "))

    dictionary[building_position]['btype'] = building_type[0]
    print(f"  1 2 3\na  {dictionary['a1']['btype']} {dictionary['a2']['btype']} {dictionary['a3']['btype']}")

while narco != "exit":
    narco = str(input("What do you want to do: ").lower())
    if narco == "build":
        Build()