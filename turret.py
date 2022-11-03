caseCnt = int(input())
caseArray = []

for _ in range(caseCnt):
    aqw = list(map(int,input().split()))
    caseArray.append(aqw)
caseResult = []

for i in range(caseCnt):
    tempArray = caseArray[i]
    x1,y1 = tempArray[0],tempArray[1]
    x2,y2 = tempArray[3],tempArray[4]
    r1,r2 = tempArray[2],tempArray[5]
    x_marin, y_marin = "x", "y"
    
    exp1 = (x_marin-x1)**2 + (y_marin-y1)**2 - r1**2
    exp2 = (x_marin-x2)**2 + (y_marin-y2)**2 - r2**2

    expMid = exp1-exp2
    print(expMid)