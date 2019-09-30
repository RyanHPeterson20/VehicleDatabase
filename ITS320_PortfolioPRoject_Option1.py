#Ryan Peterson
#ITS320

#user menu function
def user_input():
    print('Please choose one of the following options: \n1. Add a new vehicle \n2. Remove a vehicle \n3. Update vehicle atrributes \n4. Save to file')
    table_input = input('Make your selection, or press q to quit: ')
    return table_input

#function for entering vehicle data into dictionary and printing out dictionary for user review
def dictionary_vehicles (entry, iterator):
    vehicle_inventory[entry] = dict(list(iterator))
    for a in vehicle_inventory.items():
        print(a)

#inventory search
def inventory_search ():
    print('Select from the following entries: ')
    #loop through inventory keys to show available options for user to select from
    for a in vehicle_inventory.keys():
        print (a)
    #select input
    inventory_select = input('Write desired inventory entry: ')
    return inventory_select

#object automobile class
class automobile (object):
    #class constructor
    def __init__(self, make=None, model=None, color=None, year=None, mileage=None):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    #add vehicle method
    def add_vehicle(self):
        self.__make = str(input('Please enter vehicle make: '))
        self.__model = str(input('Please enter vehicle model: '))
        self.__color = str(input('Please enter vehicle color: '))
        #exception check for non-int entries
        while True:
            try:
                self.__year = int(input('Please enter vehicle year: '))
            except ValueError:
                print('Invalid entry.')
            else:
                break
        #exception check for non-int entries
        while True:
            try:
                self.__mileage = int(input('Please enter vehicle mileage: '))
            except ValueError:
                print ('Invalid entry.')
            else:
                break

    #update vehicle method
    def update_vehicle(self):
        self.__make = str(input('Please update vehicle make: '))
        self.__model = str(input('Please update vehicle model: '))
        self.__color = str(input('Please update vehicle color: '))
        #exception check for non-int entries
        while True:
            try:
                self.__year = int(input('Please update vehicle year: '))
            except ValueError:
                print('Invalid entry.')
            else:
                break
        #exception check for non-int entries
        while True:
            try:
                self.__mileage = int(input('Please update vehicle mileage: '))
            except ValueError:
                print ('Invalid entry.')
            else:
                break

    #removes vehicle method
    def remove_vehicle (self, entry):
        del vehicle_inventory[entry]
        print ('Vehicle entry has been removed.')

    #returns vehicle data from class
    def return_vehicle (self):
        vehicle = [self.__make, self.__model, self.__color, self.__year, self.__mileage]
        return vehicle

#main
if __name__ == "__main__":

    #table input variable build for while loop
    table_input = ()
    #subkeys for dictionary
    key_list = ['Make', 'Model', 'Color', 'Year', 'Mileage']
    #build dictionary
    vehicle_inventory = {}

    #while loop for user input / select from menu
    while table_input != 'q':
        table_input = user_input()

        if table_input == '1':
            # build class
            x = automobile()
            #user input to name database entry
            inv_key = input('Enter name of inventory entry: ')
            if inv_key == vehicle_inventory.keys():
                inv_key = input('Enter name of inventory entry: ')
            else:
                pass
            #add_input = data_input()
            x.add_vehicle()
            #zip together sub keys and values
            user_iterator = zip(key_list, x.return_vehicle())
            #call function for adding to dictionary
            dictionary_vehicles(inv_key, user_iterator)

        elif table_input == '2':
            #remove entry
            #search for appropriate inventory entry
            entry = inventory_search()
            x.remove_vehicle(entry)

        elif table_input == '3':
            #update entry
            #search for appropriate inventory entry
            entry = inventory_search()
            #show selection to user for reference
            print (vehicle_inventory[entry])
            #call update method
            x.update_vehicle()
            #zip together sub keys and values
            user_iterator = zip(key_list, x.return_vehicle())
            #call function for adding to dictionary
            dictionary_vehicles(entry, user_iterator)

        elif table_input == '4':
            #save data to txt file
            file_name = str(input('Enter .txt file to save to: '))
            f = open(file_name, 'w')
            for val in vehicle_inventory.items():
                f.write(str(val) + '\n')
            f.close()
            print('Your file has been save as:', file_name)

        #exit conditional
        elif table_input == 'q':
            print('Thank you for using Python Vehicle Inventory.')

        #validation check
        else:
            print('That was not a valid option, try again')



