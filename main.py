MAX_LINES=3
MAX_BET=100
MIN_BET=1
rows=3
cols=3
symbols={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[[],[],[]]
    

def deposit():
    while True:
        amount = input("Enter amount you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter valid amount greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Enter a number for lines.")
    return lines


def get_bet():
    while True:
        bet=input("Enter amount you wanna bet on each line: $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Enter valid amount for bet between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a number")
    return bet

def main():
    balance = deposit()
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount.Current balance={balance}")
        else:
            break
    print(f"You're betting ${bet} on {lines} lines.Total bet =${total_bet}")
    # print(balance,lines)


main()
