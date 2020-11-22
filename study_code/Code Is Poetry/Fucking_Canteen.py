school_canteen_is_disgusting = 1
greetings = "学校食堂ZTM恶心 🤮🤮🤮 ╭∩╮（︶︿︶）╭∩╮"


def FuckingCanteen(greeting):
    (lambda sentence: print(sentence))(greeting)  # 真切的问候


def main():
    nausea_index = 1
    while school_canteen_is_disgusting:  # 喷死恶心的食堂，如果要加一个次数限制，次数为：无限次，无限制一直喷！！！
        FuckingCanteen(str("又被恶心了一次，食堂恶心指数：%d\t" % nausea_index) + greetings)  # 去一次喷一次
        nausea_index += 1  # 表示又被恶心了一次，指数加1


if __name__ == "__main__":
    main()
