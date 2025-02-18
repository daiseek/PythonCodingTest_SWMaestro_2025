# 04-3 삽입 정렬
# 정렬된 데이터 범위에 정렬되지 않은 데이터를 삽입하는 방식으로 동작
# 시간 복잡도는 O(n^2)으로 느린 편이지만, 구현하기 쉽다.

# 과정)
# 1) 현재 index에 있는 데이터를 선택
# 2) 현재 데이터가 정렬된 위치에서 삽입될 위치 탐색
# 3) 삽입할 위치와 해당 데이터가 있는 위치까지 shift 연산 수행
# 4) 삽입 위치에 현재 데이터를 넣고, index++ 연산 수행
# 5) 전체 데이터 인덱스가 끝날 때까지 반복 -> 선택할 데이터가 없을 때까지

# - 적절한 삽입 위치를 탐색하는 부분에서 이진 탐색 binary search 같은 탐색 알고리즘을 사용하면 시간 복잡도를 줄일 수 있다.
