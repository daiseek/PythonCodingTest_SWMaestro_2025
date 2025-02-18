# 수 정렬하기 2
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	362079	112355	78759	31.463%


# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


# 손으로 풀기
step1. 정렬할 집합을 최소 길이로 나눈다.
예제에서 5개의 수가 주어졌으니 2, 2, 1로 나누었다.

step2. 나눈 집합마다 병합 정렬 실행
각 부분 집합마다 index를 지정하여 비교하며 정렬 리스트로 선언한 tempList에 추가한다.

[5, 4, 3, 2, 1]
1) set1 = [4,5], set2 = [2,3], set3 = [1]
2) tempList = []
set1[index1] = 5, set1[index2] = 4
set2[index1] = 3, set2[index2] = 2
set3[index1] = 1

3) set2와 set3를 병합정렬
tempList = [1,2,3]

4) set1도 마저 병합정렬
tempList = [1,2,3,4,5]



# 슈도코드
# 병합 정렬(start, end):
# start, end, median
# 병합 정렬(start, median)
# 병합 정렬(median+1, end)
# for i in range(start, end+1):
#     tempList에 저장

# index -> 앞 부분 집합 시작점
# index2 -> 뒷 부분 집합 시작점

# while index <= 중간점 and index2 <= 종료점:
#     양쪽 부분 집합에서 index가 가리키는 데이터를 비교 후 더 작은 수를 tempList에 추가
#     선택된 데이터를 가리키는 index를 오른쪽으로 한 칸 이동
#     반복문 끝난 후 남은 데이터 정리

# n 정렬할 수의 갯수
# A 정렬할 리스트 선언
# tempList 정렬된 임시 리스트 선언

# for n:
#     A에 append

# 병합 정렬 함수 실행
# 결과 출력



# Solution Code
import sys
input = sys.stdin.readline
print = sys.stdout.write

def mergeSort(start, end):
    if end - start < 1:
        return
    median = int(start + (end - start) / 2)
    mergeSort(start, median)
    mergeSort(median + 1, end)
    for i in range(start, end + 1):
        tempList[i] = A[i]
    k = start
    index1 = start
    index2 = median + 1

    while index1 <= median and index2 <= end:
        if tempList[index1] > tempList[index2]:
            A[k] = tempList[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tempList[index1]
            k += 1
            index1 += 1

    while index1 <= median:
        A[k] = tempList[index1]
        k += 1
        index1 += 1

    while index2 <= end:
        A[k] = tempList[index2]
        k += 1
        index2 += 1

n = int(input())
A = [0] * int(n+1)
tempList = [0] * int(n+1)

for i in range(1, n+1):
    A[i] = int(input())

mergeSort(1, n)

for i in range(1, n+1):
    print(str(A[i]) + '\n')