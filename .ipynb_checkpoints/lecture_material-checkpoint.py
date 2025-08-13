#print("hello world")
# comments
#ex_var_int = 5
#ex_var_float = 0.33
#ex_var_bool = False
#3print("ex_var_int ", ex_var_int)
#print("ex_var_float ", ex_var_float)
#print("ex_var_bool ", ex_var_bool)

#ex_var_int = 7
#print("ex_var_int ", ex_var_int)

#addition = 4 + 5 # 9
#print("addition ", addition)
#subtraction = 4 - 5 # -1
#print("subtraction ", subtraction)
#division = 4 / 4 # 1
#print("division ", division)
#multiplication = 4 * 4 # 16
#print("multiplication ", multiplication)

#exponentiation = 4**2 # 16
#print("exponentiation ", exponentiation)
#floor_division = 4 // 2 # 2
#print("floor_division ", floor_division)
#modulo = 11 % 3 # 0
#print("modulo ", modulo)

#add_assign = 5
#print("add_assign ", add_assign)
#add_assign += 7
#print("add_assign ", add_assign)

#exercise = 15 / 3 * 2 * 2 - ( 3 + 4 )
#print("exercise ", exercise)

#number = 5
#number **= 3
#print("number ", number)

#ex_round = round(1.23 + 2.80, 2)
#print("ex_round ", ex_round)

#a = 10.9
#b = 211.05
#dem = 10
#summed = a * dem + b * dem
#print("summed ", summed/dem)

#dem = 1
#penne = 16.68 * dem
#arrabiata = 6.98 * dem
#garlic = 16.78 * dem
#seasoning = 15.26 * dem
#bagguettes = 3 * dem
#meatballs = 4.39 * dem
#subtotal = penne + arrabiata + garlic + seasoning + bagguettes + meatballs
#subtotal = subtotal / dem
#subtotal = round(subtotal, 2)
#print("subtotal ", subtotal)

#ex_string = "orange"
#print("index 2 of ex_string ", ex_string[2])
#print("first 3 letters ", ex_string[:3])
#print("letters between 2nd and 5th position ", ex_string[2:5])
#print("letters after 4th position" , ex_string[4:])

#ex_string_2 = ex_string + " - "
#print("ex_string_2 " + ex_string_2)

#ex_str_3 = "Just do it!"
#print(" print ! from str-" + ex_str_3[10]),
#print(" print do from str-" + ex_str_3[5:7])
#print(" print it! from str-" + ex_str_3[8:])
#print(" print Just from str-" + ex_str_3[:4])

#ex_str_4 = "Dont " + ex_str_3[5:]
#print("ex_str_4 " + ex_str_4)

#ex_1 = False
#ex_2 = 29
#ex_3 = 4.1352
#print("type ex_1 ", type(ex_1))
#print("type ex_2 ", type(ex_2))
#print("type ex_3 ", type(ex_3))

#ex_4 = str(ex_1)
#ex_5 = str(ex_2)
#ex_6 = str(ex_3)
#print("type ex_4 ", type(ex_4))
#print("type ex_5 ", type(ex_5))
#print("type ex_6 ", type(ex_6))

#print("This\tis\tan\texample\tof\ttabs")
#print("This\nis\nan\nexample\nof\nenter")
#print("This is an example of quotes: " + "\" Do or do not. There is no try.\"")
#print("This is an example of quotes: " + '"When I Said \'immediately, \' I meant today!" said King Saul.')

#print("*******\n ****\n  ***\n   *")

#name = input("What is your name? ")
#quest = input("What is your quest? ")
#favourite_color = input("What is your favourite color? ")
#print("So your name is " + name + ", your quest is " + quest + ", and your favourite color is " + favourite_color + ".")

#age = int(input("What is your age? "))
#print("You have " + str(age) + " years old")
#print(type(age))

#def prints_four() :
#    print("this")
#    print("is")
#    print("an")
#    print("example")
#
#prints_four()
#prints_four()

#def function_one_param(parameter):
#    print("parameter: " + str(parameter) + " with type: " + str(type(parameter)))

#function_one_param("test")
#function_one_param(2)
#function_one_param(3.3)
#function_one_param(True)

#def default_example(num1=8, num2=7) :
#    print(num1 * num2)

#default_example()
#default_example(2)
#default_example(3, 3)

#def default_return_example(num1=8, num2=7) :
#    return num1 * num2

#product = default_return_example()
#print(product)

#from random import randint

#fuel = randint(10, 25)
#miles = randint(200, 400)
#
#print("the car can travel " + str(miles // fuel) + " miles per gallon.")
#print("the car's fuel tank can hold " + str(fuel) + " gallons.")
#print("the car can travel " + str(miles) + " miles on a full tank.")

#veg = input("Type the name of a vegetable.")
#color = input("Type the color of a vegetable.")
#if veg == "corn" :
#    if color == "red" :
#        print("The vegetable is a red corn.")
#    else :
#        print("The color is not red. Is " + color + ".")
#elif veg == "tomato" :
#    print("The vegetable is a tomato.")
#else :
#    print("The vegetable is not corn.")

#var_loop = 10
#
#while var_loop > 0 :
#    #print(var_loop)
#    var_loop -= 1
#
#var_input = int(3)#input("enter a number: "))
#var_i = var_input
#var_temp = 0
#while var_i > 0 :
#    var_temp += var_i
#    var_i -= 1

#print("input was " + str(var_input))
#print("the sum is " + str(var_temp))

#word = "hello world"
#for letter in word :
    #print(letter)

#input_str = input("Enter a String.")
#str_len = 0

#for letter in input_str :
#    str_len += 1

#print(input_str)
#print(str_len)

#one_input = range(5) #Range start at 0 until 5 (non-inclusive) (1 argument)
#for num in one_input :
#    print(num)
#
#two_inputs = range(5, 10) #Range start at 5 and ends at 10 (non-inclusive) (2 arguments)
#for num in two_inputs :
#    print(num)
#
#three_inputs = range(1, 20, 3) #Range start at 1 and ends at 20 (non-inclusive) with steps at 3 (3 arguments)
#for num in three_inputs :
#    print(num)

#for num in range(1, 51)  :
#    if num % 3 == 0 and num % 5 == 0 :
#        print("FizzBuzz")
#    elif num % 3 == 0 :
#        print("Fizz")
#    elif num % 5 == 0 :
#     print("Buzz")
#    else :
#        print(num)

#def factorial (fac_num) :
#    returned = 1
#    for num in range(fac_num, 1, -1) :
#        #print(str(returned), " = ", str(returned), "*", str(num))
#        returned *= num
#    return returned

#print("Factorial of " + str(3) + " is ", factorial(3))
#print("Factorial of " + str(4) + " is ", factorial(4))
#print("Factorial of " + str(5) + " is ", factorial(5))

#string_exemple = "This Is A String To Test."
#print(string_exemple.upper())
#print(string_exemple.lower())
#print(string_exemple.title())
#print(string_exemple.upper().isupper())
#print(string_exemple.upper().islower())
#print(string_exemple.istitle())
#print(string_exemple.startswith("T"))
#print(string_exemple.endswith("Test."))

#word = "abcde"
#for item in enumerate(word):
#    print(item)
#
#for index, item in enumerate(word):
#    print(index, " - ", item)
#
#for item in word:
#    print(item)

#mylist1 = [1,2,3]
#mylist2 = ["a", "b", "c"]
#for item in zip(mylist1, mylist2) :
#    print(item)
#
#mylist3 = list(zip(mylist1, mylist2))
#print(mylist3)

#print("-".join(["one", "two", "three"]))
#string_exemple = "One, Two, Three"
#print(string_exemple.split(",")) #Create a list of the string separated by the char
#
#string_exemple = "__Hello_World__"
#print("|" + string_exemple.rjust(20, "*")+ "|") #Add char at right until string has 20 of length
#print("|" + string_exemple.ljust(20, "*")+ "|") #Add char at left until string has 20 of length
#print("|" + string_exemple.center(20, "*")+ "|") #Add char at center until string has 20 of length
#print("|" + string_exemple.strip("_")+ "|") #Remove all chars that match from left and right
#print("|" + string_exemple.rstrip("_")+ "|") #Remove all chars that match from right
#print("|" + string_exemple.lstrip("_")+ "|") #Remove all chars that match from left
#
#print(string_exemple.replace("World", "People"))
#print(len(string_exemple))
#
#reverse_str = ""
#for char in range(len(string_exemple) - 1 , -1, -1) :
#    #print("[" + str(char) + "] - [" + string_exemple[char] + "]")
#    reverse_str += string_exemple[char]
#    #print("reverse_str: {" + reverse_str + "}")
#
#print("reverse_str: |" + reverse_str + "|")

#def word_counter (words) :
#    spaces_and_letters = ""
#    word_count = 1
#
#    for i in words :
#        #print("i: {" + str(i) + "}")
#        if i.isalnum() or i.isspace() or i == "-" or i == "'" :
#            spaces_and_letters += i
#
#    #print("end first for")
#
#    for j in spaces_and_letters :
#        #print("j: {" + str(j) + "}")
#        if j == " " :
#            word_count += 1
#    return word_count
#
#    #return len(param.split(" "))
#
#print(word_counter("James Bond is 007."))
#print(word_counter("When the moon hits your eye like a big pizza pie, that's amore!"))
#print(word_counter("Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
#saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
#shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
#shrimp burger, shrimp sandwich. That- that's about it."))

#name = "Mónica"
#degree = "IT"
#job = "Scrum Master"
#experience = 10
#
#print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))

#example_list_1 = [5, 4, 3, 2, 1, 8, 9]
#example_list_2 = [2.78, 9.31]
#example_list_3 = ["blue", "green", "Red", "Yellow", "Purple", "Orange", "Brown"]
#example_list_4 = [True, False, False, True, False, True, True, False, True]
#example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#example_list_6 = [10, 3.14159, "string", False, [1, 2, 3]]
#
#print(list("blah"))
#print(3 in example_list_1)
#print(8 not in example_list_1)
#
#print("string" in example_list_6)
#print("world" not in example_list_6)
#
#print(example_list_3[0]) #Access item at index 0
#print(example_list_5[2][1]) #Access item at index 2 and position 1
#print(example_list_3[2][0]) ##Access item at index 2 and position 0
#print(example_list_3[-1]) #Access item at last position of list (access from unversed order)
#
#print(example_list_3[:4]) #Get a list with the last 4 items of the original list
#print(example_list_3[3:5]) #Get a list with the items between 3 and 5 (non-inclusive) index of the original list
#print(example_list_3[3:]) #Get a list with the first 3 items of the original list
#
#print(example_list_3[2])
#example_list_3[2] = "black" #assign a new value at index 2 of the list
#print(example_list_3[2])
#example_list_3[0 : 1] = ["grey", "white"] #assign a new values from index 0 until 1 of the list
#print(example_list_3)
#
#del example_list_3[2] #Remove item at 2nd index
#print(example_list_3)
#example_list_3.remove("Yellow") #just remove the first item with this value
#print(example_list_3)
#example_list_3.append("magenta") #add magenta at the end of the list
#print(example_list_3)
#example_list_3.insert(2, "cyan") #insert cyan at index 2
#print(example_list_3)
#
#example_list_3.sort() #sort the list this will put the upper case words at the beginning
#print(example_list_3)
#
#example_list_3.sort(reverse=True) #sort the list in the reverse order
#print(example_list_3)
#print(example_list_3.index("Purple")) #get the index of the item Purple
#
#example_list_3.sort(key=str.lower) #sort the list in with the lower case words uin the beginning
#print(example_list_3)
#print(example_list_3.index("Purple"))
#
#last_item = example_list_3.pop() #remove the last item of the list and save it in a variable
#print(example_list_3)
#print(last_item)
#
#second_item = example_list_3.pop(1) #remove the item in the first index and save it in a variable
#print(example_list_3)
#print(second_item)
#
#example_list_1.sort()
#print(example_list_1)
#example_list_1.sort(reverse=True)
#print(example_list_1)
#print()
#
#import copy
#print(example_list_3)
#example_list_7 = copy.deepcopy(example_list_3)
#print(example_list_7)
#example_list_8 = copy.copy(example_list_3)
#print(example_list_8)
#print()
#example_list_3[2] = "pink"
#print(example_list_3)
#print(example_list_7)
#print(example_list_8)
#example_list_9 = [(1,2), (3, 4), (5, 6), (7,8)]
#for item in example_list_9:
#    print(item)
#
#for (a, b) in example_list_9:
#    print(a)
#    print(b)


#Create a dictionary
consoles = {"nintendo" : "wii",
            "microsoft" : "xbox",
            "sony" : "playstation"} #Key : value

#for key, value in consoles.items():
#    print(value)
#
#print(consoles["nintendo"]) #Access by the key
#print(consoles.keys())
#print(consoles.values())
#print(consoles.items())
#print(consoles.get("other", "Item not found"))
#print(consoles.get("microsoft", "Item not found"))
#
#for key, value in consoles.items():
#    print(key, " - ", value)

#ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW") #inside [] the string value will be the key
#print(ex_1)

#ex_2 = {}.fromkeys("ad", "1600 Pennsylvania Avenue NW") #without [] the string value will be split for multiple keys (just distinct values
#print(ex_1)

#microsoft = consoles.pop("microsoft")
#print(consoles)
#print(microsoft)

#ex = consoles.popitem()
#print(consoles)
#print(ex)

#consoles.clear()
#new_consoles = consoles.copy()
#print(new_consoles)
#print(consoles)
#new_consoles["nintendo"] = "switch"
#print(new_consoles)
#print(consoles)

#new_console = {"tetris": "22a"}
#consoles.update(new_console)
#print(consoles)

#consoles.setdefault("tetris", "22a") #add the new key-value if the key does not exist in the dictionary
#print(consoles)

#with_values = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)
#print(with_values)

#tuple_1 = (0, 1, 2, 3, 4, 5, 6, 8, 9)
#list_1 = [0, 1, 2, 3, 4, 5, 6, 8, 9]
#print(tuple_1.__sizeof__())
#print(list_1.__sizeof__())
#print(tuple_1)
#print(tuple_1[2])
#print(tuple_1[:8])
#print(tuple_1[2:7])
#print(tuple_1[3:])

#tuple_2 = (2.718, False, [1, 2, 3])
#print(tuple_2)
#tuple_3 = (1, 1, 0, 0, 0)
#print(tuple_3)

#tuple_4 = tuple([3.14, 2.05, 10])
#tuple_5 = tuple("edcba")
#print(tuple_4)
#print(tuple_5)

#tuple_6 = tuple({"a":1, "b":2, "c":3})
#print(tuple_6)

#for item in tuple_1:
#    print(item)

#count = 0
#while count < len(tuple_1):
#    print(tuple_1[count])
#    count += 1

#count = len(tuple_1) - 1
#while count >= 0:
#    print(tuple_1[count])
#    count -= 1

#print(tuple_1[::3]) #stride length of 3 - start at index 0 and steps of 3
#print(tuple_1[1::2]) #evens only - start at 1 and steps of 2
#print(tuple_1[7::-1]) #backwards from 8 - start at index 7 and -1 steps
#print(tuple_1[8::-2]) #odds only backwards - start at index 8 and odds only

#nested = ( 1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
#print(nested[4]) # item at 4th index of tuple
#print(nested[5][1]) #get the 1st item of the 5th index of tuple

#repeat = (7, 3, 3, 3, 0, 0, 5, 7, 0, 0)
#print(repeat.count(7))
#print(repeat.count(3))
#print(repeat.count(0))
#print(repeat.count(5))
#print(repeat.index(7))
#print(repeat.index(5))

#set_1= {9, 8, 7, 7, 6, 5, 4, 3, 2, 1}
#print(set_1)
#set_2 = set({"a", "a", "b", "c", "d", "e"})
#print(set_2)
#set_3 = set(range(1, 12, 2))
#print(set_3)

#fruits = {"apple", "orange", "banana", "cherry"}
#print(fruits)
#fruits.add("watermelon")
#print(fruits)
#fruits.remove("banana")
#print(fruits)
#fruits.discard("apple")
#print(fruits)
#fruits.clear()
#print(fruits)
#vegetables = {"carrot", "lecture"}
#groceries = fruits.union(vegetables) #or fruits | vegetables
#print(groceries)
#print()
#print(groceries.intersection(vegetables))
#print(groceries & vegetables)
#print()
#print(groceries.difference(vegetables))
#print(groceries - vegetables)

#comp_1 = {even+2 for even in range(2, 11, 2)}
#print(comp_1)

#comp_2 = {char.lower() for char in "ALLCAPS"}
#print(comp_2)

#myfile = open('test.txt')
#print(myfile)
#print(myfile.read())
#print(myfile.read()) #if you read the file 2 times the 2nd time we will not be able to see the content of the file we need to point to the begining again
#myfile.seek(0)
#print(myfile.read())
#myfile.seek(0)
#print(myfile.readlines())
#myfile.seek(0)
#my_new_file = open("C:\\Users\\mlemos\\OneDrive - Capgemini\\Desktop\\Python_Projects\\ExamplePythonProject\\test.txt")
#print(my_new_file.readlines())
#my_new_file.close()
#myfile.close()

#with open("test.txt", mode='r+') as f:
#    f.seek(0)
#    contents = f.read()
#    print(contents)
#    f.write("\nThird Line")
#    f.seek(0)
#    contents = f.read()
#    print(contents)

#from random import shuffle
#mylist = [1, 2, 3, 4, 5,  6, 7, 8, 9]
#print(mylist)
#shuffle(mylist)
#print(mylist)

#def myfunc(*args) :#receives a tuple
#    return sum(args) * 0.05
#
#print(myfunc(3, 4))
#print(myfunc(3, 4, 3))
#
#def myfunc2(**kwargs) : #redceivs a dictionary
#    print(kwargs)
#    if 'fruit' in kwargs:
#        print('My fruit of choise is {}'.format(['fruit']))
#    else:
#        print('I did nbot find any fruit here')
#
#myfunc2(fruit='apple', veggie='lettuce')

def myfunc(str):
    newStr = ""
    for char in str:
        print(str.index(char))
        if str.index(char)%2 == 0:
            newStr += char.upper()
        else:
            newStr += char.lower()

    return newStr

def myfunc2(str):
    newStr = []
    for c in range(len(str)):
        print(c)
        if c % 2 == 0:
            newStr.append(str[c].upper())
        else:
            newStr.append(str[c].lower())

    return "".join(newStr)


print(myfunc("abcdfgqwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjkl"))
print(myfunc2("abcdfgqwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjkl"))