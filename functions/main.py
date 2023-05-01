# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return f'Hello, {name}!'

def add(a, b, c):
    return a + b + c

def positive(number):
    return number > 0

def negative(number):
    return number < 0

# greet function
print(greet('Bob')) # Hello, Bob!

# add function
print(add(5,3,2)) # 10

# positive function
print(positive(50)) # True
print(positive(-50)) # False
print(positive(0)) # False

# negative function
print(negative(50)) # False
print(negative(-50)) # True
print(negative(0)) # False