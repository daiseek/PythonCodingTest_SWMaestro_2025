# 수들의 합 5 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	32 MB	28690	13825	10204	48.723%
# 문제
# 어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 
# 당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서, 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다. 
# 이때, 사용하는 자연수는 N이하여야 한다.

# 예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 
# 반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지가 있다.

# N을 입력받아 가지수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 정수 N이 주어진다.

# 출력
# 입력된 자연수 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 출력하시오


# 문제 분석
# 여기서 N의 최대값이 매우 크므로, 시간복잡도를 O(N)으로 풀어야 한다.
# 이때 투포인터를 이용할 수 있다.

# 과정
# 1. N을 입력받고, 리스트에 1부터 N까지의 자연수를 저장한다.
# 2. 투포인터를 이용해 연속된 자연수의 합을 구한다.
# 즉, start_inx, end_inx를 투포인터로 이용하는데
# [start, end]범위 내 자연수들이 연속된 수이다.
# 3. 범위 내에서 연속된 수들을 합했을 때 N이 된다면, ok!

# 여기서 start_inx를 오른쪽으로 이동 => 범위에서 가장 작은 수를 제거
# end_inx를 오른쪽으로 이동 => 범위에서 가장 큰 수를 추가


# 투포인터 이동 규칙
# 1. sum > N; sum -= start_inx; start_inx++;
# sum이 더 크면, start_inx를 왼쪽으로 이동시킨 후 1을 더한다.
# => 가장 작은 수가 빠지면서 sum이 감소

# 2. sum < N; end_inx++; sum += end_inx;
# sum이 더 작으면, end_inx를 오른쪽으로 이동시킨 후 1을 더한다.
# => 가장 큰 수가 추가되면서 sum이 증가

# 3. sum == N; end_ix++; sum += end_inx; count++;
# sum이 N과 같으면, end_inx를 오른쪽으로 이동시킨 후 1을 더하고 count를 1 증가시킨다.
# 이때 count는 연속된 수를 더했을 때 경우의 수를 뜻한다.

# Q. sum += end_inx를 하는 이유가 뭘까?
# 다음 경우를 따지기 위함!, 
# 즉, sum += end_inx를 했을 때 sum == N 인지 따지기 위함이다.

# Cor Q. sum += end_inx를 하면, sum != N이 되는거 아닌가?
# A. 새로운 sum을 찾기위한 과정이다!
# step1. sum += end_inx으로 인해 sum이 증가
# step2. sum > N이므로 start_inx가 증가된다. 즉, start_inx += 1
# step3. 투포인터 이동 규칙에 따라서 알고리즘이 작동한다.


# 솔루션 슈도코드
# n 입력받을 정수값
# count, start_inx, end_inx, sum 사용할 변수들 초기화
# count = 1 => N 자기 자신을 연속된 수로 본다!

# while end_inx !=n: end_inx가 n까지 도달하지 않을 때까지 반복
#     if sum > n: sum -= start_inx; start_inx += 1      앞서 설명한 규칙1
#     elif sum < n: end_inx += 1; sum += end_inx        앞서 설명한 규칙2
#     else: end_inx += 1; sum += end_inx; count += 1    앞서 설명한 규칙3

# print(count) 경우의 수 출력


# Code
n = int(input())
count, start_inx, end_inx, s = 1, 1, 1, 1

while end_inx !=n:
    if s == n:
        count += 1 
        end_inx += 1 
        s += end_inx
        
    elif s > n:
        s -= start_inx
        start_inx += 1 
        
    else:
        end_inx += 1 
        s += end_inx
        
print(count)


# 해설
# 1. 투 포인터의 규칙에 따라서 while 이하를 작성함.

# Keypoints
# 1. 투 포인터를 이용해 연속된 자연수의 합을 구하고, 그 값이 특정 수에 맞는지 확인할 수 있다.
# 2. 파이썬에서는 전위표기, 후위표기로 값을 증감시킬 수 없다.