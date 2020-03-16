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

#1. line_graph 그리기

x = [1,2,3,4,5]
y = [1,4,5,7,3]

plt.xlabel('x축')
plt.ylabel('y축')

#1-1. 크기를 설정
plt.figure(figsize=(10,6))
#1-2. plot안에 x,y 매개변수를 넣고 색상 매개변수 color로 선 색깔 바꾸기
#plt.plot(x,y, color='red')


# plt plot의 여러가지 버전
# plt.plot(x,y, 'r-') #빨간색 선그래프 약어
# plt.plot(x,y, 'ro') #ro = 선은 잇지 않고 포인트만 찍기
# plt.plot(x,y, 'rv') # ▼ 모양 그래프
# plt.plot(x,y, 'r>') # ▶ 모양 그래프
# plt.show()


#2. dashed-line graph 그리기
x = [0,1,2,3,4,5,6]
y = [1,4,5,6,7,8,10]

plt.figure(figsize=(10,5))
plt.plot(x,y, color='green', linestyle='dashed',marker='>',markerfacecolor='blue',markersize=10)
#2-1. linsestyle 옵션에 dashed를 추가하면 점선 그래프를 그림
#2-2. marker = 'o'를 추가하면 x,y가 만나는 지점을 o로 표시를 함. 옵션참고 : o, v, >
#2-3. markerfacecolor = 마커의 색상
#2-4. markersize = 마커 크기 조정
plt.show()