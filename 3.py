n = int(input())
for i in range(n):
    first = [int(x) for x in input().split()]
    second = [int(x) for x in input().split()]
    fmin = min(first)
    fmax = max(first)
    print(fmin, fmax)
    answer = [num for num in second if fmin <= num <= fmax]
    print(" ".join(str(x) for x in answer))
