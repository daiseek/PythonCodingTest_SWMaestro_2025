# 주몽
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	38835	18816	13391	47.012%
# 문제
# 주몽은 철기군을 양성하기 위한 프로젝트에 나섰다. 그래서 야철대장을 통해 철기군이 입을 갑옷을 만들게 하였다. 
# 야철대장은 주몽의 명에 따르기 위하여 연구에 착수하던 중 아래와 같은 사실을 발견하게 되었다.

# 갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다. 
# 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다. 
# 야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다. 
# 이러한 궁금증을 풀어 주기 위하여 N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 
# 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 재료의 개수 N(1 ≤ N ≤ 15,000)이 주어진다. 
# 그리고 두 번째 줄에는 갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 주어진다. 
# 그리고 마지막으로 셋째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다. 
# 고유한 번호는 100,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 갑옷을 만들 수 있는 개수를 출력한다.


# My code 1
n = int(input())
m = int(input())
ingredients = list(map(int, input().split()))
count = 0
s = 1

ingredients.sort()

for start_inx in range(m):
    for end_inx in range(m):
        if s == m:
            count += 1
            s += end_inx
        elif s > m:
            pass
        else:
            pass
        
count -= 1
print(count)

# 결과: 시간초과
# 추측: 이중 for문


# My code 2 - 오답
n = int(input()) 
m = int(input())  
ingredients = list(map(int, input().split())) 

ingredients.sort() 

start_inx, end_inx = 0, 0  
count = 0
s = 0  

while end_inx < n:
    if s == m:
        count += 1  
        s -= ingredients[start_inx]  
        start_inx += 1  
    elif s < m:
        if end_inx < n:  
            s += ingredients[end_inx]
            end_inx += 1
    else:  
        s -= ingredients[start_inx]  
        start_inx += 1  

print(count)


# Solution code
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()

count = 0
start_inx = 0
end_inx = n-1

while start_inx < end_inx:
    if ingredients[start_inx] + ingredients[end_inx] < m:
        start_inx += 1
    elif ingredients[start_inx] + ingredients[end_inx] > m:
        end_inx -= 1
    else:
        count += 1
        start_inx += 1
        end_inx -= 1

print(count)


# 오답노트
# 1. 갑옷 재료가 2개라는 점을 지나침. 연속된 숫자로 m을 만들어야 하는줄 알았음
# 따라서 A[start_inx] + A[end_inx] == m 이라는 조건으로 고려해야함


# 해설
# 1. 재료 리스트를 int형 요소로 받아서 sort()메소드로 정렬

# 2. 반복 수행하는 과정
# step1. start_inx = 0 일때 end_inx = n-1 일때까지 반복, 
# case1) ingredients[start_inx] + ingredients[end_inx] = m 일때 count += 1
# case2) ingredients[start_inx] + ingredients[end_inx] < m 일때 start_inx += 1
# case3) ingredients[start_inx] + ingredients[end_inx] > m 일때 end_inx -= 1 

# 해당 알고리즘은 시간복잡도를 계산해보자
# 리스트 정렬에서 O(nlogn)
# while문에서 O(n)
# 따라서 O(nlogn) + O(n) = O(nlogn)이다.

# Q. 리스트 정렬의 시간복잡도가 O(nlogn)인 이유는?
# A. 효율적인 정렬의 시간복잡도는 O(nlogn)이다
# 여기서 n은 리스트의 길이, logn은 비교횟수를 의미한다.
# logn은 구체적으로 각 요소를 정렬 위치에 삽입, 병합할 때 필요한 비교 횟수이다.
# 이는 이진 트리의 높이와 관련있다.


