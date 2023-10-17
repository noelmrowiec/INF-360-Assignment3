
#test def makeDictionaryOfCars(listOfDictionaries):

dic1 = {'name' : 'g', 'year' : 2000}
dic2 = {'name' : 'h', 'year' : 1990}
lofDict = [dic1, dic2]

lofInt = [44, 22]
loftring = ['fia', 'sdf']
lofNone = []

#listOfDictionaries = [ka, fiesta, focus, mondeo, fusion, taurus, fiesta_ST, focus_RS, mustang, gt]
#expected_output = {
#    'Ka': {'name': 'Ka', 'year introduced': 1996, 'production of the current model': 2014, 'generation': '3rd', 'vehicle information': "Developed by Ford Brazil as a super mini car"},
#    'Fiesta': {'name': 'Fiesta', 'year introduced': 1976, 'production of the current model': 2017, 'generation': '7th', 'vehicle information': "Ford's long running subcompact line based on global B-car Platform"},
#    'Focus': {'name': 'Focus', 'year introduced': 1998, 'production of the current model': 2018, 'generation': '3rd', 'vehicle information': "Ford's Compact car based on global C-car platform"},
#    'Mondeo': {'name': 'Mondeo', 'year introduced': 1992, 'production of the current model': 2012, 'generation': '2nd', 'vehicle information': 'Mid sized passenger sedan with "One-Ford" design based on CD4 platform'},
#    'Fusion': {'name': 'Fusion', 'year introduced': 2005, 'production of the current model': 2014, 'generation': '5th', 'vehicle information': 'Similar to Mondero'},
#    'Taurus': {'name': 'Taurus', 'year introduced': 1986, 'production of the current model': 2009, 'generation': '6th', 'vehicle information': 'Full sized car based on D3 platform'},
#    'Fiesta ST': {'name': 'Fiesta ST', 'year introduced': 2013, 'production of the current model': 2013, 'generation': '1st', 'vehicle information': "Fiesta's high performance factory tune"},
#    'Focus RS': {'name': 'Focus RS', 'year introduced': 2015, 'production of the current model': 2015, 'generation': '1st', 'vehicle information': 'Special high performance Focus developed by SVT'},
#    'Mustang': {'name': 'Mustang', 'year introduced': 1964, 'production of the current model': 2014, 'generation': '6th', 'vehicle information': "Ford's long running pony/muscle car"},
#    'GT': {'name': 'GT', 'year introduced': 2004, 'production of the current model': 2016, 'generation': '2nd', 'vehicle information': "Ford's limited production super car inspired by the legendary race car GT40"}
#}

#assert makeDictionaryOfCars(listOfDictionaries) == expected_output
#print('first tests passed')
#listOfDictionaries = []
#expected_output = {}
#assert makeDictionaryOfCars(listOfDictionaries) == expected_output

#assert makeDictionaryOfCars(listOfDictionaries) == expected_output
#makeDictionaryOfCars([4,235,3])

#listOfDictionaries = [
#    {'year': 2020, 'color': 'black'},
#    {'nam': 'Toyota Camry', 'year': 2021, 'color': 'white'},
#    {'name': 'Ford Mustang', 'year': 2022, 'color': 'red'}
#]
#expected_output = {
#    'Ford Mustang': {'name': 'Ford Mustang', 'year': 2022, 'color': 'red'}
#}
#assert makeDictionaryOfCars(listOfDictionaries) == expected_output

#dictOfDictionaries = { 
#    'Civic' : {'name': 'Civic', 'year': 2020, 'color': 'black'},
#    'Camry' : {'name': 'Camry', 'year': 2021, 'color': 'white'},
#    'Mustang' : {'name': 'Mustang', 'year': 2022, 'color': 'red'}
#}
#expected_output = ['Camry','Civic', 'Mustang']

#assert alphabetize(dictOfDictionaries) == expected_output

#dictOfDictionaries = { 
#    'Civic' : {'name': 'Civic', 'year': 2020, 'color': 'black'},
#    'camry' : {'name': 'camry', 'year': 2021, 'color': 'white'},
#    'Mustang' : {'name': 'Mustang', 'year': 2022, 'color': 'red'}
#}
#expected_output = ['camry','Civic', 'Mustang']

#assert alphabetize(dictOfDictionaries) == expected_output

#expected_output = ['truck']
#assert alphabetize({'name': {'name' : 'truck'}, 'year' : 2022}) == expected_output

#dictOfDictionaries = { 
#    'Civic' : {'name': 'Zebra', 'year': 2020, 'color': 'black'},
#    'camry' : {'name': 'camry', 'year': 2021, 'color': 'white'},
#    'Mustang' : {'name': 'Mustang', 'year': 2022, 'color': 'red'}
#}
#expected_output = ['camry','Mustang', 'Zebra']

#assert alphabetize(dictOfDictionaries) == expected_output
#assert alphabetize({}) == []
#assert alphabetize([23, 434,44]) == []

#dictionaryOfCars = {
#    'Honda Civic': {'name': 'Honda Civic', 'year introduced': 2020, 'color': 'black'},
#    'Toyota Camry': {'name': 'Toyota Camry', 'year introduced': 2021, 'color': 'white'},
#    'Ford Mustang': {'name': 'Ford Mustang', 'year introduced': 2022, 'color': 'red'}
#}
#expected_output = {
#    'Honda Civic' : {'name': 'Honda Civic', 'year introduced': 2020},
#    'Toyota Camry' : {'name': 'Toyota Camry', 'year introduced': 2021},
#    'Ford Mustang' : {'name': 'Ford Mustang', 'year introduced': 2022}
#}
#assert getCarInfo(dictionaryOfCars) == expected_output
#assert getCarInfo({}) == {}

#dictionaryOfCars = {
#    'Honda Civic': {'nam': 'Honda Civic', 'year introduced': 2020, 'color': 'black'},
#    'Toyota Camry': {'name': 'Toyota Camry', 'year inoduced': 2021, 'color': 'white'},
#    'Ford Mustang': {'name': 'Ford Mustang', 'year introduced': 2022, 'color': 'red'}
#}
#expected_output = {
#    'Ford Mustang' : {'name': 'Ford Mustang', 'year introduced': 2022}}

#assert getCarInfo(dictionaryOfCars) == expected_output
#print("Tests finished")