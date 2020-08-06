# FUNCTIONS - instructions to do a certain action

# 2 things required for functions:
# 1) define them
# 2) call them to work

#1) define function
def greeting():
  print("Hello")

#2) call the function to work
greeting()

def goodbye(name):
  print("Goodbye, " + name)

goodbye("Mario")


# Challenge:
# create a function called sandwich
# that will print out "salami"
def sandwich(meat):
  print("I like " + meat + " sandwiches")

sandwich("salami")

def sum(n1, n2):
  return n1 + n2
total = sum(1, 3)
print(total)

def multiply(num):
  print(num * 2)

multiply(total)


# def sum2(n1, n2):
#   print(n1 + n2)

# def add(num):
#   for i in range(5):
#     sum = num + i
#     if sum < 5:
#       print(str(sum) + " is less than 5")
#     else:
#       print(str(sum) + " is equal to or greater than 5")
#   sum2(5,5)

# add(3)

def favBook():
  print("Harry Potter")

favBook()

def favBook2(title):
  print(title)

favBook2("Lord of the Rings")
