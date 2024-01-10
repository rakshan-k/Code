import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
        "A" : 2,
        "B" : 3,
        "C" : 4,
        "D" : 5
}

symbol_value = {
        "A" : 5,
        "B" : 4,
        "C" : 3,
        "D" : 2
}

def check_winnings(columns,values,lines,bet):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
           symbol_to_check = column[line]
           if symbol != symbol_to_check:
               break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings , winning_lines



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row] , end = " | ")
            else:
                print(column[row], end = "")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter the number of lines.")

    return lines

def get_amount_of_bet():
    while True:
        bet = input("What would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter bet amount between ${MIN_BET} to ${MAX_BET}.")
        else:
            print("Enter a amount for betting.")

    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:

        bet = get_amount_of_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print(f"You do not have sufficient amount to place that bet. Your current balance is ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Your total betting so far is ${total_bet}.")


    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,symbol_value,lines,bet)
    print(f"You won ${winnings}. ")
    print(f"You won on line : ",*winning_lines)

    return winnings - total_bet 


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}.")
        answer = input("Press enter to play again.(q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with &{balance}")

    
main()
