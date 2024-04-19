m_3 = 0
m_5 = 0

for _ in range(10):
    num = int(input())

    if num % 3 == 0:
        m_3 += 1
    if num % 5 == 0:
        m_5 += 1

print(m_3, m_5)