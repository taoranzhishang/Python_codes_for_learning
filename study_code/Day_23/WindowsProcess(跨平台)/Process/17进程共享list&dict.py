import multiprocessing


def func(Flist, Fdict):
    Flist.append(4)
    Flist.append(3)
    Flist.append(2)
    Flist.append(1)
    Flist.append(0)

    Fdict["L"] = "wsz"
    Fdict["P"] = 0


if __name__ == "__main__":
    # with multiprocessing.Manager() as MG:
    #     myList = MG.list(range(5))
    #     myDict = MG.dict()
    #     p = multiprocessing.Process(target=func, args=(myList, myDict))
    #     p.start()
    #     p.join()
    #     print(myList)
    #     print(myDict)

    myList = multiprocessing.Manager().list(range(5))
    myDict = multiprocessing.Manager().dict()
    p = multiprocessing.Process(target=func, args=(myList, myDict))
    p.start()
    p.join()
    print(myList)
    print(myDict)
