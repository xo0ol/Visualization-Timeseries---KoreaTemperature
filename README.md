# Korea Temperature Time Series Data Visualization (2005–2024)
* 2005 ~ 2024년 20년간의 대한민국 지역별 기상 데이터를 전처리 및 분석하여 시각화하는 것을 목표로 합니다.
* 데이터는 [기상청 자료개방포털](https://data.kma.go.kr/cmmn/main.do)에서 수집하였으며, 이를 기반으로 지역별 기온 특성, 극한 기후 발생 패턴, 계절별 기상 변화를 탐색합니다.
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="300" />
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B0%95%EC%88%98%EB%9F%89_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="300"/>
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EC%A0%81%EC%84%A4%EB%9F%89_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="300"/>
</p>

## 📝 Overview

### 1. 💾 데이터 수집

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

* 데이터 병합

기상청 데이터에는 해당 지역을 포함하는 행정구역에 대한 정보가 없으므로 해당 지역을 포함하는 행정구역명을 매핑할 수 있도록 'region.csv'파일과 데이터 병합
    
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

📂 전처리 과정은 [KoreaTemp_preprocessing](https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/main/src/KoreaTemp_preprocessing.ipynb) 파일에서 확인할 수 있습니다.


## 📊 Visualization

### <데이터 탐색>

#### 기상요소별 관계(상관계수)
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EA%B8%B0%EC%83%81%EC%9A%94%EC%86%8C%EB%B3%84_%EC%83%81%EA%B4%80%EA%B3%84%EC%88%98.png"  width='800'/>

|관계 변수|상관계수|해석|
|--|--|--|
|기온과 강수량|0.71|평균기온이 높아질 수록 강수량이 높아짐|
|기온과 평균상대습도|0.81|평균기온이 높아질 수록 평균상대습도가 높아짐|
|기온과 최대풍속|-0.55|기온이 높아질 수록 최대풍속은 낮아짐|
|최대풍속과 평균상대습도|-0.74|최대 풍속이 커질 수록 평균상대습도가 낮아짐|
|강수량과 평균상대습도|0.77|강수량이 높아질 수록 평균상대습도가 높아짐|


#### 기상요소별 분포의 특성(계절별 비교)
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B8%B0%EC%83%81_%EC%9A%94%EC%86%8C%EB%B3%84_%EB%B6%84%ED%8F%AC_%ED%8A%B9%EC%84%B1.png"  width='800'/>

#### 기온·습도·풍속의 관계
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EA%B8%B0%EC%98%A8%C2%B7%EC%8A%B5%EB%8F%84%C2%B7%ED%92%8D%EC%86%8D%EC%9D%98_%EA%B4%80%EA%B3%84(%EC%9B%94_%EB%B3%80%ED%99%94).png"  width='800'/>

---
### <기온>

#### 연도별 기온 변화
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/3c01864ad78781b2950ae4b1c031d9e932c98ce4/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94.png"  width='800'/>

#### 연도별 월 평균 기온
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%9B%94_%ED%8F%89%EA%B7%A0_%EA%B8%B0%EC%98%A8_(heatmap).png"  width='800'/>

#### 연도별 극단 기후 변화
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%B5%9C%EA%B3%A0_%EB%B0%8F_%EC%B5%9C%EC%A0%80_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94_%EC%B6%94%EC%9D%B4.png"  width='800'/>


#### 계절별 일교차 비교
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B3%84%EC%A0%88%EB%B3%84_%EC%9D%BC%EA%B5%90%EC%B0%A8_%EB%B9%84%EA%B5%90.png"  width='800'/>
여름의 최대 일교차가 35도. 4계절 중 최저치

#### 중·남부지역의 계절별 최저/평균/최고온도 변화
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B3%84%EC%A0%88%EB%B3%84_%EC%A4%91%EB%B6%80%EC%A7%80%EC%97%AD%EA%B3%BC_%EB%82%A8%EB%B6%80%EC%A7%80%EC%97%AD%EC%9D%98_%EC%98%A8%EB%8F%84_%EB%B3%80%ED%99%942.png" width='800' />
남부지역에 중부지역보다 4계절 내내 뚜렸하게 기온이 높음을 보여줌
다만, 여름의 경우 두 지역의 기온은 눈에 띄는 차이가 없어 동일하게 더움을 보여줌

#### 중·남부지역의 이상기온 발생 빈도
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%A7%80%EC%97%AD%EB%B3%84_%EC%9D%B4%EC%83%81%EA%B8%B0%EC%98%A8_%EB%B0%9C%EC%83%9D_%EB%B9%88%EB%8F%84.png"  width='800'/>
중부지역 그래프를 보면 대관령이 -10도 이하의 이상기후 발생 빈도가 압도적으로 높음. 남부지역의 경우에는 의성과 봉화가 다른 지역에 비해 비교적 추운 날이 많았음.

#### 연도별 월간 최저/최고 기온
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/bd0ba62c50436d19ae3c8345a59b2cefd0850cd1/images/%EC%98%A8%EB%8F%84/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%9B%94%EA%B0%84_%EC%B5%9C%EA%B3%A0%C2%B7%EC%B5%9C%EC%A0%80_%EA%B8%B0%EC%98%A8.png"  width='800'/>

#### 시간대별 최저·최고 기온 발생 빈도
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EC%8B%9C%EA%B0%84%EB%8C%80%EB%B3%84_%EC%B5%9C%EC%A0%80%EC%B5%9C%EA%B3%A0%EA%B8%B0%EC%98%A8_%EB%B0%9C%EC%83%9D_%EB%B9%88%EB%8F%84.png"  width='800'/>
최저기온은 보통 새벽 3시~6시 사이에, 최고기온은 12시~15시 사이에 많이 발생됨.
그러나 아래 히트맵을 보면 대부분의 지역이 특정 시간구간대에 최저 및 최고 기온 기록 시간대가 몰려있는것에 비해 부산광역시, 제주, 진도 3지역은 최저 및 최고기온 발생 빈도가 구간별로 뚜렷한 차이를 보이지 않음.

---
### <강수량>

#### 연도별 강수량 합계

<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B0%95%EC%88%98%EB%9F%89_%ED%95%A9%EA%B3%84.png"  width='800'/>


#### 연도별 월 강수량 합계
<img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/6736592eae6636479c93a7a069bfaadeba326abf/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%9B%94_%EA%B0%95%EC%88%98%EB%9F%89_%ED%95%A9%EA%B3%84_(heatmap).png"  width='800'/>



#### 연도별 집중호우 빈도

  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/aaadacf8686394e6211475c39fc7fe974f004ab3/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%A7%91%EC%A4%91%ED%98%B8%EC%9A%B0_%EB%B9%88%EB%8F%84_%EB%B3%80%ED%99%94_%EC%B6%94%EC%9D%B4.png"  width='800'/>



#### 연도별 계절 강수량 변화

  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/aaadacf8686394e6211475c39fc7fe974f004ab3/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B3%84%EC%A0%88_%EA%B0%95%EC%88%98%EB%9F%89_%EB%B3%80%ED%99%94.png"  width='800'/>


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
