# 수 정렬하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	230841	132769	90948	58.245%
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


# sort()메소드 이용 시
n = int(input())
nums = []
temp = 0

for i in range(n):
    temp = int(input())
    nums.append(temp)
    
nums.sort()

for i in range(n):
    print(nums[i])


# sort() 메소드를 이용해 풀 수도 있으나, 여기서는 버블 정렬을 이용해보자

# 슈도코드 작성
# n 정렬할 수의 갯수
# A 수를 저장할 리스트 선언, 입력 데이터 저장

# for i in 0 ~ n-1 반복:
#     for j in 0 ~ n-1 반복:
#         현재 A에서 1칸 오른쪽 리스트 값이 더 작으면 swap 연산

# A 리스트 요소들 출력


# Solution Code
n = int(input())
A = [0] * n

for i in range(n):  
    A[i] = int(input()) 
    
for i in range(n-1):    # 총 n-1번 정렬 기능을 반복
    for j in range(n-1-i):  # 정렬할 때마다 정렬된 부분(뒷 요소들)은 제외하고 정렬
        
        if A[j] > A[j+1]:   # 버블 정렬 원리에 따라 if문 작성
            temp = A[j]     # j번째 요소와 j+1요소를 바꿔야 할 때 
                            #기존 A[j]값을 임시로 temp에 저장
            A[j] = A[j+1]
            A[j+1] = temp
            
for i in range(n):
    print(A[i])