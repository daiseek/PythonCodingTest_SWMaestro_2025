# K번째 수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	68200	24125	17140	41.746%

# 문제
# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

# 둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

# 출력
# A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.


# pivot을 정하는 방법
# 1) pivot == K => K번째 수를 찾았으므로 종료
# 2) pivot > K => 피봇 기준으로 왼쪽에 K가 있음. s부터 pivot-1까지 정렬 수행
# 3) pivot < K => 피봇 기준으로 오른쪽에 K가 있음. pivot+1부터 e까지 정렬 수행

# 여기서 배열의 중간 위치를 피봇으로 선택하자.


# 손으로 풀어보기
# Ex. [4, 1, 2, 3, 5]
# Step1. 중간에 있는 2를 피봇으로 선택
# 이후 맨 앞에 있는 4와 swap
# 피봇을 맨 앞으로 옮기는 이유는 i, j의 이동을 편하게 하기 위함
# 이후 i와 j를 각 그룹에서 왼쪽, 오른쪽 끝으로 정함

# [2, 1, 4, 3, 5]
# 여기서 pivot = 2, i =1, j = 5


# step2. j를 이동시킴
# step2-1 j > pivot => j-- 연산 반복
# 그럼, j = 5에서 j = 1이 되고, i와 만난다.

# step2-2 i < pivot => i++ 연산 반복
# 다만 위 리스트에서 i와 j가 만나기 때문에 이 과정은 할 필요 없다.


# step3. i=j이므로 pivot과 i(혹은 j)를 swap

# step5. K = 2이므로 더는 정렬하지 않고, A[1]을 출력한다.

# 슈도코드
# n 숫자 갯수 k k번째 수
# A 숫자 리스트

# # 별도의 함수로 수현
# 퀵 정렬 함수(시작, 종료):
#     데이터가 2개일 때 바로 비교해서 정렬
#     m 중앙값
#     중앙값을 시작 위치와 swap
#     pivot을 시작 위치 값 A[s]로 저장
#     i 시작점, j 끝점

#     while i < j:
#         pivot보다 큰 값이 나올 때까지 i++
#         pivot보다 작은 값이 나올 때까지 j--
#         찾은 i와 j를 swap

#     pivot을 나뉜 두 그룹의 경계 index에 저장
#     경계 index 반환

# 퀵 정렬 실행
# k번째 수 출력



# Solution Code
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(start, end, K):
    global A
    if start < end:
        pivot = partition(start, end)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(start, pivot-1, K)
        else:
            quickSort(pivot+1, end, K)
            
def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
def partition(start, end):
    global A
    
    if start + 1 == end:
        if A[start] > A[end]:
            swap(start, end)
        return end
    
    median = (start + end) // 2
    swap(start, median)
    pivot = A[start]
    i = start + 1
    j = end
    
    while i <= j:
        while pivot < A[j] and j>0:
            j -= 1
        while pivot > A[i] and i <len(A) - 1:
            i += 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1
            
    A[start] = A[j]
    A[j] = pivot
    return j

quickSort(0, n-1, K-1)
print(A[K-1])
            


# 다만.. 에러가 발생하여 gpt 코드를 참고

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(start, end, K):
    global A
    if start < end:
        pivot = partition(start, end)
        if pivot == K:
            return
        elif K < pivot: # 왼쪽 영역만 탐색
            quickSort(start, pivot - 1, K)
        else:   # 오른쪽 영역만 탐색
            quickSort(pivot + 1, end, K)

def swap(i, j):
    global A
    A[i], A[j] = A[j], A[i]  # ✅ 간결한 스왑

def partition(start, end):
    global A
    
    if start == end:    # 원소가 1개만 있을 때
        return start

    median = (start + end) // 2
    swap(start, median) # 중앙값을 맨 앞으로 옮겨 피봇으로 설정
    pivot = A[start]
    i = start + 1
    j = end

    while i <= j:
        while j >= start and A[j] > pivot:  # ✅ 인덱스 에러 방지, 오른쪽에서 피봇보다 작은 값 탐색
            j -= 1
        while i <= end and A[i] < pivot:  # ✅ 인덱스 에러 방지 => 아마 인덱스에서 오류가 난거같다.
            i += 1                        # 왼쪽에서 피봇보다 큰 값 탐색
        if i <= j:                         # 값이 엇갈리지 않았으면 swap
            swap(i, j)
            i += 1
            j -= 1

    swap(start, j)  # ✅ 피벗을 최종 위치로 이동
    return j  # ✅ 올바른 피벗 위치 반환

quickSort(0, n - 1, k - 1)
print(A[k - 1])
