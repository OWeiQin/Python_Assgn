#Done by Wei Qin, S10257453H, P07

#read data from file, append data into a list of dicts
info = []
with open("carpark-information.csv", "r") as file:
    data = file.readlines()
    for line in data[1:]:
        row = line.strip().split(",")
        #store each element as a dict in list
        infos = {"carpark_num" : row[0],\
                 "type" : row[1],\
                 "system" : row[2],\
                 "address" : row[3]}
        info.append(infos)
        
#menu func
def menu():
    print("MENU")
    print("====")
    print("[1]  Display Total Number of Carparks in 'carpark-information.csv'")
    print("[2]  Display All Basement Carparks in 'carpark-information.csv'")
    print("[3]  Read Carpark Availability Data File")
    print("[4]  Print Total Number of Carparks in the File Read in [3]")
    print("[5]  Display Carparks Without Available Lots")
    print("[6]  Display Carparks With At Least x% Available Lots")
    print("[7]  Display Addresses of Carparks With At Least x% Available Lots")
    print("[8]  Display All Carparks At X Location")
    print("[9]  Display Carpark with the Most Parking Lots")
    print("[10] Create an Output File with Carpark Availability with Addresses and Sort by Lots Available") 
    print("[0]  Exit")

#func, print total number of carpark in file  
def choice1():
    print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
    print("Total Number of carparks in 'carpark-information.csv': {}".format(len(info)))

#func, print all basement carpark in file and total number
def choice2():
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
    count = 0
    print("{:10} {:18} {:7}".format("Carpark No", "Carpark Type", "Address"))
    for i in range(len(info)): #search for all basement carpark with a loop
        if info[i]["type"] == "BASEMENT CAR PARK":
            print("{:10} {:18} {:7}".format(info[i]["carpark_num"], info[i]["type"], info[i]["address"]))
            count += 1
    print("Total number: {}".format(count))

#func to open input file and display filename
def choice3():
    print("Option 3: Read Carpark Availability Data File")
    while True:
        try: #loop for invalid file name
            filename = input("Enter the file name: ")
            file = open(filename, "r")
            content = file.readlines()
            print(content[0])
            break
        except:
            print("File does not exist. Please enter a valid filename.")
        else:
            continue
    return content

#func, adding unique carpark to list to count and print the total number 
def choice4(content):
    print("Option 4: Print Total Number of Carparks in the File Read in [3]")
    count_carpark = []
    for items in content[2:]:
        item = items.strip().split(",")
        if item not in count_carpark:
            count_carpark.append(item)
    print("Total Number of Carparks in the File: {}".format(len(count_carpark)))

#func, print carpark with 0 lots and total number of carparks with 0 lots
def choice5(content):
    print("Option 5: Display Carparls without Available Lots")
    carparks = []
    zerolot = []
    for items in content[2:]:
        item = items.strip().split(",")
        carparks.append(item)
    for i in range(len(carparks)): #loop to find carpark with 0 lots
        if carparks[i][2] == "0":
            print("Carpark Number: {}".format(carparks[i][0]))
            zerolot.append(carparks[i])
    print("Total number: {}".format(len(zerolot)))

#func, user input x%, print carparks with x% lots and total number of carparks
def choice6(content):
    print("Option 6: Display Carparks With At Least x% Available Lots")
    carparks = []
    percent_list = []
    new_carpark = []
    for items in content[2:]:
        item = items.strip().split(",")
        carparks.append(item)
    while True: #loop for invalid percentage input
        try:
            percent = int(input("Enter the percentage required: "))
            percent = abs(percent) #make the input postive
            print("{:11} {:10}  {:14}  {:10}".format("Carpark No", "Total Lots", "Lots Available", "Percentage"))
            for i in range(len(carparks)):
                if carparks[i][2] != "0": 
                    p = (int(carparks[i][2]) / int(carparks[i][1])) * 100
                    if p >= percent and percent > 0: #loop to find and add the input percentage to list and the corresponding carpark info
                        percent_list.append(p)
                        new_carpark.append(carparks[i])
            for j in range(len(percent_list)):
                print("{:<11} {:>10}  {:>14}  {:>10.1f}".format(new_carpark[j][0], new_carpark[j][1], new_carpark[j][2], percent_list[j]))
            print("Total number: {}".format(len(percent_list)))
            break
        except:
            print("Invalid percentage. Please enter a valid percentage.")
        else:
            continue

#func, print address of carparks with x% lots available
def choice7(content):
    print("Option 7: Display Addresses of Carparks With At Least x% Available Lots")
    carparks = []
    percent_list = []
    new_carpark = []
    address = []
    for items in content[2:]:
        item = items.strip().split(",")
        carparks.append(item)
    while True: #loop for invalid percentage input
        try:
            percent = int(input("Enter the percentage required: "))
            percent = abs(percent)
            print("{:11} {:10}  {:14}  {:10}  {:7}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))
            for i in range(len(carparks)):
                if carparks[i][2] != "0":
                    p = (int(carparks[i][2]) / int(carparks[i][1])) * 100
                    if p >= percent:
                        percent_list.append(p)
                        new_carpark.append(carparks[i])
                        for key, value in enumerate(info): #to find which index the carpark num is from the list of dicts
                            if value["carpark_num"] == carparks[i][0]:
                                address.append(info[key]["address"])
            for j in range(len(percent_list)):
                print("{:<11} {:>10}  {:>14}  {:>10.1f}  {:<7}".format(new_carpark[j][0], new_carpark[j][1], new_carpark[j][2], percent_list[j], address[j]))
            print("Total number: {}".format(len(percent_list)))
            break
        except:
            print("Invalid percentage. Please enter a valid percentage.")
        else:
            continue

#func get user input for location and display output similar to option7 for the given location
def choice8(content):
    print("Option 8: Display All Carparks At X Location")
    place = input("Enter a location: ")
    carparks = []
    percent_list = []
    address = []
    new_carpark = []
    for items in content[2:]:
        item = items.strip().split(",")
        carparks.append(item)
    for index, dictionary in enumerate(info):
        for key, value in dictionary.items():
            if place.upper() in value:
                address.append(value)
                for i in range(len(carparks)):
                    if info[index]["carpark_num"] == carparks[i][0]:
                        new_carpark.append(carparks[i])
                        p = (int(carparks[i][2]) / int(carparks[i][1])) * 100
                        percent_list.append(p)
    if len(percent_list) == 0:
        print("No carpark found at {}".format(place))
    else:
        print("{:11} {:10}  {:14}  {:10}  {:7}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))
        for k in range(len(percent_list)):
            print("{:<11} {:>10}  {:>14}  {:>10.1f}  {:<7}".format(new_carpark[k][0], new_carpark[k][1], new_carpark[k][2], percent_list[k], address[k]))
        print("Total number of carparks found: {}".format(len(percent_list)))

#func that display information of carpark with most parking lots
def choice9(content):
    print("Option 9: Display Carpark with the Most Parking Lots")
    carparks = []
    address= []
    new_carpark = []
    percent_list = []
    types = []
    system = []
    most = 0
    for items in content[2:]:
        item = items.strip().split(",")
        carparks.append(item)
    print("{:11} {:21}  {:22}  {:10}  {:14}  {:10}  {:7}".format("Carpark No", "Carpark Type", "Type of Parking System", "Total Lots", "Lots Available", "Percentage", "Address"))
    for i in range(len(carparks)):
        if int(carparks[i][1]) > most:
            most = int(carparks[i][1])
    for i in range(len(carparks)):
        if carparks[i][1] == str(most):
            new_carpark.append(carparks[i])
            for key, value in enumerate(info):
                if value["carpark_num"] == carparks[i][0]:
                    address.append(info[key]["address"])
                    types.append(info[key]["type"])
                    system.append(info[key]["system"])
                    p = (int(carparks[i][2]) / int(carparks[i][1])) * 100
                    percent_list.append(p)
    print("{:<11} {:<21}  {:<22}  {:>10}  {:>14}  {:>10.1f}  {:<7}".format(new_carpark[0][0], types[0], system[0], new_carpark[0][1], new_carpark[0][2], percent_list[0], address[0]))

def choice10(content):
    carparks = []
    new_carpark = []
    for items in content[2:]:
        item = items.strip().split(",")
        carparks.append(item)
    new = sorted(carparks, key=lambda x: int(x[2])) #sort the lots in ascending order
    for i in range(len(carparks)):
        for key, value in enumerate(info):
            if value["carpark_num"] == new[i][0]:
                new_carpark.append([new[i][0], new[i][1], new[i][2], info[key]["address"]])
    with open("carpark-availability-with-addresses.csv", "w") as output_file:
        output_file.write(content[0])
        output_file.write("Carpark No,Total Lots,Lots Available,Address\n")
        for i in range(len(new_carpark)):
            output_file.write(",".join(new_carpark[i]) + "\n") #convert all info to strings
     
#infinite loop to call func
while True:
    try:
        menu()
        option = int(input("Enter your option: "))
    except:
        print("Please enter a valid option number.")
    else:
        if option == 0:
            break
        elif option == 1:
            choice1()
        elif option == 2:
            choice2()
        elif option == 3:
            content = choice3()
        try:
            if option == 4:
                choice4(content)
            elif option == 5:
                choice5(content)
            elif option == 6:
                choice6(content)
            elif option == 7:
                choice7(content)
            elif option == 8:
                choice8(content)
            elif option == 9:
                choice9(content)
            elif option == 10:
                choice10(content)
        except:
            print("You can only choose this option after choosing option 3.")
        else:
            continue




