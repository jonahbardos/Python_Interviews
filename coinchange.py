""" 
Coin Change Interview Question

33 cents == 1 Quarter, 1 Nickel, 3 Pennies
"""


def num_coins(cents):
    COINS = {
        'Quarter': [25, 0],
        'Dime': [10, 0],
        'Nickel': [5, 0],
        'Penny': [1, 0] 
    }

    if cents < 1:
        print('No Change')
        return 0


    while cents != 0:    
        if cents >= COINS['Quarter'][0]:
            cents = cents - COINS['Quarter'][0] # 33 - 25, this will be remainder
            COINS['Quarter'][1] += 1

        elif cents >= COINS['Dime'][0]:
            cents = cents - COINS['Dime'][0]
            COINS['Dime'][1] += 1

        elif cents >= COINS['Nickel'][0]:
            cents = cents - COINS['Nickel'][0]
            COINS['Nickel'][1] += 1

        elif cents >= COINS['Penny'][0]:
            cents = cents - COINS['Penny'][0]
            COINS['Penny'][1] += 1

    stringShow = ''
    for coin, value in COINS.items():
        if value[1] > 1:
            stringShow += str(value[1]) + ' ' + coin + 's' + ' '
        elif value[1] == 1: 
            stringShow += str(value[1]) + ' ' + coin + ' '
    print(stringShow)
    return

num_coins(0)

