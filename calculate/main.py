# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli_price = 2
leek_price = 2
potato_price = 3
brussel_sprout_price = 7

sum_one_each = broccoli_price + leek_price + potato_price + brussel_sprout_price

num_items = 4
avg_price = sum_one_each / num_items

num_broccolis = 5
num_leeks = 2
num_potatoes = 7
num_brussel_sprouts = 10

sum_total = (broccoli_price * num_broccolis) + (leek_price * num_leeks) + \
    (potato_price * num_potatoes) + (brussel_sprout_price * num_brussel_sprouts)

discount_percentage = 0.3

discounted_sum_total = sum_total * (1 - discount_percentage)
print(round(discounted_sum_total, 2))
