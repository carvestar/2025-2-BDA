import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

# 한글 폰트 깨짐 처리
rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 상위 20게 국가명 영어 -> 한국어
country_map_top20 = {
    "United States of America": "미국",
    "India": "인도",
    "Germany": "독일",
    "United Kingdom of Great Britain and Northern Ireland": "영국",
    "Canada": "캐나다",
    "France": "프랑스",
    "Brazil": "브라질",
    "Poland": "폴란드",
    "Netherlands": "네덜란드",
    "Spain": "스페인",
    "Italy": "이탈리아",
    "Australia": "호주",
    "Russian Federation": "러시아",
    "Turkey": "튀르키예",
    "Sweden": "스웨덴",
    "Switzerland": "스위스",
    "Austria": "오스트리아",
    "Israel": "이스라엘",
    "Iran, Islamic Republic of...": "이란",
    "Pakistan": "파키스탄",
}

# Country 국가명 한글 변환
df_raw['Country'] = df_raw['Country'].map(country_map_top20).fillna(df_raw['Country'])

# 변환된 상태로 groupby
ds_data = df_raw.groupby('Country').size()

# 상위 20개 국가 시각화
ds_data.nlargest(20).plot.pie(figsize = (10, 10))
plt.tight_layout()
plt.show()