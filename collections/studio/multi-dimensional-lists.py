food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food = food.split(",")
equipment = equipment.split(",")
pets = pets.split(",")
sleep_aids = sleep_aids.split(",")

food.sort()
equipment.sort()
pets.sort()
sleep_aids.sort()


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food, equipment, pets, sleep_aids]
print("Cargo Hold:", cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
cabinet_selection = int(input("Select a cabinet (0-3): "))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if cabinet_selection < 0 or cabinet_selection > 3:
    print("Error: Invalid cabinet number")
else:
    print("Cabinet", cabinet_selection, "contains:", cargo_hold[cabinet_selection])


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
if 0 <= cabinet_selection <= 3:
    item = input("Enter an item to search for: ")
    if item in cargo_hold[cabinet_selection]:
        print("Cabinet", cabinet_selection, "DOES contain", item)
    else:
        print("Cabinet", cabinet_selection, "DOES NOT contain", item)