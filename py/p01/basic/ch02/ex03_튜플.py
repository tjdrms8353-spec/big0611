# 튜플(tuple)
fruit_tuple = ('사과','바나나','오렌지')
print(fruit_tuple)
# 줄복사방법 : 쉬프트 + 알트 + 위아래 방향키
# 위치이동 : 알트 + 방향키
fruit_tuple = ('사과','바나나','오렌지','사과','바나나')
print(fruit_tuple)

# 선택
# 인덱싱
print(fruit_tuple[1])

# 수정(Update)할 수 없음
# fruit_tuple[1] = '키위'
# TypeError: 'tuple' object does not support item assignment 
# 위와같은 에러가 나옴 Type이 잘못되었다.

# 추가 불가능
# fruit_tuple.append('수박')
# AttributeError: 'tuple' object has no attribute 'append'
# 위와같은 에러가 나옴 (속성에러(매서드에러))

# 삭제 안됨
# fruit_tuple.remove('사과')
# AttributeError: 'tuple' object has no attribute 'remove'
# 추가와 똑같은 에러

# 타입 변환 (튜플은 수정,삭제 등이 안되기때문에 타입을 변환하게되면 수정가능하다)
# 기본형 : int(), float(), str(), bool()
# 컨테이너형 : list(), tuple(), set(), dict()
# 튜플을 리스트로 변환
print('32:',fruit_tuple)
fruit_list = list(fruit_tuple)
fruit_list.append('수박')  # 수박을 추가한다
fruit_list.remove('사과')  # 사과를 삭제한다
fruit_list[1] = '키위'     # 1번을 키위로 바꿔 지정한다
print('35:',fruit_list)
# 리스트를 다시 튜플로 변환
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)

