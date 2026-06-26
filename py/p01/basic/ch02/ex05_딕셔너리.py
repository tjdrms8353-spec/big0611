# 딕셔너리(dict)
'''
이름 = {
    '키' : 값
    'key' : alue
}
'''
# 생성
my_dict = {
    'name' : '해리',
    'age' : 27,
    'height' : 190,
    'weight' : 99.9
}
print(my_dict)

# 선택
print(my_dict.keys())     # '키'만 출력됨
print(my_dict['age'])     # '키'중에 age만 출력됨

# 수정(Update)
my_dict['age'] = 28
print(my_dict)       # 나이가 28 로 수정되어 출력됨

# 딕셔너리.update({키:값})
my_dict.update({'weight' : 100})
print(my_dict)       # weight 가 99.9 -> 100 으로 변경되어 출력됨

# 추가
my_dict.update({'address': '부산'})
print(my_dict)       # 부산이 추가되어 출려됨

# 삭제
# 딕셔너리.popitem() : 마지막 아이템 삭제
my_dict.popitem()
print(my_dict)       # 부산이 삭제되어 출력됨

# 딕셔너리.pop('키')
# 특정 '키'값 삭제
my_dict.pop('age')
print(my_dict)       # 'age'만 삭제되어 출력

# 딕셔너리.clear()
# 아이템 전부 삭제
# my_dict.clear
# print(my_dict)

# 키값까지 삭제
# del my_dict
# print(my_dict)