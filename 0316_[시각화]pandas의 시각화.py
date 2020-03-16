#기본 패키지 세팅 ~머신러닝까지 (복붙하고 시작하기)   ============================

import numpy as np #수치연산, 선형대수, ndarray라는 자료 구조를 가진 패키지
import pandas as pd #Series, DF 자료구조, 기술통계, 간단한 시각화를 가진 패키지
import seaborn as sns #샘플데이터와 시각화
import matplotlib.pyplot as plt #그래프 그리기 패키지
#그래프의 음수 사용을 위한 설정
plt.rcParams['axes.unicode_minus'] = False

#그래프 한글처리 패키지
from matplotlib import font_manager, rc
import platform
if platform.system() == 'Windows': #윈도우즈라면
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin': #매킨토시(MacOS)라면
    rc('font', family='AppleGothic')

from sklearn import preprocessing #데이터 전처리 패키지
#sklearn : 데이터셋, 전처리, 머신러닝용 패키지

#지도 시각화 패키지
import folium

#수학 관련 패키지
import math

#========================================================================

"""
s = pd.Series([1,2,3,4,5,6,7,8,9,10]) #1-1. 시리즈를 생성
print(s)

s.plot()
plt.show() #1-2. matlplotlib의 plot 메소드를 사용할거면 show 메소드를 꼭 호출 해야 함

s = pd.Series([1,2,3,4,5,6,7,8,9,10], index=pd.date_range('2020-01-01', periods=10))
# 1-3.Series를 만들때, index를 날짜로 만드는 방법
print(s)
s.plot()
plt.show()


#판다스로 그래프 그리기 ========================================================================

data_set = np.random.rand(10,3) #2-1. 10행 3렬의 random한 값들로 구성된 행렬을 만들어줘
#print(data_set)
df = pd.DataFrame(data_set)
#print(df) #2-2. 상단에서 만든 data_set 행렬을 판다스의 데이터프레임으로 변화

#3. 막대 그래프 그리기
df.plot(kind='bar') #cf. pandas는 kind에 원하는 그래프를 넣어주는 형태로 만든다.
plt.show()

#cf. 기본값은 선 그래프로 line. barh, pie, scatter, hist


#영역 그래프 그리기 ========================================================================
df.plot(kind='area', stacked = False) #4-1. area로 넣으면 영역 그래플 그려준다.
#위의 값이 아래 값을 덮어버리면 stacked = False로 하면 모두 보인다.
plt.show() 


#데이터프레임으로 그리기 ========================================================================
grade_num = [5, 14, 12, 3]
students = ['A', 'B', 'C', 'D']
num = [0, 1, 2, 3]

#4-1. 데이터 프레임 만들기
df = pd.DataFrame(grade_num, index=students, columns=['students'])
print(df)

#4-2. 막대 그래프 그리기
#cf> df.plot(kind='bar') #이렇게 바로 할 수도 있는데.. 부가 옵션을 설정하려면 객체를 하나 만들어 주는게 좋다.
grade_bar = df.plot.bar(grid=True) #격자가 나타남
grade_bar.set_xlabel('학점') #x축 이름 설정하기
grade_bar.set_ylabel('학생수') #y축 이름 설정하기
grade_bar.set_title('학점별 학생수 막대 그래프')
plt.show()


#산점도 그리기 ========================================================================

temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100]

dict_data = {'기온' : temperature, '판매량' : Ice_cream_sales}
df_ice_cream = pd.DataFrame(dict_data) #5-1. 별다른 설정이 없으면 dict 데이터의 key값이 컬럼이 됨
print(df_ice_cream)

df_ice_cream.plot.scatter(x='기온',y='판매량', title='기온과 아이스크림 판매')  #5-2. 바로 컬럼명을 x,y에 써주면 된다.
plt.show()
"""

#히스토그램 그리기 ===================================================================

math = [76,82,84,83,90,86,85,92,72,71,100,87,81,76,94,78,81,60,79,69,74,87,82,68,79]
df_math = pd.DataFrame(math, columns = ['Student'])
math_hist = df_math.plot.hist(bins=8, grid = True) #6-1. bins는 기본값이 10임. 막대 수 조정하고 싶으면 수동으로 넣어주기.
math_hist.set_xlabel('시험 점수')
math_hist.set_ylabel('frequency')
math_hist.set_title('수학 시험의 히스토그램')
plt.show()