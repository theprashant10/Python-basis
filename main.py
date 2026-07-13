import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbols_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings,winnings_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                 print(column[row],end="")
        print()





def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print(" Please enter a number")
    return amount



def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print(" Please enter a number")
    return lines

def get_bet():
    while True:
        lines = input("What would you like to bet on each line? $ ")
        if lines.isdigit():
            lines=int(lines)
            if MIN_BET<= lines <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print(" Please enter a number")
    return lines

def game(amount):
    lines=get_number_of_lines()
    while True:
     bet=get_bet()
     Total_bet=bet*lines
     if Total_bet>amount:
         print(f"You don't have enough balance to bet that amount, your current balance is ${amount}")
     else:
        break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to:{Total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbols_value)
    print_slot_machine(slots)
    winnings, winnings_lines=check_winnings(slots,lines,bet,symbols_value)
    print(f" You won  ${winnings}.")
    print(f"You won on lines:", *winnings_lines)
    return winnings - Total_bet



def main():
    amount=deposit()
    while True:
        print(f"Current balance is ${amount}")
        spin=input("press enter to play ( q to quit).")
        if spin=="q":
            break
        amount += game(amount)
    print(f"You left with ${amount}")
main()


