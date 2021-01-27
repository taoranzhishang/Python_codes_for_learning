import random


def merge(list1, list2):
    mergeList = list()
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            mergeList.append(list1[0])
            del list1[0]
        else:
            mergeList.append(list2[0])
            del list2[0]
    mergeList.extend(list1)
    mergeList.extend(list2)
    return mergeList


def main():
    list1 = [random.randint(0, pow(x, 2)) for x in range(1, 11)]
    list2 = [random.randint(0, x * 2) for x in range(10, 0, -1)]
    print(list1, "\n", list2)

    list1.sort()
    list2.sort()
    print(list1, "\n", list2)

    print(merge(list1, list2))


if __name__ == "__main__":
    main()
