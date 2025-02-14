# 평균 1546
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	318062	161808	130543	50.331%
# 문제
# 세준이는 기말고사를 망쳤다. 
# 세준이는 점수를 조작해서 집에 가져가기로 했다. 
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 
# 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

# 출력
# 첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10^-2 이하이면 정답이다.


# My code
nums = input()
scores = list(map(int, input().split()))

score_sum = 0
score_mean = 0
score_max = 0

for i in scores:
    if score_max < i:
        score_max = i
        
for i in scores:
    score_sum += int(i)/score_max*100
    score_mean = score_sum/int(nums)
    
print(score_mean)
    

# 노트
# 1. list와 map 함수를 이용해 요소들을 int형으로 배치했다.
# 이때 split메소드로 띄어쓰기에 따라 구분지었다.
# int형으로 이미 요소들이 변환되었기에 for문에서 int(i)로 변환할 필요가 없다.


# Solution code
n = input()
myScores = list(map(int, input().split()))
myMax = max(myScores)
mySum = sum(myScores)
myMean = mySum/myMax*100/int(n)

print(myMean)

# 설명
# 1. map() 함수
# map(함수, 리스트) 형태로 사용


# Q. 첫 인자로 뭐가 올 수 있는거지?
# A.

# 1. 사용자 정의 함수
# def square(x):
#     return x * x
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)

# 2. lambda 함수
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x * x, numbers)

# Note1. lambda 함수는 이름이 없는 함수로, 한 줄로 함수를 표현할 수 있다.
# lambda 매개변수1, 매개변수2, ... : 표현식

# 3. 내장 함수
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(str, numbers)
# 자료형(내장 함수)를 통해 요소마다 형변환

# 4. 클래스
# class MyClass:
#     def double(self, x):
#         return x * 2

# obj = MyClass()
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = map(obj.double, numbers)


# 2. split() 메소드
# 문자열을 특정 문자를 기준으로 나누어 리스트로 반환한다.
# 문자를 쓰지 않으면 공백(띄어쓰기)를 기준으로 나눈다.
# EX.
# text = "apple,banana,cherry"
# fruits = text.split(',') => ['apple', 'banana', 'cherry']


# Keywords
# 1. map(함수, 반복가능한객체)를 통해 인덱스에 매핑시킬 수 있다.
# 이때 list()로 묶지 않으면, map 객체가 반환된다.

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x * x, numbers)

# # map 객체는 반복 가능하지만 리스트가 아님
# print(squared_numbers)  # 출력: <map object at 0x...> -> 메모리주소출력

# Note. at 0x...은 map 객체의 메모리주소이다.
# 즉, 현재 squared_numbers는 어떠한 데이터가 아닌 map객체를 의미
# 이를 list()로 묶어주면, map 함수를 사용하여 연산된 요소들로 이루어진 리스트가 반환된다.


# map 객체를 반복하여 요소에 접근할 수 있음
# for num in squared_numbers:
#     print(num)  # 출력: 1, 4, 9, 16, 25

# 이를 쉽게 사용하기 위해 list()로 묶어준 것!


# 2. split() 메소드를 통해 문자열을 나눌 수 있다.