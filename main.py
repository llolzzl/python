# # 주석을 사용하는 이유 코멘트 / 이 함수는 어떤 함수이다. history를 남김
#
# print("Hello Word!")
# print(1+5) # 더하기
# print(1*5) # 곱하기
# print(5/2) # 나누기
# print(5%2) # 나머지
#
# # 변수의 이름을 지정할 때 명확하게 지어주는 것이 좋음
# professor = "Sungchul Choi"
# print(professor) # professor이라는 변수에 Sungchul Choi를 담아 변수를 출력해줌
# a = 7 # 할당함 ( 변수에 숫자 7을 넣어줌)
# b = 5
# print(a+b) # a와 b의 값을 더함
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print("a+b") # 문자열로 a+b를 출력 시킴
#
# a = 1
# b = 1
# print(a,b) # 정수형
# print(type(a),type(b)) # 어떤 type인지 확인 가능
# a = 1.5
# b = 3.5
# print(a,b) # 실수형
# print(type(a),type(b))
# a = "ABC"
# b = "101010"
# print(a,b) # 문자형
# print(type(a),type(b))
# a = True
# b = False
# print(a,b) # 불리형
# print(type(a),type(b))
#
# print(2 ** 8) # 곱하기 두 번 : 제곱
# print(2 / 8)  # 자동으로 실수형 (몫+나머지)
# print(2 // 8) # 나누기 두 번 : 몫 값 나머지값을 제외한 몫만 확인 가능
#
# a += 1 # 증가 연산
# print(a)
# a = 1
# a = a+1
# print(a)
#
# b -=1 # 감소 연산
# print(b)
# b = 1
# b = b -1
# print(b)
#
# a = input() # 입력
# b = input()
# print(int(a)+int(b))
# # print(type(a))
#
# num1 = int(a)
# num2 = int(b)
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1**num2)
# print(num1//num2)
#
# a= 20
# b= '10'
# print()
#
#
# print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
# print("변환하고 싶은 섭씨온도를 입력하세요.")
#
# celsius = input()
# fahrenheit = float(celsius)*1.8+32
# print('섭씨온도 : ', float(celsius))
# # print(f"사용자가 입력한 섭씨 온도 : {celsius} 입니다.")
# # print(f"섭씨온도" + celsius + "입니다") << 비효율적
# print('화씨온도 : ', float(fahrenheit))
# print(f"변환한 화씨 온도 : {fahrenhit} 입니다.")

#
# colors = ['red', 'blue', 'green']
# print(colors[0])
# print(colors[1])
# print(colors[2])
# print(len(colors)) # 리스트 길이 확인
#
# a = 'red'
# b = 'blue'
# c = 'green'
# colors = [a, b, c] # 변수로 지정해서 넣을 수 있음
#
# numbers = [5, 6, 7, 8] # 숫자 리스트도 가능

# cities = ['서울', '부산', '인천', '대구', '광주', '울산', '수원']
# print(cities[0:6]) # 리스트 인덱스는 0부터 시작 / 이전 순서까지 / 0부터 6번째 전까지
# print(cities[3])
# print(cities[5:]) # 5부터 끝까지 / 앞 또는 뒤에 순서를 안썼을 경우 처음부터 또는 마지막까지
# print(cities[:5]) # 처음부터 5번째 전까지
# print(cities[-1]) # - 붙일 경우 뒤에서부터 순서대로 -1 >> 뒤에서 첫번째

# 리스트 연산
# color1 = ['red', 'blue', 'green']
# color2 = ['orange', 'black', 'white']
# print(color1+color2)
# total_color = color1+color2
# print(len(color1))
# print(len(total_color))
# print(color1*2) # color1 리스트 2회 반복
# print('blue' in color2) # color2 변수 안에 문자열 'blue' 종재 여부 반환

# color = ['red', 'blue', 'green']
# color.append('white') # 리스트에 white 추가
# print(color)
# color.extend(['black','purple']) # 리스트에 새로운 리스트 추가
# print(color)
# color.insert(0,'orange') # 0번째 위치에 orange 추가
# print(color)
# color.remove('red') # 리스트에 red 삭제
# print(color)

# # 인덱스의 재혈당과 삭제
# color = ['red', 'blue', 'green']
# color[0] = 'orange'
# print(color)
# del color[0]
# print(color)
#
# # 패킹과 언패킹
# t = [1, 2, 3] # 1, 2, 3 을 변수 t에 패킹
# a, b, c = t # t에 있는 값 1, 2, 3을 변수 a, b, c에 언패킹
# print(t, a, b, c)
#
# a_list = [1, 2, 3]
# b_list = [4, 5, 6]
# c_list = [a_list,b_list]
# print(c_list)
# print(c_list[0])
# print(c_list[1])
#
# kor_score = [49, 79, 20, 100, 80]
# math_score = [43, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
# midterm_score=[kor_score, math_score, eng_score]
# math_score[0] = 1000
# print(midterm_score)
# print(math_score)
# print(midterm_score[1][3]) # 두 번째 요소에 세 번째 값

# print("I eat %d apples"%3) # 포맷팅이랑 비슷 하지만 한개만 출력 할때는 이렇게 적어도 됨
# print("I eat %s apples"%'five')
# number = 3
# print("I eat %d apples"%number)
# print("I eat %0.2f apples"%1.5)
# print('%10s' % 'hi') # 공백 주기
# print('%1-0sjane' % 'hi')

# a= 300
# b= 300
# print(a is b)
# print(a == b)

# print("성적표")
# python1 = int(input())
# python2 = int(input())
# python3 = int(input())
# python4 = int(input())
# python5 = int(input())
#
# print("----------------------------------------")
# print("이민지", "85", "80", "65", "python1", "100")
# print("이소연", "85", "80", "65", "python1", "100")
# print("이준영", "85", "80", "65", "python1", "100")
# print("하태균", "85", "80", "65", "python1", "100")
# print("황윤정", "85", "80", "65", "python1", "100")
# print("----------------------------------------")

import pandas as pd

score = [["85", "80", "65", "python1", "100"],
         ["85", "75", "95", "python2", "98"],
         ["85", "90", "80", "python3", "51"],
         ["85", "85", "90", "python4", "90"],
         ["85", "95", "80", "python5", "100"]]

df = pd.DateFrame(score, columns = ["국어", "영어", "수학", "파이썬", "C언어"], inde= ["이민지", "이소연", "이준영", "하태균", "황윤정"])
print(df)