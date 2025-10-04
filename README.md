# Korea Temperature Time Series Data Visualization (2005–2024)
* 2005 ~ 2024년 20년간의 대한민국 지역별 기상 데이터를 전처리 및 분석하여 시각화하는 것을 목표로 합니다.
* 데이터는 [기상청 자료개방포털](https://data.kma.go.kr/cmmn/main.do)에서 수집하였으며, 이를 기반으로 지역별 기온 특성, 극한 기후 발생 패턴, 계절별 기상 변화를 탐색합니다.
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="400" />
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B0%95%EC%88%98%EB%9F%89_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="400"/>
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EC%A0%81%EC%84%A4%EB%9F%89_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="400"/>
</p>

## 📝 Overview

### 1. 데이터 수집

* 출처: [기상청 자료개방포털](https://data.kma.go.kr/cmmn/main.do)
* 기간: 2005-2024년
* 지역: 대한민국 전 지역
* 주요 변수
  
| 한글 | 영문 | 상세 |
| :--- | :--- | :--- |
| 지점 | `region_number` | 기상 관측소의 고유 번호입니다. |
| 지점명 | `region_name` | 기상 관측소의 이름 (예: 서울, 부산)입니다. |
| 일시 | `date` | 관측이 이루어진 날짜입니다. |
| 최저기온 시각(hhmi) | `min_temp_time` | 최저 기온이 기록된 시각 (시간:분)입니다. |
| 최고기온 시각(hhmi) | `max_temp_time` | 최고 기온이 기록된 시각 (시간:분)입니다. |
| 최대 순간풍속 시각(hhmi) | `max_instant_wind_time` | 최대 순간 풍속이 관측된 시각 (시간:분)입니다. |
| 최대 풍속 시각(hhmi) | `max_wind_time` | 최대 풍속이 관측된 시각 (시간:분)입니다. |
| 최대 순간 풍속 풍향(16방위) | `max_instant_wind_direction_16` | 최대 순간 풍속이 불었던 방향을 16방위로 나타낸 값입니다. |
| 최대 풍속 풍향(16방위) | `max_wind_direction_16` | 최대 풍속이 불었던 방향을 16방위로 나타낸 값입니다. |
| 평균기온(°C) | `avg_temp` | 해당 날짜의 24시간 평균 기온입니다. |
| 최저기온(°C) | `min_temp` | 해당 날짜에 기록된 가장 낮은 기온입니다. |
| 최고기온(°C) | `max_temp` | 해당 날짜에 기록된 가장 높은 기온입니다. |
| 일강수량(mm) | `daily_rainfall` | 해당 날짜의 24시간 동안 내린 비의 총량입니다. |
| 최대 순간 풍속(m/s) | `max_instant_wind_speed` | 3초간의 평균 풍속 중 가장 큰 값으로, 돌풍에 해당하는 풍속입니다. |
|최대 순간 풍속 풍향|`max_instant_wind_direction`|최대 순간 풍속이 불었던 방향의 값입니다.
|최대 풍속 풍향|`max_wind_direction`|최대 풍속이 불었던 방향의 값입니다.
| 최대 풍속(m/s) | `max_wind_speed` | 10분간의 평균 풍속 중 가장 큰 값입니다. |
| 평균 풍속(m/s) | `avg_wind_speed` | 해당 날짜의 24시간 동안의 평균 풍속입니다. |
| 최소 상대습도(%) | `min_relative_humidity` | 해당 날짜에 기록된 가장 낮은 상대 습도입니다. |
| 평균 상대습도(%) | `avg_relative_humidity` | 해당 날짜의 24시간 평균 상대 습도입니다. |
| 합계 일조시간(hr) | `total_sunshine_hours` | 해당 날짜에 태양이 비춘 총 시간입니다. |
| 일 최심신적설(cm) | `daily_max_new_snowfall` | 해당 날짜에 새로 쌓인 눈의 깊이 중 가장 깊은 값입니다. |
| 일 최심적설(cm) | `daily_max_snowfall` | 해당 날짜에 지면에 쌓인 눈의 깊이 중 가장 깊은 값입니다. |

### 2. 데이터 전처리
>**구체적인 전처리 과정 및 코드는 [<📂KoreaTemp_preprocessing.ipynb>](https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/main/src/KoreaTemp_preprocessing.ipynb) 파일에서 확인할 수 있습니다**
* 데이터 병합
  1. 기상청 데이터의 region_number 컬럼(기상관측소 지역 번호)을 기준으로, 해당 지역에 대응하는 행정구역명(예: 서울특별시, 경기도)을 신규 컬럼으로 매핑
  2. 지역 번호와 행정구역 간 매핑 정보가 포함된 행정구역 참조 데이터(region.csv)와 병합 작업을 수행
    
* 결측치 처리
  
  1. 평균 기온 → 최저/최고 기온 평균값으로 보정
  2. 강수량, 적설량 → 결측 시 0으로 대체
  3. 40% 이상 결측된 일사량, 전운량, 충하층운량 총 3개의 컬럼 삭제
  4. 일조량 → 랜덤포레스트 기반 예측치로 대체
     
* 이상치 처리
  1. 풍향 데이터에서 음수 및 360° 이상 값 제거
    
* 범주형 변수 추가
  1. 관측일자에서 년/월/일을 추출하여 각 `date_year`/`date_month`/`date_day` 컬럼으로 추가
  2. 최저/최고기온 시간구간 데이터를 시간구간(0-3, 3-6)으로 추출하여 범주형 컬럼으로 추가
  3. 지역명으로 중부지역과 남부지역을 구분하는 `district`컬럼 추가
  4. 계절 컬럼 추가 (봄, 여름, 가을, 겨울)



## 📊 Visualization

### 1. 데이터 탐색을 위한 그래프

#### 1-1. 기상요소별 관계(상관계수)
|관계 변수|상관계수|해석|
|--|--|--|
|기온과 강수량|0.71|평균기온이 높아질 수록 강수량이 높아짐|
|기온과 평균상대습도|0.81|평균기온이 높아질 수록 평균상대습도가 높아짐|
|기온과 최대풍속|-0.55|기온이 높아질 수록 최대풍속은 낮아짐|
|최대풍속과 평균상대습도|-0.74|최대 풍속이 커질 수록 평균상대습도가 낮아짐|
|강수량과 평균상대습도|0.77|강수량이 높아질 수록 평균상대습도가 높아짐|
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EA%B8%B0%EC%83%81%EC%9A%94%EC%86%8C%EB%B3%84_%EC%83%81%EA%B4%80%EA%B3%84%EC%88%98.png"  width='600'/>

#### 1-2. 기상요소별 분포의 특성(계절별 비교)
>최저, 최고, 평균 기온 분포에서는 한국의 사계절 온도 특성이 잘 드러나고 있다.
>
>봄과 가을이 유사한 기온대에 위치하는 반면, 여름과 겨울은 뚜렷한 극단적 온도 분포를 형성하고 있다.
>
>풍속은 계절별로 큰 차이를 보이지 않으나, 여름 분포가 다른 계절에 비해 얇고 높은 봉우리를 형성하고 있다. 이는 다른 계절에 비해 10 이하의 풍속이 분 날이 많았음을 의미한다.
>
>합계 일조시간은 계절별로 나누어도 0 부근과 10부근에서 두 개의 봉우리(이봉 분포)를 형성하고 있다. 이는 계절만으로 설명되지 않는 또 다른 요인(예: 지역, 구름 등)이 일조시간 분포를 결정하는 것으로 추정할 수 있으며, 추가 요인 고려가 필요하다.

<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B8%B0%EC%83%81_%EC%9A%94%EC%86%8C%EB%B3%84_%EB%B6%84%ED%8F%AC_%ED%8A%B9%EC%84%B1.png"  width='800'/>

#### 1-3. 기온·습도·풍속의 관계
>기온과 습도는 계절 변화에 따라 유사한 패턴을 보이며, 함께 상승하거나 하락하는 경향이 나타난다.
>
>반면, 풍속은 이들과 반비례적인 관계를 보여 기온과 습도가 높을수록 낮아지고, 기온과 습도가 낮을수록 강해지는 특징을 가진다.

<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EA%B8%B0%EC%98%A8%C2%B7%EC%8A%B5%EB%8F%84%C2%B7%ED%92%8D%EC%86%8D%EC%9D%98_%EA%B4%80%EA%B3%84(%EC%9B%94_%EB%B3%80%ED%99%94).png"  width='800'/>

---
### 2. 기온

#### 2-1. 연도별 기온 변화
>연도별로 전체 지역에서 관측된 최저, 평균, 최고 기온을 평균을 내어 그린 그래프. 최저, 평균, 최고기온 세 지표 모두 전반적으로 상승하는 추세를 보이고 있다.
>
>특히 최근으로 갈수록 상승 폭이 뚜렷하게 나타나며, 이는 장기적인 기후 변화와 지구 온난화의 영향을 반영하는 것으로 해석될 수 있다.
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/3c01864ad78781b2950ae4b1c031d9e932c98ce4/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94.png"  width='800'/>

#### 2-2. 연도별 월 평균 기온
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%9B%94_%ED%8F%89%EA%B7%A0_%EA%B8%B0%EC%98%A8_(heatmap).png"  width='800'/>

#### 2-3. 연도별 극단 기후 변화
>연도별로 해당 연도에서 나타난 최저 기온과 최고 기온을 그린 그래프.
>
>2005~2024년 동안 최고 기온은 2018년에 41.0℃로 가장 높았고, 최저 기온은 2012년에 -27.7℃로 가장 낮게 기록되었다.
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/70ce266ef68a4ebc53bd4a26785118a9328e1c9a/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%B5%9C%EA%B3%A0_%EB%B0%8F_%EC%B5%9C%EC%A0%80_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94_%EC%B6%94%EC%9D%B4.png"  width='800'/>
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EC%98%A8%EB%8F%84/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%9B%94%EA%B0%84_%EC%B5%9C%EA%B3%A0%C2%B7%EC%B5%9C%EC%A0%80_%EA%B8%B0%EC%98%A8.png"  width='800'/>

#### 2-4. 계절별 일교차 비교
>일교차가 가장 작은 계절은 여름(최대 약 35℃), 가장 큰 계절은 봄(최대 약 48.6℃)으로 나타났다. 
>
>이는 여름철에는 기온이 전반적으로 고르게 높게 유지되는 반면, 봄·가을·겨울에는 일교차가 크게 발생함을 의미한다.
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B3%84%EC%A0%88%EB%B3%84_%EC%9D%BC%EA%B5%90%EC%B0%A8_%EB%B9%84%EA%B5%90.png"  width='800'/>

#### 2-5. 중·남부지역의 계절별 최저/평균/최고온도 변화
>여름에는 중부지역과 남부지역의 최소, 평균, 최대 온도 차이가 거의 보이지 않는 반면, 겨울에는 중부지역이 남부지역보다 눈에 띄게 낮은 온도를 기록했다.
>
>전체적으로 남부지역이 중부지역보다 높은 온도를 유지하며 온화한 기후를 보인다.
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B3%84%EC%A0%88%EB%B3%84_%EC%A4%91%EB%B6%80%EC%A7%80%EC%97%AD%EA%B3%BC_%EB%82%A8%EB%B6%80%EC%A7%80%EC%97%AD%EC%9D%98_%EC%98%A8%EB%8F%84_%EB%B3%80%ED%99%942.png" width='800' />

#### 2-6. 중·남부지역의 이상기온 발생 빈도
>-15도 이하(파란색 계열)인 극한 저온 발생 빈도는 남부지역에 비해 중부지역에서 훨씬 두드러지게 나타난다.
>
>특히 철원, 파주, 제천, 대관령에서 극한 저온이 자주 발생했으며, 이 중에서 대관련의 빈도가 가장 높다.
>
>30도 이상(붉은색 계열)인 극한 고온 발생 빈도는 남부지역에 압도적으로 높게 나타난다.
>
>특히 35도 이상의 극심한 폭염(진한 붉은색) 빈도 역시 남부지역 도시들에서 더 뚜렷하게 관찰된다.

<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%A7%80%EC%97%AD%EB%B3%84_%EC%9D%B4%EC%83%81%EA%B8%B0%EC%98%A8_%EB%B0%9C%EC%83%9D_%EB%B9%88%EB%8F%84.png"  width='800'/>

#### 2-7. 시간대별 최저·최고 기온 발생 빈도
>선 그래프는 각 시간대를 x축으로 하여 최저 및 최고기온이 나타난 시간대의 빈도를 나타낸다.
>
>히트맵은 전체 시간 구간을 백분율로 하여 특정 시간대에 나타난 횟수를 비율로 표시한다.
>
>대부분의 지역에서 03시~09시 사이에 최저기온이 가장 높은 빈도로 발생했다. 특히 03시-06시 구간이 가장 진한 파란색을 나타낸다.
>
>대부분의 지역에서 12시~18시 사이에 최고기온이 압도적으로 높은 빈도로 발생했다. 특히 12시-15시 구간(짙은 빨간색)은 태양 복사가 가장 강하고 지표면의 열 축적이 정점에 달하는 낮 시간대의 특성을 나타낸다.
>
>바다의 영향을 강하게 받는 해양성 기후의 특성을 보이는 부산, 인천, 제주, 진도 등의 특정 지역에서는 다른 내륙 지역에 비해 상대적으로 특정 시간대에 몰리는 경향이 적다. 

<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EC%8B%9C%EA%B0%84%EB%8C%80%EB%B3%84_%EC%B5%9C%EC%A0%80%EC%B5%9C%EA%B3%A0%EA%B8%B0%EC%98%A8_%EB%B0%9C%EC%83%9D_%EB%B9%88%EB%8F%84.png"  width='800'/>

---
### 3. 강수량

#### 3-1. 연도별 강수량 합계
>20년간의 강수량은 120,000 부근의 평균값(붉은 점선)을 중심으로 상당히 큰 폭으로 등락을 거듭하고 있다. 이는 강수 패턴이 안정적이지 않고 불규칙한 변동성을 보이고 있음을 의미한다.
>
>2023년(165,567), 2020년(154,177), 2011년(151,295), 2024년(140,087) 등은 강수량이 평균치를 훨씬 초과하였으며, 특히 2023년은 20년간 최고치를 기록하며 이들 연도에는 집중호우나 홍수 피해 위험이 매우 높았음을 보여준다.
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B0%95%EC%88%98%EB%9F%89_%ED%95%A9%EA%B3%84.png"  width='800'/>

#### 3-2. 연도별 집중호우 빈도
>가장 높은 강수량을 기록했던 2023년, 2020년, 2011년에서 강수 횟수가 많았음을 확인할 수 있다.
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/aaadacf8686394e6211475c39fc7fe974f004ab3/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%A7%91%EC%A4%91%ED%98%B8%EC%9A%B0_%EB%B9%88%EB%8F%84_%EB%B3%80%ED%99%94_%EC%B6%94%EC%9D%B4.png"  width='800'/>

#### 3-3. 연도별 월 강수량 합계
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%9B%94_%EA%B0%95%EC%88%98%EB%9F%89_%ED%95%A9%EA%B3%84_(heatmap).png"  width='800'/>

#### 3-4. 연도별 계절 강수량 변화

  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/aaadacf8686394e6211475c39fc7fe974f004ab3/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B3%84%EC%A0%88_%EA%B0%95%EC%88%98%EB%9F%89_%EB%B3%80%ED%99%94.png"  width='800'/>

#### 3-5. 지역별 강수량 합계
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6899031c71780b1038788056ad933b56547ad525/images/%EC%A7%80%EC%97%AD%EB%B3%84_%EA%B0%95%EC%88%98%EB%9F%89_%ED%95%A9%EA%B3%84.png" width="800">

---

### <적설량>

#### 연도별 적설량 합계

  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EC%A0%81%EC%84%A4%EB%9F%89/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%8B%A0%EC%A0%81%EC%84%A4%EB%9F%89_%ED%95%A9%EA%B3%84.png"  width='800'/>


#### 중부지역과 남부지역의 적설량 비교

  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EC%A0%81%EC%84%A4%EB%9F%89/%EC%A4%91%C2%B7%EB%82%A8%EB%B6%80%EC%A7%80%EC%97%AD_%EC%A0%81%EC%84%A4%EB%9F%89_%EB%B9%84%EA%B5%90.png"  width='800'/>


#### 지역별 적설량 비교

  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EC%A0%81%EC%84%A4%EB%9F%89/%EC%A7%80%EC%97%AD%EB%B3%84_%EC%8B%A0%EC%A0%81%EC%84%A4%EB%9F%89_%ED%95%A9%EA%B3%84.png"  width='800'/>


---
#### 요약
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/2585b9f8c75a348d65daf97b9badb996aa9af80f/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png"  width='1000'/>
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/2585b9f8c75a348d65daf97b9badb996aa9af80f/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B0%95%EC%88%98%EB%9F%89_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png"  width='1000'/>
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/2585b9f8c75a348d65daf97b9badb996aa9af80f/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EC%A0%81%EC%84%A4%EB%9F%89_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png"  width='1000'/>
