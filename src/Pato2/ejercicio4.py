def min_elements_to_remove(l, r):
    n = r - l + 1
    bit_counts = [0] * 8 # Suponemos que los enteros son de 32 bits
    for i in range(l, r+1):
        for j in range(32):
            if i & (1 << j) != 0:
                bit_counts[j] += 1
    min_bits = min(bit_counts)
    return n - sum(1 for c in bit_counts if c == min_bits)

t=int(input())
for _ in range(1,t+1):
    l,r=map(int ,input().split())
    print(min_elements_to_remove(l,r))
