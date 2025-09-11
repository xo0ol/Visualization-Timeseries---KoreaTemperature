
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

# plt 타이틀 설정 및 png 저장 간편 함수 정의
def maintitle_and_save(main_title, fontsize=30, main_y = 1.005):
    main_title = main_title
    path = f'../images/{main_title.replace(" ", "_")}.png'
    plt.suptitle(main_title, fontsize=fontsize, fontweight='bold', y=main_y)
    plt.tight_layout()

    # 이미지 저장
    plt.savefig(path, bbox_inches='tight')
    plt.show()


# 범주형 날짜/시간의 str 타입 설정
def column_to_str(df, column='date_year'):
    df[column] = df[column].astype('str')

# 간단한 시각화 출력 시 figure 설정
def set_figure(x=15, y=10):
    plt.figure(figsize=(x, y))
    
# plt 그리드 설정 함수
def set_plot_style(ax, title, fontsize=15, y_lim=None, grid=False, fontweight=None):
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.grid(grid)
    ax.set_title(title, fontsize=fontsize, fontweight=fontweight)
    if y_lim:
        ax.set_ylim(y_lim)

# 상관계수를 표시하는 함수 정의
def plot_corr(x, y, **kwargs):
    ax = plt.gca()
    r, p = pearsonr(x, y)
    ax.annotate(f'{r:.2f}', 
                xy=[.5, .5], 
                xycoords=ax.transAxes, 
                fontsize=40*abs(r),
                color='blue' if r > 0 else 'red',
                ha='center', 
                va='center')

# pairplot
def pair_grid(data, s=5, height=2.5):
    g = sns.PairGrid(data, height=height)
    g.map_lower(sns.scatterplot, s=s)
    g.map_diag(sns.kdeplot)
    g.map_upper(plot_corr)
    plt.show()

# 가로 막대 플롯(left starts)
def plot_barh_leftstarts(results, category_names, figsize=(10, 5)):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=figsize)
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncols=len(category_names)//2, bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


class PlotText:
    """
    matplotlib.axes.Axes 객체에 텍스트를 추가하는 클래스.
    바 차트나 라인 차트 등 다양한 그래프에 라벨을 쉽게 추가할 수 있습니다.
    """
    @staticmethod
    def add_labels(ax, data, x_column, y_column, adjust=0, orientation='v', measure='', ha='center', va='center', fontsize=8, fontweight='normal', f=0, color='black'):
        """
        그래프에 텍스트 라벨을 추가하는 정적 메서드.
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            텍스트를 추가할 Axes 객체.
        data : pandas.DataFrame
            그래프를 그리는 데 사용된 데이터프레임.
        x_column : str
            x축에 해당하는 데이터프레임 컬럼명.
        y_column : str
            y축에 해당하는 데이터프레임 컬럼명.
        orientation : str, optional
            텍스트 라벨의 방향 ('v' for vertical, 'h' for horizontal), by default 'v'.
        measure : str, optional
            라벨에 추가할 단위 문자열, by default ''.
        ha : str, optional
            수평 정렬 ('left', 'center', 'right'), by default 'center'.
        va : str, optional
            수직 정렬 ('top', 'bottom', 'center'), by default 'center'.
        fontsize : int, optional
            폰트 크기, by default 8.
        fontweight : str, optional
            폰트 굵기, by default 'bold'.
        f : int, optional
            소수점 자릿수, by default 0.
        color : str, optional
            텍스트 색상, by default 'black'.
        """
        # 세로 그래프 - x축 범주: str
        if orientation == 'v':
            x_values = data[x_column].astype('str')
            y_values = data[y_column]
            for x, y in zip(x_values, y_values):
                ax.text(x, y + (y * adjust), f'{y:,.{f}f}{measure}', ha=ha, va='bottom', fontsize=fontsize, fontweight=fontweight, color=color)
        
        # 가로 그래프 - y축 범주: str
        elif orientation == 'h':
            x_values = data[x_column]
            y_values = data[y_column].astype('str')
            for x, y in zip(x_values, y_values):
                ax.text(x - (x * adjust), y, f'{x:,.{f}f}{measure}', ha='left', va=va, fontsize=fontsize, fontweight=fontweight, color=color)
