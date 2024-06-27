def convertnegative(output):
    """
    Converts negative numbers into positive numbers
    """
    if(output<0):
        output = output*-1
    return output
def factorial(number):
    """
    This function calculates the factorial number of number inserted in the variable number
    """
    number = convertnegative(number)
    multiplier = [1] * (number +1)
    multiplier2 = [1] * (number +1)
    counter = 0
    counter2 = 0
    output=0
    while(True):
        
        if(number == 0):
            print("0! = 1")
            print(f"The factorial of 0 is 1")
            break
        if(abs(counter) == 0):
            print("0! = 1")
            counter = number - 1
           
        if(counter < number):
            output=0
            print(f"{abs(counter - number-1)}! = {abs(counter - number-1)}", end=" ")
            counter2 = counter
            for i in range(number):
                for b in range(abs(number - counter2+1) ):
                    multiplier2[b] = abs(counter2 - number)
                    print(f"{multiplier2[b]}", end=" ")
                    if(b >0):
                        if(output==0):
                            output = multiplier2[b-1]+1
                        else:
                            output = output * (multiplier2[b]+2)
                    counter2+=1
                    b+=1
                i+=1
            counter-=1
            print("")
        if(counter <=0):
            return output
while(True):
    try:
        number = int(input("Type a number to get its factorial: "))
        output = factorial(number)
        print(f"The factorial of {number} is {output}")
        break
    except ValueError:
        print("Invalid number, type a valid number.")
