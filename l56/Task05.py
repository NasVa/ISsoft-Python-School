import random

nums = [4, 5, 7, 1, 6, 8, 13, 9, 12, 10, 3]

def k_min(A, k):
    q = random.randint(0, len(A) - 1)
    s = []
    m = []
    try:
        for i in range (len(A) - 1):
            if A[i] < A[q]:
                s.append(A[i])
            elif A[i] > A[q]:
                m.append(A[i])
        if k < len(s):
            return k_min(s, k)
        elif k >= len(A) - len(m):
            return k_min(m, k - (len(A) - len(m)))
        else:
            return A[q]
    except TypeError:
        return("Incomparable types of elements")
    
k = 0
while k > len(nums) or k <= 0:
    k = int(input(f"k > {len(nums)}: "))
print(k_min(nums, k))
