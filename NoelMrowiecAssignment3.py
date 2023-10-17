# INF360 - Programming in Python
# Noel Mrowiec
# Assignment 3
# Ford car database

# Dictionary for each car 
ka = {'name' : 'Ka', 'year introduced' : 1996, 'production of the current model' : 2014, 'generation' : '3rd', 'vehicle information' : "Developed by Ford Brazil as a super mini car"}

fiesta = {'name' : 'Fiesta', 'year introduced' : 1976, 'production of the current model' : 2017, 'generation' : '7th', 'vehicle information' : "Ford's long running subcompact line based on global B-car Platform"}

focus = {'name' : 'Focus', 'year introduced' : 1998, 'production of the current model' : 2018, 'generation' : '3rd', 'vehicle information' : "Ford's Compact car based on global C-car platform"}

mondeo = {'name' : 'Mondeo', 'year introduced' : 1992, 'production of the current model' : 2012, 'generation' : '2nd', 'vehicle information' : "Mid sized passenger sedan with \"One-Ford\" design based on CD4 platform"}

fusion = {'name' : 'Fusion', 'year introduced' : 2005, 'production of the current model' : 2014, 'generation' : '5th', 'vehicle information' : "Similar to Mondero"}

taurus = {'name' : 'Taurus', 'year introduced' : 1986, 'production of the current model' : 2009, 'generation' : '6th', 'vehicle information' : "Full sized car based on D3 platform"}

fiesta_ST = {'name' : 'Fiesta ST', 'year introduced' : 2013, 'production of the current model' : 2013, 'generation' : '1st', 'vehicle information' : "Fiesta's high performance factory tune"}

focus_RS = {'name' : 'Focus RS', 'year introduced' : 2015, 'production of the current model' : 2015, 'generation' : '1st', 'vehicle information' : "Special high performance Focus developed by SVT"}

mustang = {'name' : 'Mustang', 'year introduced' : 1964, 'production of the current model' : 2014, 'generation' : '6th', 'vehicle information' : "Ford's long running pony/muscle car"}

gt = {'name' : 'GT', 'year introduced' : 2004, 'production of the current model' : 2016, 'generation' : '2nd', 'vehicle information' : "Ford's limited production super car inspired by the legendary race car GT40"}

# Function will take a list of the car dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
# The function will do the following:
#1.	take a list as the function arguments
#2.	taking name's values from your original dictionaries, put them to a new dictionary as its keys
#3.	taking the original dictionaries, put them as the values to those keys in your new dictionary
#4.	return the new dictionary
#
def makeDictionaryOfCars(listOfDictionaries):
    # verify that list has at least one element
    dictionary = {}
    if listOfDictionaries:
        for element in listOfDictionaries:
            try:
                dictionary.update({element['name'] : element})
            except:
                print('The \'name\' key was not found. Check data.')

    
    return dictionary

# Function will go through the a dictionary and return a list of all the car's names, sorted alphabetically.
# dictionaryOfCars: Must a dictionary of dictionaries. Running a list thru makeDictionaryOfCars() will yield 
# proper format.  
# The function will do the following:
#1.	take a dictionary as argument. Must have a key value with name of the car. The value must be a dictionary. 
#       return from makeDictionaryOfCars() is value format for the argument.
#2.	for each pair of key:value in the argument dictionary, take the name's value out and put it in a list
#3.	sort the list alphabetically
#4.	return the sorted list
#
def alphabetize(dictionaryOfCars):
    listOfCarNames = []

    # checks if dictionary has at least one element
    if dictionaryOfCars:
        try:
            for car in dictionaryOfCars.values():
                try:
                    # get name from dictionary 
                    listOfCarNames.append(car['name'])
                except:
                    print("Unable to get 'name' from " +str(car))

            listOfCarNames.sort(key=str.lower)
        except:
            print('Error when trying to alphabetize. Check that data passed to function is correct.')
    return listOfCarNames


# Function will go through the newly created dictionary return a dictionary of all the cars names and year introduced.
# function will do the following:
#1.	take a dictionary as argument. Must have a key value with name of the car. The value must be a dictionary. 
#       return from makeDictionaryOfCars() is value format for the argument.
#2. for each pair of key:value in the argument dictionary, take the name's value and year introduced's value out and save it in another dictionary
#3. returns this new dictionary
def getCarInfo(dictionaryOfCars):
    dictOfCarInfo = {}

    # checks if dictionary has at least one element
    if dictionaryOfCars:
        try:
            for name, carInfo in dictionaryOfCars.items():
                try:
                    # get name from dictionary 
                    newDict  = {name : {'name' : carInfo['name'], 'year introduced' : carInfo['year introduced']}}
                    dictOfCarInfo.update(newDict)
                except:
                    print("Unable to get 'name' and/or 'year introduced' from element")

        except:
            print('Error when trying to get car info. Check that data passed to function is correct.')
    
    return dictOfCarInfo

# print results fron function  alphabetize(), each on their own line.
listOfCars = [ka, fiesta, focus, mondeo, fusion, taurus, fiesta_ST, focus_RS, mustang, gt]
alphabetizedCarList = alphabetize(makeDictionaryOfCars(listOfCars))
for car in alphabetizedCarList:
    print(car)

# print results fron function getCarInfo() in the format: year : name. Sort by year introduced.
listOfCars = [ka, fiesta, focus, mondeo, fusion, taurus, fiesta_ST, focus_RS, mustang, gt]
dictOfCarInfo = getCarInfo(makeDictionaryOfCars(listOfCars))
# sort the dictionary by year introduced
sortedDict = dict(sorted(dictOfCarInfo.items(), key=lambda x: x[1]['year introduced']))     #the key=lambda is code from Stack Overflow and ChatGPT
for car in sortedDict.values():
    print(str(car['year introduced']) + ' : ' + car['name'])
