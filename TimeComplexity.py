# 01-1. 알고리즘의 척도, 시간복잡도

# 실제 시간 복잡도는 3가지 유형으로 나뉜다.
# 1) 빅-오메가: 최선의 경우에서 연산 횟수를 나타냄
# 2) 빅-오: 평균적인 경우에서 연산 횟수를 나타냄
# 3) 빅-세타: 최악인 경우에서 연산 횟수를 나타냄

# 코딩 테스트에서는 빅-오 표기법을 사용한다.
# 또한, 시간 복잡도를 판단할 때는 최악인 경우를 고려해야 한다.

# 시간 복잡도는 대게 근사값으로 축약된다.
# 연산 횟수는 1초에 2000만 번 연산하는 것을 기준으로 한다.
# 주어지는 수 n에 따라서 연산 횟수가 주어진 연산 시간을 넘지 않도록 알고리즘을 짜야 한다.

# 시간 복잡도를 계산할 때 중점이 되는 것
# 1) 상수는 제외한다
# 2) 반복문이 중첩될 수록 시간복잡도는 기하급수적으로 늘어난다.

# 가령, 단순하게 for문을 사용하여 코드를 짠다고 가정해보자
# 1) for문 1개를 이용
# 2) for문 3개를 이용
# 3) 이중 for문을 이용

# 여기서 1)과 2)는 시간 복잡도가 O(n)이다.
# 사실 2)번은 시간 복잡도가 O(3n)이지만, 상수는 제외하므로 O(n)이다.
# 3)번은 시간 복잡도가 O(n^2)이므로 연산 횟수가 훨씬 많음을 알 수 있다.

