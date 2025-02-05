def doubleNumbers(my_list): # each number multiply by 2 
    for index, value in enumerate(my_list):
         my_list[index]= int(my_list[index]*2)

def stringListToIntegerList(strList): # convert string to int 
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def listOf50(): # put numbers and saves as a list 
    numbers = []
    for i in range(50):        
        numbers_list = input("write only numbers or write stop: ")
        if numbers_list == "stop":
            break
        else: 
            numbers.append(numbers_list)
    return numbers

def printCharAndIndex(my_list): # printing index and value 
    for index, value in enumerate (my_list):
        print("on index " + str(index) + " the number is " + str(value))

for i in range(0,1001): # print from 1-1000
    print(i) 

my_list= [4, 1, 4, 2, 6, 8, 200] 
printCharAndIndex(my_list)

double_list = [0, 274, 66, 305.5]
doubleNumbers(double_list)
print(double_list)

numbers_50 = listOf50() 
stringListToIntegerList(numbers_50)
print(numbers_50)

# I couldn't find a way "to not" put other strings than "stop" and it will write error . 
