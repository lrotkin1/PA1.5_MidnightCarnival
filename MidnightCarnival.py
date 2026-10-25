#Leah Rotkin
#Midnight Carnival

#challenge 5

'''These are my fist 3 accumulators. The first is to calculate the total amount of visitors, the second to track total admission revenue, and the last to track total ticket revenue.'''

tot_visitors = 0
tot_admission_revenue = 0
tot_tickets = 0

name = input("What is your name?(or enter 'done' to finish): ").strip().lower()

'''This is the start of my main loop that controls the repeat of visitor experience.'''

while name != 'done':


#Challenge 1

    try:
        age = int(input("How old are you?: "))
    except ValueError as e:
        print(f"{e}")
    vip = input("Do you have a VIP pass (yes/no)?: ").strip().lower()

    '''Boolean logic that controls who gets to enter the carnival and how much they pay.'''

    if age < 8 and vip !="yes":
        print("You must be accompanied by an adult.")
    elif 8 <= age <= 17 and vip !="yes":
        print("Welcome! Price is $5 a ticket.")
    elif age >=18 and vip !="yes":
        print("Welcome! Price is $10 a ticket.")
    if vip == "yes":
        print("Welcome VIP member! You may enter free of charge.")

    tot_visitors += 1

    if age < 8 and vip == "no":
        print("Sorry you may not enter the carnival")
        tot_visitors -= 1
        point = 0
        break

    if 8 <= age <= 17 and vip == "no":
        tot_admission_revenue += 5
    elif age >=18 and vip == "no":
        tot_admission_revenue += 10



#Challenge 2

    '''A while loop that uses try and except to ask the user how many tickets they would like to buy and the        price.'''

    while True:
        try:
            tickets = int(input("How many tickets would you like to purchase (1-20)?: "))
            if tickets < 1 or tickets > 20:
                raise ValueError("You must enter a whole number between 1 and 20")
        except ValueError as e:
            print(f"{e}")
            continue
        else:
            if 1<= tickets <= 20:
                print(f"Accepted: {tickets}")
                print(f"price $: {tickets*2}")
            break


    tot_tickets += tickets*2


#Challenge 3

    plays = int(input(f"How many plays? (You may play up to {tickets} times): "))
    point = 0

    '''A for loop that controls the game using the range of the plays the user entered.'''

    for i in range(plays):
        guess = input("Guess a number between 1 and 5: ")
        guess = int(guess)
        if guess == 1 or guess == 2 or guess == 4 or guess == 5:
            print(f"You won 2 points!!")
            point += 2
        elif guess == 3:
            print("You won!! You earned 10 points!")
            point += 10
        else:
            if guess < 1 or guess > 5:
                print("Out of range, no points won.")

    print(f"Total Prize Points Won: {point}")


#Challenge 4

    row = 0
    col = 0

    print("Magic Board!")

    '''While loop with logic printing the magic board.'''

    while col < 5:
        while row < 5:
            if row == 0:
                print("* _  _  _ *")
                print()
            elif row == 1:
                print("_ * _  * _")
                print()
            elif row == 2:
                print("_  _ * _  _")
                print()
            elif row == 3:
                print("_ * _  * _")
                print()
            elif row == 4:
                print("* _  _  _ *")
                print()
            row += 1
        col += 1

    print("Total number of positions examined by inner loop is 5 positions each loop; totaling 25 positions.")

    name = input("What is your name?(or enter 'done' to finish): ").strip().lower()

'''My original loop is done, and now I listed the total amount of visitors, total admission revenue, total ticket revenue, total prize points awarded, and finally total combined revenue.'''

print(f"Number of visitors admitted: {tot_visitors}")

print(f"Total admission revenue: ${tot_admission_revenue}")

print(f"Total ticket revenue: ${tot_tickets}")

print(f"Total prize points awarded: {point}")

print(f"Combined revenue: ${tot_admission_revenue + tot_tickets}")

#Testing Record
'''
Denied Visitor:
    name = chana
    age = 8
    vip = no
    So this visitor was denied entry, correct results.
VIP Visitor:
    name = shira
    age = 45
    vip = yes
    Visitor enters free of charge.
    Visitor bought 2 tickets (price $4) and one play. Entered the number 2 and won
    two points.
    Visitor was shown the magic board.
    Total visitors, total admission revenue, total ticket revenue, total prize
    points, and total combined revenue were then displayed.
    Correct results
Invalid Ticket Entry:
    name = menucha
    age = 35
    vip = no
    price is then given at $10
    visitor was asked how many tickets they want to buy between 1 - 20. Visitor replied
    90 and was told You must enter a whole number between 1 and 20.
    visitor played 2 games, was shown magic board and was done.
    Total visitors, total admission revenue, total ticket revenue, total prize
    points, and total combined revenue were then displayed.
    Correct results
Nonnumeric Ticket Entry:
    name = zahra
    age = 19
    vip = yes
    Visitor responded 'five' when prompted to buy tickets and received the message
    invalid literal for int() with base 10: 'five', and then reprompted so she bought
    3 tickets and played once.
    Then visitor was shown the magic board.
    Total visitors, total admission revenue, total ticket revenue, total prize
    points, and total combined revenue were then displayed.
    Correct results
Multiple Visitors:
    Visitor 1:
        name = shaindy
        age = 17
        vip = no
        bought 3 tickets and played twice. Won a total of 4 points.
        was shown the magic board.
    Visitor 2:
        name = chaya
        age = 18
        vip = yes
        bought 3 tickets and played once. Won a total of 10 points.
        was shown the magic board.
    Visitor 2:
        name = ahuva
        age = 20
        vip = yes
        bought 20 tickets and played  3 times. Won a total of 14 points.
        was shown the magic board.
        User entered 'done'.
        Total visitors, total admission revenue, total ticket revenue, total prize
        points, and total combined revenue were then displayed.
        Correct results
'''
