def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")    


def main():
    value = int(input("How many numbers : "))
     
    data = list()

    Accept(data,value)
    Display(data)

    No = int(input("Enter the number to search : ")) 
    Ret = list(filter(lambda no : (no == No),data))
    if(len(Ret) == 0):
        print("Number is not present !!!")
    else:
        print("Number is present")    
        



if __name__ == "__main__":
    main()