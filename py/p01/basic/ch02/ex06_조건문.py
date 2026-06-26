# 실행문
# 조건문
'''
 탭키와 스페이스바를 섞어쓰면 X (보통 탭키로 많이 사용함)
 들여쓰기(indent)
 1) if 조건식:
    수행문1


 2) if 조건식:
    수행문1
 else
    수행문2
 
 조건식은 결과가 True 또는 False
 비교연산(>, <, >=, <=, ==, !=),
 논리연산(and, or, not)의 결과는 True 또는 False
 '''
# 문제1. 기온이 0도 보다 높으면 "아이스아메키라노를 출력하는 프로그램"
today_temp = 30
if today_temp > 0:
    print("문제1:","아이스 아메리카노")  
# 파이썬은 들여쓰기를 꼭 해야한다 
# :을 사용했으면 수행문이 있어야하는데 없기 때문



# 문제2. 기온이 0ºC보다 높으면 ‘아이스 아메리카노’를 출력하고,
#  그렇지 않은 경우에는 
# ‘따뜻한 아메리카노’를 출력하는 프로그램을 만들어 보세요.
today_temp = -10
if today_temp > 0:
    print("문제2:","아이스 아메리카노")
else:
    print("문제2:","따뜻한 아메리카노")

'''
 if 조건식1:
     수행문1
 elif 조건식2:
     수행문2
 elif 조건식3:
      수행문3
 '''
'''
else:
    수행문3
'''

#문제3.기온이 0ºC보다 높으면 ‘아이스 아메리카노’, 
# 기온이 0ºC이면 ‘미지근한 아메리카노’, 
# 나머지 경우에는 ‘따뜻한 아메리카노’를 
# 출력하는 프로그램을 만들어 보세요.
today_temp = 30
if today_temp > 0:
    print("문제3:","아아")
elif today_temp == 0:
    print("문제3:","디아")
else:
    print("문제3:","뜨아")

# 중첩if

# 문제4. 날씨가 맑은 날인 경우, 기온이 0ºC보다 높으면 ‘아이스 아메리카노’, 
# 기온이 0ºC이면 ‘미지근한 아메리카노’, 
# 나머지 경우에는 ‘따뜻한 아메리카노’를 출력하고
# 날씨가 맑지 않은 경우,‘카푸치노’를 출력하는 프로그램을 만들어 보세요.

weather = "비"
today_temp = 30

if weather == "맑음":
    if today_temp > 0:
        print("문제4:","아아")
    elif today_temp == 0:
        print("문제4:","디아")
    else:
        print("문제4:","뜨아")
else:
    print("문제4:","먹지마!")

math_score = 80
eng_score = 100

if eng_score >= 90 and math_score >= 90:
    print("문제5:","용돈인상")
elif eng_score <= 80 and math_score <= 80:
    print("문제5:","용돈삭감")
else:
    print("문제5:","동결")


math_score = 80
eng_score = 100

if eng_score >= 90 or math_score >= 90:
    print("문제6:","용돈인상")
elif eng_score <= 80 or math_score <= 80:
    print("문제6:","용돈삭감")
else:
    print("문제6:","동결")