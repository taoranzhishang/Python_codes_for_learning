print(sorted([1, 3, 5, 2, 0]))  # [0, 1, 2, 3, 5]，返回list，默认从小到大
print(sorted([1, 3, 5, 2, 0], reverse=True))  # [5, 3, 2, 1, 0] 从大大小
print(sorted([1, 2, -5, 1, -0]))  ##[-5, 0, 1, 1, 2]
print(sorted([1, 2, -5, 1, -0], key=abs))  # [0, 1, 1, 2, -5] 按绝对值排
print(sorted("abcACB"))  # ['A', 'B', 'C', 'a', 'b', 'c']，从小到大
print(sorted(["aBc", "YTc", "YUOi"]))  # ['YTc', 'YUOi', 'aBc']，按每个元素能区别大小的字母排
print(sorted(["aBc", "YTc", "YUOi"], reverse=True))  # ['aBc', 'YUOi', 'YTc']，从小到大
print(sorted(["aBc", "YTc", "YUOi"], key=str.lower))  # ['aBc', 'YTc', 'YUOi']，全部按小写排
print(sorted(["aBc", "YTc", "YUOi"], key=str.upper))  # ['aBc', 'YTc', 'YUOi']，全部按大写排
