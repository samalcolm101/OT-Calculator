from tabulate import tabulate  # packaghe for displaying the inputs nicely

allDays = []
MONTH = input("Month: ")  # gets the month
if MONTH == "February":  # deals with leap years
    leap = input("Is it a leapyear? ")
    if leap == "Yes":
        leapYear = True


def howManyDays(month, leapYear=False):  # gets how many days are in a month
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    if leapYear:
        return daysInMonths[12]

    return(daysInMonths[months.index(month.title())])


DAYS = howManyDays(MONTH)
LUNCH = input("Lunch: ")  # gets the legnth of the lunch break in hours

""" EXPLANATIONS FOR HOW calcType WORKS
calcType 1: HUMAN --> MATHS
calcType 2: MATHS --> HUMAN

"""


def timeToNum(calcType, time1):
    if calcType == 1:
        partitioned = time1.partition(":")  # splits hours and minutes
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

        return (f"{hours}.{mins}")  # returns in a maths format

    elif calcType == 2:
        partitioned = time1.partition(".")
        hours = int(partitioned[0])
        mins = float(partitioned[2])
        while mins > 1:  # there is a power factor issue somewhere, and this bodgily fixes it
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


def cleanUpTimes(time1):  # does some housekeeping
    time1 = timeToNum(1, time1)
    time1 = timeToNum(2, time1)

    return time1


def timeDifference(start, finish):  # calculates the time difference
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

    return(timeToNum(2, str(calc)))  # returns it in human form not maths form


def dataInput():
    for _ in range(1, DAYS+1):  # loops through however many days there are in that month
        if _ > 1.1:
            print(tabulate(allDays))
        op = []
        op.append(_)
        print(_)
        startTime = input("Start Time: ")  # gets the start time
        if startTime == "NWD":  # handles non working days
            allDays.append([_, 0, 0, 0, 0])
            continue
        op.append(cleanUpTimes(startTime))
        finishTime = input("Finish Time: ")  # gets the finish time
        op.append(cleanUpTimes(finishTime))
        op.append(LUNCH)
        op.append(timeDifference(startTime, finishTime))
        allDays.append(op)  # appends the final list


def calcTotalHours():
    totalHours = 0
    for day in allDays:
        if day[4] == 0:  # handles Non working days
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
print(tabulate(allDays, headers=["Date", "Start Time", "Finish Time", "Lunch Time", "Total Work"]))

print(f"""
Total Hours: {totalHours}
Hourly Salary: {hourlySalary}
Total Hourly Pay: £{totalHours*hourlySalary}

""")
