import random

# пузырьком
def bubblesSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# вставки
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j] :
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Шелла
def shellSort(array):
    inc = len(array)
    while inc:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc
            array[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return array

# выбором
def choiceSort(array):
    i = 0
    while i < len(array) - 1:
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j += 1
        array[i], array[m] = array[m], array[i]
        i += 1
    return array


# быстрая, опорный рандомный
def quickSort(array):
   if len(array) <= 1:
       return array
   else:
       q = random.choice(array)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in array:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quickSort(s_nums) + e_nums + quickSort(m_nums)

# слиянием
def merge(A, B):
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i]) 
            i += 1 
        else:
            Res.append(B[j]) 
            j += 1 
    Res += A[i:] + B[j:] 
    return Res

def MergeSort(A): 
    if len(A) <= 1: 
        return A 
    else:
        L = A[:len(A) // 2] 
        R = A[len(A) // 2:] 
    return merge(MergeSort(L), MergeSort(R))


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

