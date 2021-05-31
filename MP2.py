from operator import attrgetter


class Process:
    def __init__(self, name, arrival, time, priority):
        self.name = name
        self.arrival = arrival
        self.time = time
        self.priority = priority
    waitingTime = 0


class QuantizedProcess:
    name = ""
    timeConsumed = 0
    #waitingTime = 0

def get_time(p):
    return p.get('time')

# for line in finalStrippedLines:
#     name = ""
#     spaceIndex = 0
#     for char in line:
#         if char != ' ':
#             spaceIndex += 1
#         else:
#             break
#     #extract substring from index 0 to spaceIndex - 1
#     name = line[0:spaceIndex-1]
#     #remove all characters from index 0 to spaceIndex
#     newLine = line[spaceIndex:]

# spaceIndex = 0
# for char in line:
#     if char != ' ':
#         spaceIndex += 1
#     else:
#         break
# #extract substring from index 0 to spaceIndex - 1
# if spaceIndex == 1:
#     name = line[0:1]
# else:
#     name = line[0:spaceIndex+1]
# print(name)
# #remove all characters from index 0 to spaceIndex
# newLine = line[spaceIndex+1:]
# print(newLine)

def extractLeftmostNumber(line):
    spaceIndex = 0
    for char in line:
        if char != ' ':
            spaceIndex += 1
        else:
            break
    #extract substring from index 0 to spaceIndex - 1
    if spaceIndex == 1:
        num = line[0:1]
    else:
        num = line[0:spaceIndex+1]
    
    return num

def removeLeftmostNumber(line):
    #print(line)
    spaceIndex = 0
    for char in line:
        if char != ' ':
            spaceIndex += 1
        else:
            break
    #print(spaceIndex)
    newLine = line[spaceIndex+1:]
    return newLine
    #return newLine
   
# line = "2 1 15 0"
# print(line)
# print(extractLeftmostNumber(line))
# print(removeLeftmostNumber(line))


lines = []
filename = input("Enter filename to be read as input: ")
with open (filename, 'r') as f:
    for line in f:
        lines.append(line)

lines.pop(0)  
#print(lines)



strippedLines = [s.replace("\t\t", ' ') for s in lines]
#print(strippedLines)
finalStrippedLines = [s.replace("\t", '') for s in strippedLines]
#print(finalStrippedLines)


processes = []
for line in finalStrippedLines:
    # numbersExtracted = 0
    # while numbersExtracted < 3:
    #     if numbersExtracted == 0:
    #         name = extractLeftmostNumber(line)
    #         arrivelLine = removeLeftmostNumber(line)
    #         numbersExtracted += 1
    #print(line)
    name = extractLeftmostNumber(line)
    arrivalLine = removeLeftmostNumber(line)
    #print(name)

    arrival = extractLeftmostNumber(arrivalLine)
    timeLine = removeLeftmostNumber(arrivalLine)
    #print(arrival)

    time = extractLeftmostNumber(timeLine)
    priorityLine = removeLeftmostNumber(timeLine)
    #print(time)

    priority = extractLeftmostNumber(priorityLine)
    #print(priority)
    
    newProcess = Process(name,arrival,time,priority)
    # print(newProcess.name)
    # print(newProcess.arrival)
    # print(newProcess.time)
    # print(newProcess.priority)

    processes.append(newProcess)



# # FIRST COME FIRST SERVE # # #
print(" # # # # # FIRST COME FIRST SERVE # # # # #")
waitingTime = 0
totalWaitingTime = 0
numOfProcesses = 0
for p in processes:
    print("Process " + p.name + " waiting time: " + str(waitingTime)+" ms")
    totalWaitingTime += waitingTime
    waitingTime += int(p.time)
    numOfProcesses += 1
    #print(totalWaitingTime)
    #print('\n')

#print(numOfProcesses)
averageWaitingTime = totalWaitingTime/numOfProcesses
print("\nFCFS Average Waiting Time = " + str(averageWaitingTime) + " ms\n")

turnaroundTime = 0
totalTurnaroundTime = 0
numOfProcesses = 0
for p in processes:
    turnaroundTime += int(p.time)
    print("Process " + p.name + " turnaround time: " + str(turnaroundTime)+" ms")
    totalTurnaroundTime += turnaroundTime
    numOfProcesses += 1
averageTurnaroundTime = totalTurnaroundTime/numOfProcesses
print("\nFCFS Average Turnaround Time = " + str(averageTurnaroundTime) + " ms\n")



print(" # # # # # SHORTEST JOB FIRST # # # # #")
waitingTime = 0
totalWaitingTime = 0
numOfProcesses = 0
sortedProcesses = sorted(processes, key=lambda x: int(x.time), reverse=False)
for p in sortedProcesses:
    #print(p.time)
    print("Process " + p.name + " waiting time: " + str(waitingTime)+" ms")
    totalWaitingTime += int(waitingTime)
    waitingTime += int(p.time)
    numOfProcesses += 1

averageWaitingTime = totalWaitingTime/numOfProcesses
print("\nSJF Average Waiting Time = " + str(averageWaitingTime) + " ms\n")

turnaroundTime = 0
totalTurnaroundTime = 0
numOfProcesses = 0
for p in sortedProcesses:
    turnaroundTime += int(p.time)
    print("Process " + p.name + " turnaround time: " + str(turnaroundTime)+" ms")
    totalTurnaroundTime += turnaroundTime
    numOfProcesses += 1
averageTurnaroundTime = totalTurnaroundTime/numOfProcesses
print("\nSJF Average Turnaround Time = " + str(averageTurnaroundTime) + " ms\n")


print(" # # # # # PRIORITY # # # # #")
waitingTime = 0
totalWaitingTime = 0
numOfProcesses = 0
sortedProcesses = sorted(processes, key=lambda x: int(x.priority), reverse=False)
for p in sortedProcesses:
    #print(p.time)
    print("Process " + p.name + " waiting time: " + str(waitingTime)+" ms")
    totalWaitingTime += int(waitingTime)
    waitingTime += int(p.time)
    numOfProcesses += 1

averageWaitingTime = totalWaitingTime/numOfProcesses
print("\nPRIORITY Average Waiting Time = " + str(averageWaitingTime) + " ms\n")

turnaroundTime = 0
totalTurnaroundTime = 0
numOfProcesses = 0
for p in sortedProcesses:
    turnaroundTime += int(p.time)
    print("Process " + p.name + " turnaround time: " + str(turnaroundTime)+" ms")
    totalTurnaroundTime += turnaroundTime
    numOfProcesses += 1
averageTurnaroundTime = totalTurnaroundTime/numOfProcesses
print("\nPRIORITY Average Turnaround Time = " + str(averageTurnaroundTime) + " ms\n")


print(" # # # # # SHORTEST REMAINING PROCESSING TIME # # # # #")
waitingTime = 0
totalWaitingTime = 0
numOfProcesses = 0

sortedProcesses = sorted(processes, key=lambda x: int(x.arrival), reverse=False)

currentProcesses = []
timeLine = []
processWithMinimumTime = None
for p in sortedProcesses:
    currentProcesses.append(p)
    processWithMinimumTime = min(currentProcesses, key=attrgetter('time'))
    #print(processWithMinimumTime.name)
    timeLine.append(processWithMinimumTime)


print("sorry miss, wa jud na kaya saakong powers ang SRPT :(\n")
# for t in timeLine:
#     print(t.name + t.time)



    


print(" # # # # # ROUND ROBIN # # # # #")
roundRobinProcesses = []
for p in processes:
    roundRobinProcesses.append(p)

# for p in roundRobinProcesses:
#     print(p.name+", burst time = "+p.time)

quantizedProcesses = []
totalElapsedTime = 0
while roundRobinProcesses != []:
    for p in roundRobinProcesses:
        newQP = QuantizedProcess()
        #newQP.origTime = int(p.time)
        timeLeft = int(p.time) - 4
        if timeLeft > 0:
            p.time = timeLeft
            totalElapsedTime += 4
            newQP.name = p.name
            newQP.timeConsumed += 4
            #print("Process "+newQP.name +" time consumed = "+str(newQP.timeConsumed))
            quantizedProcesses.append(newQP)
        elif timeLeft < 0:
            totalElapsedTime += int(p.time)
            newQP.name = p.name
            newQP.timeConsumed += int(p.time)
            #print("Process "+newQP.name +" time consumed = "+ str(newQP.timeConsumed))
            quantizedProcesses.append(newQP)
            roundRobinProcesses.remove(p)
        else:
            totalElapsedTime += 4
            newQP.name = p.name
            newQP.timeConsumed += 4
            #print("Process "+newQP.name +" time consumed = "+ str(newQP.timeConsumed))
            quantizedProcesses.append(newQP)
            roundRobinProcesses.remove(p)
        #print("Process "+str(p.name)+" time left = "+str(p.time))


processesCopy = processes
elapsedTime = 0
for p in processesCopy:
    tempWaitingTime = 0
    for qp in quantizedProcesses:
        if p.name != qp.name:
            tempWaitingTime += qp.timeConsumed
        else:
            p.waitingTime += tempWaitingTime
            tempWaitingTime = 0

totalWaitingTime = 0
numOfProcesses = 0
for p in processesCopy:
    print("Process "+p.name+" waiting time = "+str(p.waitingTime)+" ms")
    totalWaitingTime += p.waitingTime
    numOfProcesses+=1

averageWaitingTime = totalWaitingTime/numOfProcesses
print("\nROUND ROBIN Average Waiting Time = " + str(averageWaitingTime) + " ms\n")








# for qp in quantizedProcesses:
#     #print("Process "+qp.name+" time consumed = "+str(qp.timeConsumed))
#     for currProcess in quantizedProcesses:
#         if qp.name != currProcess.name:
#             qp.waitingTime += currProcess.timeConsumed
#         elif qp.name == currProcess.name:
#             pass
#     print ("Process " +qp.name + " waiting time = "+str(qp.waitingTime))


# for p in processes:
#     for qp in quantizedProcesses:
#         if p.name != qp.name:
#             p.waitingTime += qp.timeConsumed
#         elif p.name == qp.name:
#             #check if there are still duplicate p.name's in quantizedP's
#             pIsNotFinished = 0
#             for i in quantizedProcesses:
#                 if p.name == i.name:
#                     pIsNotFinished = 1
#                 else:
#                     pass
            

#     print("Process "+p.name+" waiting time = "+ str(p.waitingTime))
# for qp in quantizedProcesses:
#     print("Process "+qp.name+" time consumed = "+ str(qp.timeConsumed))