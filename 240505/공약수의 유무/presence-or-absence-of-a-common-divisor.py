a,b = map(int,input().split())
arr = []
for i in range(2, 1920):
    if 1920 % i == 0 and 2880 % i ==0:
        arr.append(i)
sati = False
for j in range(len(arr)):
    if arr[j] >=a and arr[j] <=b:
        sati = True
if sati == True:
    print(1)
else:
    print(0)