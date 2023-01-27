space = 20 * ' '
print(space, 'Welcome to Treasure Island.\n', space[:19], 'Your mission is to find the treasure.')
choice01 = input('Left or Right? ').title()
if (choice01 == 'Right'):
    print(space, 'Game Over!')
else:
    print(space,'Welcome to Level 2!')
    choice02 = input('Swim or Wait? ').title()
    if choice02 == 'Swim':
        print(space, 'Game Over!')
    else:
        print(space,'Welcome to Level 3!')
        print(space,'Which door?')
        choice03 = input("Red, Blue or Yellow? ").title()
        if choice03 == ('Red' or 'Blue'):
            print(space,'Game Over!')
        else:
            print(space,'You Win!')

