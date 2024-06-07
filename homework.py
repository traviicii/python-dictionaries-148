import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}



def next_id():  # created a function that will return an id I can use to make a new service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Does this information look correct? y/n")
        if correct == 'y': # create ticket
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else: #go back to the top of the while loop (skip to the next iteration)
            clear()
            continue



def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER
Enter the corresponding number for the action you'd like to take:
    1- Open a new service ticket.
    2- Update the status of an existing ticket  to "closed".
    3- Display all tickets.
    4 - Quit
''')
        if ans == '1':
            clear()
            new_ticket() # function to add a new ticket
        elif ans == '2':
            pass # funtion to update an existing ticket
        elif ans == '3':
            clear()
            print(service_tickets) # function to display all tickets
        elif ans == '4':
            print("Thanks for making service tickets n stuff like that. Have a good one!")
            break
        else:
            print("enter the right number you fool")
        
main()