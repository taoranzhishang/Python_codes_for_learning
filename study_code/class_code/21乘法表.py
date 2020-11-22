for i in range(1, 10):
    for j in range(1, i + 1):
        result = i * j
        print("{}×{}={:2}".format(j, i, result), end="\t")
    print()
