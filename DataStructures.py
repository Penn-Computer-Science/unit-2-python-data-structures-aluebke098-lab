
# part 1: lists
def part_1():
    # list of 10 numbers
    list_a = [1,2,3,4,5,6,7,8,9,10]
    # print first, last, middle number
    print(list_a[0])
    print(list_a[-1])
    middle = len(list_a) // 2
    print(list_a[middle])
    print("")
    # add new number to end
    list_a.append(42)
    # replace 3rd number with 99
    list_a[2] = 99
    # loop through and only print even numbers
    for i in list_a:
        if i % 2 == 0:
            print(i)
    print("")

# part 2: dictionaries
def part_2():
    # dict of 5 countries with capitals
    dictionary_a = {"United States of America":"Washington, DC", 
                    "Japan":"Tokyo", "Mexico":"Mexico City",
                    "Italy":"Rome", "India":"New Delhi"}
    # print capital of 2 countries
    print(dictionary_a["Mexico"])
    print(dictionary_a["Italy"])
    print("")
    # add new pair
    dictionary_a["Egypt"] = "Cairo"
    # change the capital of one country
    dictionary_a["United States of America"] = "New York City"
    # loop through and print everything 
    for key,value in dictionary_a.items():
        print(f"{value} is the capital of {key}.")
    print("")

# part 3: sets
def part_3():
    # create a set of favorite fruits
    set_a = {"pineapple", "apples", "mango", "cherries"}
    # add a fruit, remove a fruit
    set_a.add("bananas")
    set_a.remove("mango")
    # create a set of fruit a friend likes
    set_b = {"apples", "pomegranate", "stawberries", "raspberries"}
    # print:
        # fruits both like
    print(set_a.intersection(set_b))
        # fruits only I like
    print(set_a.difference(set_b))
        # all fruits either like
    print(set_a.union(set_b))
    print("")

# part 4: tuples
def part_4():
    # create tuple of 5 colors
    tuple_a = ("red", "orange", "yellow", "green", "blue")
    # print first and last color
    print(tuple_a[0])
    print(tuple_a[-1])
    print("")
    # loop through + print each color
    for i in tuple_a:
       print(i)
    print("")
    # try to change color (note error)
    try:
       tuple_a[0] = "pink"
    except:
       print("\'tuple\' object does not support item assignment")
       print("")

# part selection
num = int(input("Input the number you wish to view.\n"))
print("")
if num == 1:
  part_1()
elif num == 2:
  part_2()
elif num == 3:
  part_3()
elif num == 4:
  part_4()
