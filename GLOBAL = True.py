GLOBAL = True


def make_false():
    global GLOBAL
    GLOBAL = False


print(GLOBAL)

make_false()

print(GLOBAL)
