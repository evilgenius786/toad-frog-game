import os


def menu():
    return input("""Lilypad game
------------
D) Demonstration
P) Play game
R) Reset
E) Exit Game

Please enter your option: """).upper()


def demonstrate():
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Demonstration ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AIM OF THE GAME: Switch positions of the frogs(F) and toads(T) as shows-
['F','F','F','','T','T','T'] to ['T','T','T','','F','F','F']

To move enter a FROM and TO position for each move-
For example from starting position ['F','F','F','','T','T','T']-
FROM: 3
TO: 4
Gives ['F','F','','F','T','T','T']

RULES:
1) Frogs can only move to the right and toads can only move to the left
2) The frog or toad can move one place into an empty space or jump over
one another frog or toad to move into an empty space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")


def play():
    global count, to
    count = 0
    while True:
        win = True
        for i in range(3):
            if lilypad[i] != 'T':
                win = False
        if win:
            for i in range(4,6):
                if lilypad[i] != 'F':
                    win = False
        if win:
            return input(f"Congratulations! You have won the game in {count} moves.")
        print()
        print("Position ", end='')
        print(position)
        print("Lilypad  ", end='')
        print(lilypad)
        print("Enter R -> Reset, E -> Exit Game, or your choice in the FROM position")
        f = input("FROM: ")
        if f.upper() == 'E':
            exit()
        elif f.upper() == 'R':
            print("Resetting the game...")
            count = 0
            reset()
            continue
        try:
            to = int(input("TO: ")) - 1
            f = int(f) - 1
        except:
            print("Invalid entry! Please enter again")
            continue
        if f < 0 or f > 6 or to < 0 or to > 6:
            print("Invalid entry!")
        elif abs(f - to) > 2:
            print("Error, you can't take more than 2 steps.")
        elif lilypad[f] == ' ':
            print("You can't move empty space!")
        elif lilypad[to] != ' ':
            print("You can only move to an empty space!")
        elif f == to:
            print("FROM and TO can't be same.")
        elif frog == 0:
            if lilypad[f] == 'F':
                if f > to:
                    print("Frog can't move left")
                if f < to:
                    lilypad[f], lilypad[to] = lilypad[to], lilypad[f]
                    count += 1
            if lilypad[f] == 'T':
                if f < to:
                    print("Toad can't move right")
                if f > to:
                    lilypad[f], lilypad[to] = lilypad[to], lilypad[f]
                    count += 1
        elif frog == 1:
            if lilypad[f] == 'T':
                if f > to:
                    print("Toad can't move left")
                if f < to:
                    lilypad[f], lilypad[to] = lilypad[to], lilypad[f]
                    count += 1
            if lilypad[f] == 'F':
                if f < to:
                    print("Frog can't move right")
                if f > to:
                    lilypad[f], lilypad[to] = lilypad[to], lilypad[f]
                    count += 1


def reset():
    global frog
    frog = 0  # FROG (left) = 0 , FROG (right) = 1
    global position
    position = ['1', '2', '3', '4', '5', '6', '7']
    global lilypad
    lilypad = ['F', 'F', 'F', ' ', 'T', 'T', 'T']
    count = 0


reset()
option = ''
while True:
    os.system('cls')
    option = menu()
    os.system('cls')
    if option == 'D':
        demonstrate()
    elif option == 'P':
        play()
    elif option == 'R':
        print("Resetting the game...")
        reset()
    elif option == 'E':
        break
    else:
        print("Invalid choice!")
    input("Press any key to continue...")
