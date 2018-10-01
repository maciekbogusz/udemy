# known_peope = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
# 
# if person in known_peope:
#     print("You know {}!".format(person))
# else:
#     print("You don`t know {}!".format(person))
known_people = []    

    
def who_do_you_know():
    exit_command  = 'n'
    while exit_command != "y":
        known_names = input("Who do you know? ")
        known_people.append(known_names)    
        exit_command = input("Do you want to stop?")                
    return known_people

def ask_user(known_persons):
    #Ask user for a name
    # see if their name is in te list of people they knwo
    # print out nthat they know that person
    username = input("Enter a name of someone you know: ")
    for element in known_persons:
        if username == element:
            print("Your name is in the list")
        elif username != element:
            print("You do not know this person")
    
    

known_persons = who_do_you_know()
ask_user(known_persons)

print(known_persons)

