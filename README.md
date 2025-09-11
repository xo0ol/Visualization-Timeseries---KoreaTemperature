# Korea Temperature Time Series data Visualization (2005~2024)
* 이 프로젝트는 2005년부터 2024년까지 20년간의 대한민국 전체 지역의 다양한 기상 요인 데이터를 분석하고 시각화합니다.
* 기상청 자료개방포털에서 제공하는 데이터를 바탕으로
* 이 분석을 통해 특정 지역의 기온 특성을 파악하고, 기록적인 한파와 폭염이 발생했던 해를 찾아내어 기후 변화 추이를 이해하는 것을 목표로 합니다.
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="600"/>
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EA%B0%95%EC%88%98%EB%9F%89(2005%EB%85%84~2024%EB%85%84).png" width="600"/>
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EC%A0%81%EC%84%A4%EB%9F%89_%EB%B3%80%ED%99%94(2005%EB%85%84~2024%EB%85%84).png" width="600"/>
</p>

## 📝 프로젝트 개요 (Overview)

### 1. 💾 데이터 수집
[기상청 자료개방포털](https://data.kma.go.kr/cmmn/main.do)에서 2005~2024년 대한민국 지역별 기온 데이터를 다운로드했습니다.
- categorical variable

| 한글 컬럼명 | 변환된 영어 컬럼명 | 내용 |
| :--- | :--- | :--- |
| 지점 | `region_number` | 기상 관측소의 고유 번호입니다. |
| 지점명 | `region_name` | 기상 관측소의 이름 (예: 서울, 부산)입니다. |
| 행정구역 | `region` | 기상 관측소가 소속된 구역의 이름입니다. |
| 일시 | `date` | 관측이 이루어진 날짜입니다. |
| 최저기온 시각(hhmi) | `min_temp_time` | 최저 기온이 기록된 시각 (시간:분)입니다. |
| 최고기온 시각(hhmi) | `max_temp_time` | 최고 기온이 기록된 시각 (시간:분)입니다. |
| 최대 순간풍속 시각(hhmi) | `max_instant_wind_time` | 최대 순간 풍속이 관측된 시각 (시간:분)입니다. |
| 최대 풍속 시각(hhmi) | `max_wind_time` | 최대 풍속이 관측된 시각 (시간:분)입니다. |
| 최대 순간 풍속 풍향(16방위) | `max_instant_wind_direction_16` | 최대 순간 풍속이 불었던 방향을 16방위로 나타낸 값입니다. |
| 최대 풍속 풍향(16방위) | `max_wind_direction_16` | 최대 풍속이 불었던 방향을 16방위로 나타낸 값입니다. |
| 최저기온 시간구간 | `min_temp_hour` | 최저 기온이 기록된 시간대 (예: 0~1시)를 나타냅니다. |
| 최고기온 시간구간 | `max_temp_hour` | 최고 기온이 기록된 시간대 (예: 13~14시)를 나타냅니다. |
| 최대 풍속 시간구간 | `max_wind_hour` | 최대 풍속이 기록된 시간대를 나타냅니다. |
| 최대 순간풍속 시간구간 | `max_instant_wind_hour` | 최대 순간풍속이 기록된 시간대를 나타냅니다. |
| 일시(연) | `date_year` | 일시에서 연도만 분리한 값입니다. |
| 일시(월) | `date_month` | 일시에서 월만 분리한 값입니다. |
| 일시(일) | `date_day` | 일시에서 일만 분리한 값입니다. |
| 계절 | `season` | date_month를 기준으로 계절을 매칭한 값입니다.

- continuous variable

| 한글 컬럼명 | 변환된 영어 컬럼명 | 내용 |
| :--- | :--- | :--- |
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
시각화에 용이한 형태로 데이터를 처리하기 위해 다음과 같은 단계를 거쳐 데이터 정제를 완료했습니다.
  * 데이터 병합
    * 기상청 데이터에는 지역명과 고유번호만 포함되어 있어, 해당 지역이 어느 행정구역에 소속되어있는지 확인을 위해, 별도의 지역 고유번호-행정구역명 매핑 데이터를 병합하여 분석에 필요한 행정구역 컬럼을 추가했습니다.
    * 사용된 데이터 셋
      ```python
      !wget -O '/content/region.csv' 'https://raw.githubusercontent.com/xo0ol/Visualization-Timeseries---Temperature/refs/heads/main/data/region.csv'
      ```
  * 결측치 처리
    |||
    |--|--|
    |평균 기온| 최저기온과 최고기온의 평균값으로 대체
    |강수량|NaN인 경우, 그 날 비가 내리지 않아 관측값 없음으로 보아, 0으로 대체
    |최심적설 및 최심신적설량|NaN인 경우, 관측값 없음으로 보아 0으로 대체
    |40% 이상이 결측치인 컬럼 삭제| 합계 일사량, 평균 전운량, 평균 중하층운량 3개의 컬럼은 40% 이상이 결측치이므로, 임의의 값으로 채울 시 데이터 왜곡될 것을 고려하여 컬럼 삭제함.
    |1,000개 미만인 결측치 단순 제거|
    |합계 일조시간| 랜덤포레스트 모델을 생성하여 결측값을 예측값으로 대체

  * 이상치 처리
    |||
    |--|--|
    |풍향|0 미만의 음수, 또는 360 이상인 값 제거

- 데이터 전처리 과정은 [KoreaTemp_preprocessing](https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/main/src/KoreaTemp_preprocessing.ipynb) 파일에서 확인할 수 있습니다.


### 3. 📊 시각화 및 분석 결과
<p align="center">
  <img src=""  width='800'/>
</p>

#### 기상요소별 관계(상관계수)
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e20a67a8bc13901f7b09e38bad89494b507827a4/images/%EA%B8%B0%EC%83%81%EC%9A%94%EC%86%8C%EB%B3%84_%EC%83%81%EA%B4%80%EA%B3%84%EC%88%98.png"  width='800'/>
</p>

|관계 변수|상관계수|해석|
|--|--|--|
|기온과 강수량|0.71|평균기온이 높아질 수록 강수량이 높아짐|
|기온과 평균상대습도|0.81|평균기온이 높아질 수록 평균상대습도가 높아짐|
|기온과 최대풍속|-0.55|기온이 높아질 수록 최대풍속은 낮아짐|
|최대풍속과 평균상대습도|-0.74|최대 풍속이 커질 수록 평균상대습도가 낮아짐|
|강수량과 평균상대습도|0.77|강수량이 높아질 수록 평균상대습도가 높아짐|


#### 기상요소별 분포의 특성(계절별 비교)
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B8%B0%EC%83%81_%EC%9A%94%EC%86%8C%EB%B3%84_%EB%B6%84%ED%8F%AC_%ED%8A%B9%EC%84%B1.png"  width='800'/>
</p>
기상청 데이터에서 연속형 데이터만 뽑아서 분포를 그려봄. 합계 일조시간은 분포가 2개의 봉우리가 졌음

#### 연도별 기온 변화
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/3c01864ad78781b2950ae4b1c031d9e932c98ce4/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B8%B0%EC%98%A8_%EB%B3%80%ED%99%94.png"  width='800'/>
</p>

#### 계절별 일교차 비교
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B3%84%EC%A0%88%EB%B3%84_%EC%9D%BC%EA%B5%90%EC%B0%A8_%EB%B9%84%EA%B5%90.png"  width='800'/>
</p>
여름의 최대 일교차가 35도 차이로 4계절 중 가장 적음. 나머지 계절은 45~47도까지 일교차가 벌어짐.

#### 중·남부지역의 계절별 최저/평균/최고온도 변화
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EA%B3%84%EC%A0%88%EB%B3%84_%EC%A4%91%EB%B6%80%EC%A7%80%EC%97%AD%EA%B3%BC_%EB%82%A8%EB%B6%80%EC%A7%80%EC%97%AD%EC%9D%98_%EC%98%A8%EB%8F%84_%EB%B3%80%ED%99%942.png" width='800' />
</p>
남부지역에 중부지역보다 4계절 내내 뚜렸하게 기온이 높음을 보여줌
다만, 여름의 경우 두 지역의 기온은 눈에 띄는 차이가 없어 동일하게 더움을 보여줌

#### 중·남부지역의 이상기온 발생 빈도
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EC%A7%80%EC%97%AD%EB%B3%84_%EC%9D%B4%EC%83%81%EA%B8%B0%EC%98%A8_%EB%B0%9C%EC%83%9D_%EB%B9%88%EB%8F%84.png"  width='800'/>
</p>
중부지역 그래프를 보면 대관령이 -10도 이하의 이상기후 발생 빈도가 압도적으로 높음. 남부지역의 경우에는 의성과 봉화가 다른 지역에 비해 비교적 추운 날이 많았음.


#### 시간대별 최저·최고 기온 발생 빈도
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/e2de6b711965134c9dd7c1ba6c25e8d0168655b3/images/%EC%8B%9C%EA%B0%84%EB%8C%80%EB%B3%84_%EC%B5%9C%EC%A0%80%EC%B5%9C%EA%B3%A0%EA%B8%B0%EC%98%A8_%EB%B0%9C%EC%83%9D_%EB%B9%88%EB%8F%84.png"  width='800'/>
</p>
최저기온은 보통 새벽 3시~6시 사이에, 최고기온은 12시~15시 사이에 많이 발생됨.
그러나 아래 히트맵을 보면 대부분의 지역이 특정 시간구간대에 최저 및 최고 기온 기록 시간대가 몰려있는것에 비해 부산광역시, 제주, 진도 3지역은 최저 및 최고기온 발생 빈도가 구간별로 뚜렷한 차이를 보이지 않음.

#### 연도별 집중호우 빈도
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/aaadacf8686394e6211475c39fc7fe974f004ab3/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EC%A7%91%EC%A4%91%ED%98%B8%EC%9A%B0_%EB%B9%88%EB%8F%84_%EB%B3%80%ED%99%94_%EC%B6%94%EC%9D%B4.png"  width='800'/>
</p>


#### 연도별 계절 강수량 변화
<p align="center">
  <img src="https://github.com/xo0ol/Visualization-Timeseries---KoreaTemperature/blob/aaadacf8686394e6211475c39fc7fe974f004ab3/images/%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B3%84%EC%A0%88_%EA%B0%95%EC%88%98%EB%9F%89_%EB%B3%80%ED%99%94.png"  width='800'/>
</p>
