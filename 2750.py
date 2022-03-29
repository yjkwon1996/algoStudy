# 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750

"""
N개의 수가 주어졌을 때 오름차순으로 정렬
"""
# 첫째 줄에 수의 개수 N이 주어지고
# 둘째 줄부터 N개의 줄에 수가 주어진다.
# 수는 중복되지 않으며 절댓값이 1000보다 작거나 같은 정수

N = int(input())

arr = []
for i in range(N) :
    num = int(input())
    arr.append(num)

arr.sort()
for i in range(N) :
    print(arr[i])


# 2751 수 정렬하기 2
# https://www.acmicpc.net/problem/2750

# 위와 동일하지만, 시간복잡도가 O(nlogn)으로 해결할 수 있다.




