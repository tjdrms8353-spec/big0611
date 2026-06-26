# 세트(set)
# 생성
fruit_set = {'사과','바나나','오렌지'}
print(fruit_set)
# 1. 중복 불가능
fruit_set = {'사과','바나나','오렌지','사과','바나나'}
print(fruit_set)

# 2. 선택(인덱싱) 불가능
# fruit_set[1]
# TypeError: 'set' object is not subscriptable (첨자에러)

# 3. 추가 (추가되는 위치,순서는 없다(랜덤) 그래서 인덱싱이 없다)
fruit_set.add('키위')
print(fruit_set)

# 확장
vegetable_set = {'당근','토마토','양파'}
fruit_set.update(vegetable_set)
print(fruit_set)

# 삭제
fruit_set.remove('양파')
print(fruit_set)

# (번외)clear
fruit_set.clear()
print(fruit_set)   # -> set()로 출력됨