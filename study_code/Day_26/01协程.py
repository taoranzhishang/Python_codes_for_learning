def func():
    print("Stage 1")
    yield 1
    print("Stage 2")
    yield 2
    print("Stage 3")
    yield 3


"""
Python协程的最简单形式，控制函数的阶段执行，节约进程现成的切换
"""
coroutine = func()  # 生成器
print(next(coroutine))
print(next(coroutine))
