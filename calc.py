def main():
    #get the inputs
    x = int(input("First Number: "))
    y = int(input("Second Number: "))

    #choose the operation
    op = input("Add or Multi: ").capitalize()

    #apply the selected operation
    if op == 'A':
        add(x, y)
    elif op == 'M':
        multi(x, y)
    else:
        print("Invalid")

#define operation for multiplication
def multi(x, y):
    print(x * y)

#define operation for addition
def add(x, y):
    print(x + y)
    
#call main
main()