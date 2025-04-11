def findProduct(li):
    answer = 1
    for ele in li:
        answer = (answer * ele) % (10 **9 + 7)
    print(answer)

# n = int(input())
# A = list(map(int, input().split()))
A = [1,2,3,4,5]
findProduct(A)