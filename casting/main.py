# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")

# Part 2
order = 'leek 4'
num_str = order[5:]
num_leeks = int(num_str)
leek_price = 2
sum_total = num_leeks * leek_price
print(sum_total)

# Part 3
broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'

broccoli_weight = float(broccoli_order[8:])
broccoli_total_price = round(broccoli_weight * broccoli_price, 2)

print(f"{broccoli_weight}kg broccoli costs {broccoli_total_price}e")
