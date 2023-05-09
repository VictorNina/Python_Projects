def palindrome(vector):
    if len(vector) <= 1:
        return True
    if vector[0] != vector[-1]:
        return False
    return palindrome(vector[1:-1])


n=int(input())
vector=list(map(int, input().split()))
if palindrome(vector):
    print("SI")
else:
    print("NO")