history = []
calc = True

def addition(fNum, lNum):
    ttl = fNum+lNum
    output=(str(fNum)+"+"+str(lNum)+"="+str(ttl))
    print(output)
    history.append(output)
    print("==================================")
    print()

def substraction(fNum, lNum):
    ttl = fNum-lNum
    output=(str(fNum)+"-"+str(lNum)+"="+str(ttl))
    print(output)
    history.append(output)
    print("==================================")
    print()

def maltiplication(fNum, lNum):
    ttl = fNum*lNum
    output=(str(fNum)+"*"+str(lNum)+"="+str(ttl))
    print(output)
    history.append(output)
    print("==================================")
    print()

def divition(fNum, lNum):
    ttl = fNum/lNum
    output=(str(fNum)+"/"+str(lNum)+"="+str(ttl))
    print(output)
    history.append(output)
    print("==================================")
    print()


def main():
    print("1. Addition")
    print("2. Substraction")
    print("3. Maltiplication")
    print("4. Divition")
    print("5. History")
    print("6. Reset History")
    print("7. Exit")

    print()
    operator= int(input("Enter your operator  : "))
    if operator>7:
        print("Invalid number")
        print()

    elif operator==1:
        print("Addition")
        print("------------------Addition ------------------")
        fNum = int(input("Enter your first Number : "))
        lNum = int(input("Enter your last Number  : "))
        addition(fNum,lNum)
    elif operator==2:
        print("Substraction")
        print("------------------Substraction ------------------")
        fNum = int(input("Enter your first Number : "))
        lNum = int(input("Enter your last Number  : "))
        substraction(fNum,lNum)
    elif operator==3:
        print("Maltiplication")
        print("------------------Maltiplication ------------------")
        fNum = int(input("Enter your first Number : "))
        lNum = int(input("Enter your last Number  : "))
        maltiplication(fNum,lNum)
    elif operator==4:
        print("Divition")
        print("------------------Divition ------------------")
        fNum = int(input("Enter your first Number : "))
        lNum = int(input("Enter your last Number  : "))
        divition(fNum,lNum)
    
    elif operator==5:
        print("------------------HISTORY ------------------")
        for x in history:
            print(x)
        print("---------------------------------------------")
        print()
    elif operator==6:
        history.clear()
        print("History was cleared")
        print("---------------------------------------------")
        print()
    elif operator==7:
        print("Exited")
        global calc
        calc=False

while calc == True:
    main()
