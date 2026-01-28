# def main():
#     x, y = 10, 100
#     if x > y:
#         print(f"{x} is greater than {y}")
#     elif x == y:
#         print(f"{x} is equal to {y}")
#     else:
#         print(f"{x} is less than {y}")




from operator import index


def add(a: int, b: int):
    return a + b


def compare(a: int, b: int):
    if a > b:
        return f"{a} is greater than {b}"
    elif a == b:
        return f"{a} is equal to {b}"
    else:
        return f"{a} is less than {b}"


def max_of_two(a: int, b: int):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a 

def add_numbers(a, b):
    return a + b  

def multi_add(*args):
    return sum(args)

def printwithwhile(limit):
    i = 0
    while i < limit:
        print(i)
        i += 1

def print_with_for(limit):
    for i in range(limit):
        print(i)

def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "mango"]

def find_number(numbers, target):
    for num in numbers:
        if num == target:
            print("Found ", target)
            break   
        print("Check", num)

nums = [2, 4, 6, 8, 10]

def print_even(numbers):
    for num in numbers:
        if num % 2 != 0:
            continue 
        print(num)

nums = [1, 2, 3, 4, 5, 6]

def print_with_index(items):
    for index, value in enumerate(items):
        print("Index:", index, "Value:", value)

names = ["Chandan", "Rahul", "Amit"]


def fubnonacii_main():
    a, b = 0, 1
    n = int(input("Enter the number of terms: ")) 
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
  
def fubonacii_iterative():
    n=int(input("Enter the number of terms: "))
    def fibonacci(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)
    for i in range(n):
        print(fibonacci(i), end=' ')

def swapCase():
    n=input("enter string: ")
    for char in n:
        if char.islower():
            print(char.upper(),end='')
        else:
            print(char.lower(),end='')
    # if n.islower():
    #     print(n.upper())
    # else:
    #     print(n.lower())    
    
def split_and_join():
    with open(r"C:\Users\chand\OneDrive\Desktop\platform\PEPCLASS\file.txt", "r") as file:
        s = file.read().strip()

    words = s.split(" ")
    print(words)
    words = list(filter(None, words))
    print("-".join(words))
def listoffriends():
    friends = ["A", "B", "C", "Dd"]
    # for friend in friends:
    #     print(friends.index(friend),friend)
    # print(len(friends))
    for index,friend in enumerate(friends):
        print(friend,index)
    print(len(friends))

def dictionaydata():
    student={"ram":23,"shyam":24,"hari":22}
    students={"name":["ram","shyam","hari"],"age":[23,24,22]}
    for item in student.items():
        print(item)
    for age in student.values():
        print(age)
    for name in student.keys():
        print(name)
    

def title_upper_find():
    s="hello world"
    print(s.title())
    print(s.upper())
    print(s.find("o"))

def greeting():
    date = input("Enter date (DD-MM): ")
    time_date = int(input("Enter time in 24 hour format (0-23): "))

    # Check New Year first
    if date == "01-01" or date == "1-1" or date=="01/01" or date=="1/1":
        print("🎉 Happy New Year!")
   
    elif time_date < 12:
        print("Good Morning")
    elif 12 <= time_date < 18:
        print("Good Afternoon")
    else:
        print("Good Evening")

def listappend():
    my_list=['ram','shyam']
    for i in range(5):
        my_list.append(i*i)
    print(my_list)
    print(my_list.index('shyam'))
    print(my_list.index(1))
    print(my_list.index(1)=='hello')
    # == to check value
    idx = my_list.index('shyam')
    my_list[idx] = 'hello'
    print(my_list)

def main():
    # x, y = 10, 100
    # print(compare(x, y))
    # print(f"add({x}, {y}) = {add(x, y)}")
    # print(f"max_of_two({x}, {y}) = {max_of_two(x, y)}")
    # print(add_numbers(x, y))
    # print(multi_add(x, y, 50, 25))]
    # printwithwhile(5)
    # print_with_for(5)
    # print_fruits(my_fruits) 
    # find_number(nums, 6)
    # print_even(nums)
    # print_with_index(names)
    # print(fubnonacii_main())
    # print(fubonacii_iterative())
    # swapCase()
    # print()
    # split_and_join()
    # listoffriends()
    # dictionaydata()
    # title_upper_find()
    # greeting()
    listappend()

if __name__ == "__main__":
    main()




