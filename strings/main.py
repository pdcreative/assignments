# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# create variables for each player who scored and the minute of the goal
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54


# create a string that reports on who scored when
scorers = player1 + ' ' + str(goal_0) + ', ' + player2 + ' ' + str(goal_1) 
print(scorers)

# create a single string with information about who scored when
report = f"{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"
print(report)

# define the player's name
player = 'Hans van Breukelen'

# isolate the first name
first_name = player[:player.find(' ')]
print(first_name)

# isolate the length of the last name
last_name_len = len(player[player.find(' ')+1:])
print(last_name_len)

# create the short name
last_name = player[player.find(' ')+1:]
name_short = f"{first_name[0]}. {last_name}"
print(name_short)

# create the chant
chant = f"{first_name}! " * len(first_name)
chant = chant.strip()
print(chant)

# check if the chant ends with a space character
good_chant = chant[-1] != ' '
print(good_chant)