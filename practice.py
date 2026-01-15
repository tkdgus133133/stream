import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime as dt
import datetime

st.title('이것이 타이틀이다.')
st.header('이것이 헤더이다.')
st.subheader('이것이 서브헤더이다.')
st.text('이것이 일반 텍스트이다.')

st.title('스마일 : 😊')

st.caption('이것이 캡션이다.')
st.markdown('이것이 **마크다운** 이다.')    

# 코드표시
sample_code = '''
def hello():
    print("Hello, Streamlit!")'''
st.code(sample_code, language='python')

st.markdown('xxxxx :green[초록색]으로 변경하고, :blue[뭐] 볼드체 설정가능')
st.markdown(':green[$\sqrt{x^2+y^2}=1$] 같은 수식도 지원')

#dataframe 생성
dataframe = pd.DataFrame({
    'first column' : [1,2,3,4,],
    'second column' : [10,20,30,40,]
})
#테이블출력
st.table(dataframe)  # 정적인 데이터프레임
#메트릭
st.dataframe(dataframe)  # 인터랙티브한 데이터프레임
st.metric('온도', 35, delta=5)  
st.metric(label='삼성전자',value='140.000',delta='+3800')
#컬럼으로 영역 나누어 표기
col1, col2, col3 = st.columns(3)
col1.metric(label='USD',value='1,250',delta='-15')
col2.metric(label='EUR',value='1,450',delta='+20')
col3.metric(label='JPY',value='1,100',delta='0')

#버튼클릭

button = st.button('버튼을 눌러주세요')
if button:
    st.write(':blue[버튼]이 눌렸습니다.')

agree = st.checkbox('체크박스를 눌러주세요')
if agree:
    st.write('체크박스가 선택되었습니다.')  

#라디오버튼
import streamlit as st

# 올바른 문법
mbti = st.radio(
    '당신의 MBTI는?', 
    ['ENFP', 'INFP', 'INTJ', 'ISTJ'], 
    index=2
)
if mbti == 'ENFP':
    st.write('당신은 모험을 좋아하는 사람입니다.')
elif mbti == 'INFP':
    st.write('당신은 열정적인 중재자입니다.')
elif mbti == 'INTJ':
    st.write('당신은 전략가입니다.')

#셀렉트박스
color = st.selectbox('좋아하는 색은?',('빨강','파랑','초록'))
st.write(f'당신이 좋아하는 색은 {color}입니다.')

#멀티셀렉트박스
hobbies = st.multiselect(
    '당신의 취미는?',
    ['독서', '운동', '영화', '음악']
)
st.write(f'당신의 취미는 {", ".join(hobbies)}입니다.')

#슬라이더
age = st.slider(
    '당신의 나이는?',
     0,100,25
)
st.write(f'당신의 나이는 :blue[{age}]세입니다.')

value = st.slider(
    '범위의 값을 다음과 같은 범위로 설정',
    0.0,100.0,(25.0,75.0)
)
st.write(f'선택된 값은 :green[{value}]입니다.')       # 배만들때


#날짜선택
start_time = st.slider(
    '약속 언제 잡을래?',
    min_value=dt(2026,1,1,0,0),
    max_value=dt(2026,1,31,0,0),
    value=dt(2026,1,15,0,0),
    step=datetime.timedelta(days=1),
    format = 'yyyy-MM-DD'
)
#텍스트입력
# 텍스트입력
title = st.text_input(
    label='가고싶은곳??', 
    value='여기에 입력하세요', 
    placeholder='홍콩, 부산'
)
st.write(f'당신의 제목은 :blue[{title}]입니다.')
#숫자입력
number = st.number_input(
    label='좋아하는 숫자는?',
    min_value=0,
    max_value=120,
    value=25,
    step=1
)
st.write(f'당신이 좋아하는 숫자는 :green[{number}]입니다.')

#파일다운로드 버튼
st.download_button(
    label='다운로드',
    data=dataframe.to_csv().encode('utf-8'),
    file_name='sample.txt',
    mime='text/plain'
)



import streamlit as st
import random  # 필수! 랜덤 모듈을 불러와야 합니다.

st.title('로또 번호 생성기')

def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)
    return sorted(lotto)

button = st.button('로또 번호 생성')

if button:
    # 5세트의 번호를 생성합니다.
    for i in range(1, 6):
        # f-string을 사용하여 제목과 번호를 깔끔하게 출력합니다.
        # subheader 안에는 문자열만 들어가야 하므로 아래처럼 작성하세요.
        numbers = generate_lotto()
        st.subheader(f'{i}번째 로또 번호: {numbers}') 
        st.write("---") # 구분을 위한 가로줄