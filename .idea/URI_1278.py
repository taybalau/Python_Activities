a = int(input())
final = ''

while True:
    b = []
    for i in range(a):
        c = input().split()
        c = ' '.join(c)
        b.append(c)

    d = []
    for j in b:
        e = len(j)
        d.append(e)

    maior = max(d)

    for m in b:
        if len(m) == maior:
            final = final + f'\n{m}'
        else:
            k = maior - len(m)
            u = ' ' * k
            final = final + f'\n{u}{m}'
    a = int(input())
    if a == 0:
        break
    final = final + f'\n'

final = final.replace(final[0], '', 1)
print(final)
