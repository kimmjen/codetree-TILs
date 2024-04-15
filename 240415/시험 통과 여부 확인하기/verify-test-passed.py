score = int(input())

if score >= 80:
    print('pass')
else:
    need = 80 - score
    print(f"{need} more score")