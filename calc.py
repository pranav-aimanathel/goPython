def main():
    x = int(input("First Number: ")) 
    y = int(input("Second Number: ")) 
    op = input("Add or Multi: ")

    if op == 'A':
        add(x, y)
    elif op == 'M':
        multi(x, y)
    else:
        print("Invalid")


def multi(x, y):
    print(x * y)

def add(x, y):
    print(x + y)
    

main()