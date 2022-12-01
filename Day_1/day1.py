

def loadFile():
    with open('AOC\day1_input.txt', 'r') as file:
        data = file.read()
    return data
    
def findMaxCalories():
    inputs =loadFile()
    
    curCal = 0
    top1Cal = 0
    top2Cal = 0
    top3Cal = 0
    splitInput = inputs.splitlines()
    for splits in splitInput:
        if(splits == ''): #new elf!
            if(curCal > top1Cal):
                if(top1Cal > top2Cal):
                    top2Cal = top1Cal
                top1Cal = curCal
            elif(curCal > top2Cal):
                if(top2Cal > top3Cal):
                    top3Cal = top2Cal
                top2Cal = curCal
            elif(curCal > top3Cal):
                top3Cal = curCal
            curCal = 0
        else:
            curCal += int(splits)
            
    print(top1Cal)
    print(top2Cal)
    print(top3Cal)
    
    return (top1Cal+ top2Cal+ top3Cal)

print(findMaxCalories())
#loadFile()