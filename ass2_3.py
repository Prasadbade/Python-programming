def Factorial(No):
    fact = 1
    for i in range(1,(No+1)):
        fact = fact * i

    return fact    


def main():
    value = int(input("Enter the Number"))
    
    Ret = Factorial(value)
    print("Factorial of Number is : ",Ret)    

if __name__ == "__main__":
    main()