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

titanic = sns.load_dataset('titanic')
titanic.info()

fig = plt.figure(figsize=(15, 5)) # 그래프 크기 설정
ax1 = fig.add_subplot(1, 3, 1) # 1행 3열 - 1번째 그래프
ax2 = fig.add_subplot(1, 3, 2) # 1행 3열 - 2번째 그래프
ax3 = fig.add_subplot(1, 3, 3) # 1행 3열 - 3번째 그래프

"""
# x축, y축에 변수 핛당
sns.barplot(x='sex', y='survived', data=tit, ax=ax1)
# x축, y축에 변수 핛당하고, hue 옵션 추가하여 누적 출력순으로 출력
sns.barplot(x='sex', y='survived', hue='class', data=tit, ax=ax2)
# x축, y축에 변수 핛당하고, dodge=False 옵션으로 1개의 막대그래프로 출력
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=tit, ax=ax3)
# 차트 제목 표시
ax1.set_title('titanic survived - sex')
ax2.set_title('titanic survived - sex/class')
ax3.set_title('titanic survived - sex/class(stacked)')

plt.show()


# 빈도막대 그래프 ========================================================================

# 기본값 : palette='Set1' 로 색상 설정
sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1)
# hue 옵션에 'who' 추가 : who(man, woman, child) 각각 빈도 막대그래프 출력
sns.countplot(x='class', hue='who', palette='Set2', data=titanic, ax=ax2)
# dodge=False 옵션 추가 (축 방향으로 분리하지 않고 누적 그래프 출력)
sns.countplot(x='class', hue='who', palette='Set3', dodge=False, data=titanic, ax=ax3)
# 차트 제목 표시
ax1.set_title('titanic class')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(stacked)')
plt.show()



# 바이올린 그래프 ========================================================================

# 그래프 객체 생성 (figure에 4개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 10)) # 그래프 크기 설정
ax1 = fig.add_subplot(2, 2, 1) # 2행 2열 - 1번째 그래프
ax2 = fig.add_subplot(2, 2, 2) # 2행 2열 - 2번째 그래프
ax3 = fig.add_subplot(2, 2, 3) # 2행 2열 - 3번째 그래프
ax4 = fig.add_subplot(2, 2, 4) # 2행 2열 - 4번째 그래프

# 박스 그래프 - 기본값
sns.boxplot(x='alive', y='age', data=titanic, ax=ax1)
# 박스 그래프 - hue = 'sex' 변수를 추가하여 남녀 데이터를 구분하여 출력
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2)
# 바이올린 그래프 - 기본값
sns.violinplot(x='alive', y='age', data=titanic, ax=ax3)
# 바이올릮 그래프 - hue = 'sex' 변수를 추가하여 남녀 데이터를 구분하여 출력
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4)
plt.show()

# 조인 그래프 ========================================================================

# 조인트 그래프 - 산점도(기본값)
j1 = sns.jointplot(x='fare', y='age', data=titanic)
# 조인트 그래프 - 회귀선 : kind='reg'
j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic)
# 조인트 그래프 - 육각 그래프 : kind='hex'
j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic)
# 조인트 그래프 - 커널 밀집 그래프 : kind='kde'
j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic)


# ★ FacetGrid ===============================================
# who(man, woman, child), survived(0, 1)

sns.set_style('darkgrid')
#스타일에 들어갈 수 있는 조건 : darkgrid, whitegrid, dark, white, ticks

#조건 나누기 : 컬럼은 who로 행은 생존 여부로 나누겠다.
g= sns.FacetGrid(data=titanic,col='who', row='survived')

# 어떤 그래프로 출력할지 넣어준다.
g= g.map(plt.hist,'age')

plt.show()
"""

# ★ pairplot ===============================================

sns.set_style('darkgrid')

#분석에 쓸 데이터를 선택한다!
titanic_pair = titanic[['age','pclass','fare']]

g = sns.pairplot(data=titanic_pair)
plt.show()