# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line

# Ask user for his/her/it's name
name = input("What's your name?")
# Ask user for his/her/it's age
age = int(input("How old are you"))


years_until_retirement_age = 69 - age  # Calculate the years until retirement

"""Create a messsage whit the users name 
and years until retirement"""
message = f"Hi {name}! You can enyoy your retirement in {years_until_retirement_age} years."

""" Print the message 
to the console """
print(message)
