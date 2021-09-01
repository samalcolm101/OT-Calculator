from tabulate import tabulate
"""
table = [["Sun", 696000, 1989100000], ["Earth", 6371, 5973.6],
         ["Moon", 1737, 73.5], ["Mars", 3390, 641.85]]

print(tabulate(table))

"""


allDays = []
MONTH = input("Month: ")


def howManyDays(month, leapYear=False):
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    if leapYear:
        return daysInMonths[12]

    return(daysInMonths[months.index(month.title())])


DAYS = howManyDays(MONTH)
LUNCH = input("Lunch: ")


"""
calcType 1: HUMAN --> MATHS
calcType 2: MATHS --> HUMAN

"""


def timeToNum(calcType, time1, time2=0, time3=0):
    if calcType == 1:
        partitioned = time1.partition(":")
        hours = int(partitioned[0])
        mins = int(partitioned[2])
        if mins < 8:  # upto xx:07
            mins = 0
        elif mins < 23:  # between xx:08 and xx:22
            mins = .25
        elif mins < 38:  # between xx:23 and xx:37
            mins = .5
        elif mins < 52:  # between xx:38 and xx:52
            mins = .75
        elif mins < 60:  # between xx:53 and xx:59
            hours += 1
            mins = 0

        return (f"{hours}.{mins}")

    elif calcType == 2:
        partitioned = time1.partition(".")
        hours = int(partitioned[0])
        mins = float(partitioned[2])
        while mins > 1:
            mins = mins/10

        if mins == 0:
            mins = 0
        elif mins == 0.25:
            mins = 15
        elif mins == 0.5:
            mins = 30
        elif mins == 0.75:
            mins = 45
        return(f"{hours}:{mins}")


def cleanUpTimes(time1):
    time1 = timeToNum(1, time1)
    time1 = timeToNum(2, time1)

    return time1


def timeDifference(start, finish):
    start = timeToNum(1, start)
    finish = timeToNum(1, finish)

    partitioned = start.partition(".")
    startHours = int(partitioned[0])
    startMins = float((partitioned[2]))

    partitioned = finish.partition(".")
    finshHours = int(partitioned[0])
    finishMins = float(partitioned[2])
    startJoined = startHours + startMins
    finishJoined = finshHours + finishMins

    calc = finishJoined - startJoined

    return(timeToNum(2, str(calc)))


def dataInput():
    for _ in range(1, DAYS+1):
        if _ > 1.1:
            print(tabulate(allDays))
        op = []
        op.append(_)
        print(_)
        startTime = input("Start Time: ")
        if startTime == "NWD":
            allDays.append([_, 0, 0, 0, 0])
            continue
        op.append(cleanUpTimes(startTime))
        finishTime = input("Finish Time: ")
        op.append(cleanUpTimes(finishTime))
        op.append(LUNCH)
        op.append(timeDifference(startTime, finishTime))
        allDays.append(op)


def calcTotalHours():

    totalHours = 0
    for day in allDays:
        if day[4] == 0:
            continue
        mathsTime = timeToNum(1, day[4])

        partitioned = mathsTime.partition(".")
        mathsHours = int(partitioned[0])
        mathsMins = float(partitioned[2])
        mathsJoined = mathsHours + mathsMins
        mathsJoined -= int(LUNCH)
        totalHours += mathsJoined
    return totalHours

dataInput()
# calcTotalHours()

salary = input("What is your yearly salary: ")
monthSalary = int(salary)/12
daySalary = monthSalary/DAYS
hourlySalary = daySalary/8
totalHours = calcTotalHours()
print(tabulate(allDays))

print(f"""

Total Hours: {totalHours}
Hourly Salary: {hourlySalary}
Total Hourly Pay: £{totalHours*hourlySalary}

""")
