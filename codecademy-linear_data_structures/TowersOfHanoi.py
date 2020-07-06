from stack2 import *

# Create the stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = [left_stack, middle_stack, right_stack]
    
# Set up the game
print("Let's play Towers of Hanoi!!")
num_disks = int(input("\nHow many disks do you want to play with?\n").strip())
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for num_disk in range(num_disks, 0, -1):
    left_stack.push(num_disk)

num_optimal_moves = 2**num_disks - 1
print("\nThefastes you can solve this game is in {} moves.".format(
    num_optimal_moves
))

#Get User Input
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        # Print user's command
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {} for {}".format(
                letter, name
            ))

        user_input = input().strip()
        if user_input == 'exit':
            break

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]
        else:
            return None

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disk:
    print(
        "\n\n\n...Current Stacks..."
        )
    for stack in stacks:
        stack.print_items()

    while True:
        print(
            "\nWhich stack do you want to move from?\n"
            )
        # dari stack mana
        from_stack = get_input()
        print(
            "\nWhich stack do you want to move to?\n"
        )
        # ke stack mana
        to_stack = get_input()
        if from_stack == None:
            print(
                "\n\nInvalid Move. Try Again"
                )
        """
        unfinished error to_stack
        karena to stack tidak Nonetype object bukan masuk stack object
        lanjut bisa di task 30:
        https://www.codecademy.com/paths/computer-science/tracks/linear-data-structures/modules/cspath-stacks/projects/towers-of-hanoi
        """
        elif to_stack == None or to_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        

print("done ... ")