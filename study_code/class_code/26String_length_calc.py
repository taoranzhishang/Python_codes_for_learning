def string_length_calc(str):
    count = 0
    for data in str:#遍历字符串，轮巡一次，计数器加1
        count += 1
    return count


def main():
    string = input("Please enter a string:")
    characters_count = string_length_calc(string)
    print("The number of characters in this string are: %d" % characters_count if characters_count > 1 \
              else "The number of characters in this string is: %d" % characters_count)


if __name__ == "__main__":
    main()
