a, b = input().split()
c, d = input().split()
e, f = input().split()


def check(sym, tem):
    if sym == 'Y' and int(tem) >=37:
        return 1
    return 0


if check(a, b) + check(c, d) + check(e, f) >= 2:
    print('E')
else:
    print('N')