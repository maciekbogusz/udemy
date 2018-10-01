numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number%2 == 0:
            evens.append(number)
    return evens
even_numbers = even_numbers()
#print(even_numbers)

# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code

def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"

choice = input("Please enter: ")
output = user_menu(choice)
#print(output)

