import string

def main():
    #getting the number of elements to be calculated
    n = int(input("Number of elements to calculate: "))

    elements = []

    #get values for each element in the list
    element = input(f"Enter value for element {chr(ord('a') + i)}: ")
    elements.append(element)
    
    #choose the operation
    while True:
        op = input("Choose the operation: ").capitalize()
        if op in ['A', 'M', 'D', 'S']:
            break

    #apply the selected operation
    if op == 'A':
        add(x, y)
    elif op == 'M':
        multi(x, y)
    elif op == 'S':
        sub(x, y)

        #avoid clash with division with 0
    elif op == 'D':
        if x or  y == 0:
            print("Calculation not possible. Retry with correct calculation")
        else:
            div(x, y)
    else:
        print("Invalid")

#define operation for multiplication
def multi(x, y):
    print(x * y)

#define operation for addition
def add(x, y):
    print(x + y)

#define operation for subtraction
def sub(x, y):
    print(x - y)

#define operation for division
def div(x, y):
    print(x / y)
    
#call main
main()