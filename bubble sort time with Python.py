import time
from random import randint

#버블 정렬
#array = []
#for _ in range(1000):
#    array.append(randint(1, 100))

#최악
array_b = []

for i in range(10000, 1, -1):
    array_b.append(i)

start_time = time.time()

for i in range(len(array_b)-1):
    for j in range(len(array_b)-1 - i):
        if array_b[j] > array_b[j + 1]:
            array_b[j], array_b[j + 1] = array_b[j + 1], array_b[j]

end_time = time.time()
print("버블 정렬 최악 성능 측정:", end_time - start_time)


#최선
array = []

for i in range(1, 10000):
    array.append(i)

start_time = time.time()

for i in range(len(array)-1):
    for j in range(len(array)-1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

end_time = time.time()
print("버블 정렬 최선 성능 측정:", end_time - start_time)
