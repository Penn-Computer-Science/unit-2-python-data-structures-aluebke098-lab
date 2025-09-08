# part selection
# num = int(input("Input the number you wish to view.\n"))
# print("")
# if num == 1:
#   part_1()
# elif num == 2:
#   part_2()
# elif num == 3:
#   part_3()
# elif num == 4:
#   part_4()

# part 1: lists
def part_1():
    # list of 10 numbers
    list_a = [1,2,3,4,5,6,7,8,9,10]
    # print first, last, middle number
    print(list_a[0])
    print(list_a[-1])
    middle = range(list_a) // 2
    print(list_a[middle])
    # add new number to end
    list_a.append(42)
    # replace 3rd number with 99
    list_a[2] = 99
    # loop through and only print even numbers
    for i in list_a:
        if i % 2 == 0:
            print(i)
