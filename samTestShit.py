def timeDifference(start, finish):
    partitioned = start.partition(":")
    startHours = int(partitioned[0])
    startMins = int(partitioned[2])

    partitioned = finish.partition(":")
    finshHours = int(partitioned[0])
    finishMins = int(partitioned[2])

    startJoined = int(f"{startHours}.{startMins}")
    print(startJoined)

timeDifference("09:30", "18:30")
