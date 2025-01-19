import time     
print("Hello , this is my final project")
user_name = input("whats is your name?: ") #name
print("Hi" +" " + user_name + " " + "nice to meet you")
print("This is a special calculator, I would need two numbers from you")
number_1 = int(input("first number: ")) #num 1
number_2 = int(input("second number: "))# num 2 
print("Thank you for putting in your numbers" +" "+ str(number_1) +" " + "and" + " "+ str(number_2) )
number_1_status = "odd"
number_2_status = "odd"
if number_1 % 2 ==0 : 
       number_1_status = "even"
print("I can see that the first number is" +" "+ number_1_status )
if number_2 % 2 ==0 : 
       number_2_status = "even"

print("And the second number is" +" "+ number_2_status )

if (number_1 + number_2) % 2 != 0 :
                print("So one of them is even, and one is odd")
else:
        if (number_1 % 2)== 0 and (number_2 % 2) == 0  :
                status_numbers = "even"
        else:
                status_numbers = "odd"     
        print("So both of them are" + " " + status_numbers )
selection = str(input("operator (+ , -, *, /): "))
if selection == "+" :
         result=number_1 + number_2 
         mark="+"      
elif selection == "-": 
         mark="-"
         result=number_1 - number_2
elif selection == "*" :
         mark="*"
         result=number_1 * number_2
elif selection == "/" :
        mark = "/"
        division_choose= input("You chose division, should the result be integer? (y/n): ")
        if number_2 == 0 : 
                print("Eror, cant dvided by zero")
        elif division_choose == "y" : 
                result = number_1 // number_2 
        elif division_choose == "n":  
                result= number_1 / number_2                 
if number_2 !=0 :
        print(str(number_1) + " " + str(mark) + " " + str(number_2) + " " + "=" + " " + str(result))
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print("Thank you" +" " + str(user_name) +" " + "for using the calculator on" + " " +  time_string)