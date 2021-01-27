import random


def merge(list1, list2):
    index1 = index2 = 0
    mergeList = list()
    while index1 < len(list1) and index2 < len(list2):
        """
        对所有元素进行归并
        """
        # if list1[index1] <= list2[index2]:
        #     mergeList.append(list1[index1])
        #     index1 += 1
        # else:
        #     mergeList.append(list2[index2])
        #     index2 += 1
        """
        相同索引元素相同归并一次
        """
        if list1[index1] < list2[index2]:
            mergeList.append(list1[index1])
            index1 += 1
        elif list1[index1] > list2[index2]:
            mergeList.append(list2[index2])
            index2 += 1
        else:
            mergeList.append(list1[index1])
            index1 += 1
            index2 += 1

    while index1 < len(list1):
        mergeList.append(list1[index1])
        index1 += 1
    while index2 < len(list2):
        mergeList.append(list1[index2])
        index2 += 1

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
