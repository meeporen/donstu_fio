price_one = input()

price_two = input()

price_free = input()

price_four = input()

price_five = input()

price = int(price_one)+int(price_two)+int(price_free)+int(price_four)+int(price_five)

tax = price*7/100

result_price = price+tax

print (price,tax,result_price)