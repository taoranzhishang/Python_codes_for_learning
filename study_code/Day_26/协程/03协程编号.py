def func():
    data = ''
    for i in range(1, 10):
        r = yield data
        print(i, r)


coroutine = func()
# coroutine.send(None)
# coroutine.send("xi")
# coroutine.send("li")
# coroutine.send("wang")
for i in [None, "xi", "li", "wang"]:
    coroutine.send(i)
