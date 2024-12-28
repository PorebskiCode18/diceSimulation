import random
sumArray=[]
specialRoll=[0,0,0,0,0,0,0,0,0,0,0]
def rollDie():
    global sumArray
    ranNum1=random.randrange(1,7)
    ranNum2=random.randrange(1,7)
    sum= ranNum1 + ranNum2
    sumArray.append(sum)
def checkArray():
    global sumArray, specialRoll
    for i in range(1000):
        for x in range(12):
            if sumArray[i]==x+2:
                specialRoll[x]+=1
def main():
    for i in range(1000):
        rollDie()
    checkArray()
    print("Out of 1000 rolls, you rolled a sum of:")
    for x in range(11):
        print(x+2,":", specialRoll[x])
main()