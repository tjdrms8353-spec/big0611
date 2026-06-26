a = 5
print(a)

b = 3
print(b)

print(a + b)

c = '가나다'
print(c)

radio_freq = 107.9
print(radio_freq)

# 잘못된 변수명: 숫자로 시작
# 2var = '행복'
# SyntaxError: invalid decimal literal

# 잘못된 변수명: 공백 포함
# happy var = '행복'
# SyntaxError: invalid syntax

# 잘못된 변수명: 특수문자 포함(단, _는 허용)
# happyvar! = '행복'
# SyntaxError: invalid syntax

# 잘못된 변수명: 예약어 사용
# def = '행복'
# SyntaxError: invalid syntax

# 대소문자 구분
abc = 5
ABC = 'Apple'
# print() 내장함수의 인자의 수는 제한 없다
print(abc, ABC)

# 다중 변수 동시 선언
x, y, z = 'Apple', 'Banana', 'Carrot'
print(x, y, z)

# 변수명에 언더스코어(_) 사용
# 이는 주로 사용하지 않을 변수을 위한 자리 표시자로 사용됩니다.
_, var = 'Not use', 'Use'
print(_, var)

# 단일값의 다중 변수 선언
x = y = z = 'Same'
print(x, y, z)

# 단일값의 다중 변수 할당
x = y = z = '같은값'
print(x, y, z)