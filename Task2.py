
def commandSet():
    list4Check = set(list4Play)
    list2Print = []
    for num in list4Play:
        if num not in list2Print:
            list2Print.append(num)
    if len(list4Check) == len(list4Play):
        print ("It is a set")
    elif list2Print:
        # not set
        print(list2Print)



def commandFilter(oddOrEven, list4Play):
    #, list4Play
    if oddOrEven == 'even':
        list2Print = [x for x in list4Play if x % 2 == 0]
    else:
        list2Print = [x for x in list4Play if x % 2 != 0]
    if list2Print:
        print(list2Print)


def commandMult(elem, list4Play):
    list2Print = [elem*x for x in list4Play]
    if list2Print:
        print (list2Print)


def commandDiv(elem, list4Play):
    if elem == 0:
        print("ZeroDivisionError caught")
        return
    else:
        list2Print = [x/elem for x in list4Play]
        if list2Print:
            print (list2Print)


def commandSlice(list4Play, idx1, idx2):
    # from n to m including
    lenList = len(list4Play)-1
    list2Print = []
    if idx1 not in range(lenList) or idx2 not in range(lenList)\
            or idx2 < idx1:
        print("IndexError caught")
        return
    else:
        for idx in range(len(list4Play)):
            if idx >= idx1 and idx <= idx2:
                list2Print.append(list4Play[idx])
        if list2Print:
            print(list2Print)


def commandSort(list4Play):
    if list4Play:
        print(sorted(list4Play))


def commandReverse(list4Play):
    if list4Play:
        list2Print = list(reversed(list4Play))
        print(list2Print)



data = input()
count = 0 #rounds
listListmon = list(map(int, data.split()))

data = input()
while data != "exhausted":
    list4Play = listListmon
    count += 1
    command = data
    if command == "set":
        commandSet()
    elif command.startswith("filter"):
        oddOrEvenC = command.split()[1]
        commandFilter(oddOrEvenC, list4Play)
    elif command.startswith("multiply"):
        num = int(command.split()[1])
        commandMult(num, list4Play)
    elif command.startswith("divide"):
        num = int(command.split()[1])
        commandDiv(num, list4Play)
    elif command.startswith("slice"):
        start, stop = int(command.split()[1]), int(command.split()[2])
        commandSlice(list4Play, start, stop)
    elif command.startswith("sort"):
        commandSort(list4Play)
    elif command.startswith("reverse"):
        commandReverse(list4Play)

    data = input()


print(f"I beat It for {count} rounds!")
