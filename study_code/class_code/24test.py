import sys
a = 257


def main():
	b = 257  # 第6行
	c = 257  # 第7行
	print(b is c)  # True
	print(a is b)  # False
	print(a is c)  # False
	print(sys.maxsize)


if __name__ == "__main__":
	main()