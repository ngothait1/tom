list = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]
string = "16|11|20|-2|9|19|7|5|10|5|20|-9|16|7|4|2|-5|2|-3|10"

def addItem(my_list,item):
    last_item = str(item[:])
    print( my_list + [last_item])
   
def sort(my_list):
    sorted_number = sorted(my_list)
    print(sorted_number)
    list_down = sorted(my_list,reverse = True)
    print(list_down)

def maxNumber(my_list):
    max_number = max(my_list)
    print(max_number)

def minNumber(my_list):
    min_number = min(my_list)
    print(min_number)

def printTop5Max(my_list):
    print_Top5_Max = sorted(my_list,reverse = True)
    print(print_Top5_Max[0:5])

def sortedNumberNew(my_list):
    text = my_list.split("|")
    sorted_number = sorted(text)
    print(sorted_number)

addItem(list,'nadav')
sort(list)
maxNumber(list)
minNumber(list)
printTop5Max(list)
sortedNumberNew(string)
