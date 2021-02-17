import sys
import csv
debug = False
seperator = "\n" #How results are seperated. E.g new line, or space etc

if not debug:
    fileName = sys.argv[1]
    if ".csv" not in fileName:
        fileName += ".csv"
else:
    fileName = "test.csv"

#Open and read CSV in to array of fruits

fruits = [] #Format = [(fruit, days, char1, char2)..x]
with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            fruits.append((row[0], row[1], row[2], row[3]))
        line_count += 1


#Process data
fruitsByType = [] #Format: [[fruitName, totalInBasket, [characteristics]] ..x]
for fruit in fruits:
    found = False
    for x in range(0, len(fruitsByType)):
        if fruitsByType[x][0] == fruit[0]: #If fruit already in array
            found = True
            fruitsByType[x][1] = fruitsByType[x][1] + 1 #Alter total fruits
            fruitsByType[x][2].append(fruit[2]) #Append characteristics
            fruitsByType[x][2].append(fruit[3])

    if not found:
        fruitsByType.append([fruit[0], 1, [fruit[2], fruit[3]]])

#Sort in descending order
fruitsByType = sorted(fruitsByType, key=lambda x: x[1], reverse=True)

returned = ""
returned += "Total Fruits: " + str(len(fruits)) + seperator
returned += "Total Types of Fruits: " + str(len(fruitsByType)) + seperator
returned += "Fruit Types: "
for fruit in fruitsByType:
    name = fruit[0]
    amount = fruit[1]
    returned += name + " (" + str(amount) + "), "
returned = returned[:-1] + seperator

returned += "Fruit Characteristics: "
for fruit in fruitsByType:
    name = fruit[0]
    rawCharacteristics = fruit[2]
    for x in range(0, len(rawCharacteristics)):
        rawCharacteristics[x] = rawCharacteristics[x].replace(" ", "")
    characteristics = list(dict.fromkeys(rawCharacteristics))
    returned += name + ": ("
    for characteristic in characteristics:
        returned += characteristic + ", "
    returned = returned[:-2] + "), "
returned = returned[:-2] + seperator

returned += "In basket over 3 days: "
overLimit = [] #Format [fruit1, fruit2,...x]
for fruit in fruits:
    name = fruit[0]
    timeInBasket = fruit[1]

    if int(timeInBasket) > 3:
        overLimit.append(fruit)

fruitsOverLimit = []
for fruit in overLimit:
    name = fruit[0]
    found = False
    for x in range(0, len(fruitsOverLimit)):
        if name == fruitsOverLimit[x][0]:
            found = True
    if not found:
        fruitsOverLimit.append(fruit)


for fruit in fruitsOverLimit:
    returned += fruit[0]
    count = 0
    for item in overLimit:
        if fruit[0] == item[0]:
            count += 1
    returned += " (" + str(count) + "), "
returned = returned[:-2]

print(returned)
