# 구간 합 구하기 4 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	145063	59522	43323	38.437%
# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

# 제한
# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 100,000
# 1 ≤ i ≤ j ≤ N

# 예제입력
# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5


# Soulution code
import sys
input = sys.stdin.readline
datas, queries = map(int, input().split())
dataList = list(map(int, input().split()))
sumList = [0]
temp = 0

for nums in dataList:
    temp += nums
    sumList.append(temp)
    
for query in range(queries):
    i, j = map(int, input().split())
    print(sumList[j]-sumList[i-1])


# 오답노트
# 1. sumList를 만들 생각을 하지 못함.
# 이중 for문을 이용하여 구간합을 처리하려고 했음.

# 해설
# 1.  sys 모듈: 파이썬 인터프리터와 상호작용하는 기능 제공
# sys.stdin.readline()은 input()보다 빠르게 동작한다.
# 저 코드를 빼니 시간초과가 떴다.

