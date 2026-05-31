import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib import font_manager
from pathlib import Path

st.set_page_config(page_title="데이터 시각화", page_icon="📊", layout="wide")
st.title("데이터 시각화 예시")
st.write("matplotlib, seaborn, plotly로 만든 간단한 한글 그래프 예시입니다.")


def set_korean_font():
    font_path = Path(__file__).resolve().parents[1] / "fonts" / "NotoSansKR-Medium.ttf"
    if font_path.exists():
        font_manager.fontManager.addfont(str(font_path))
        font_name = font_manager.FontProperties(fname=str(font_path)).get_name()
        plt.rcParams["font.family"] = font_name
        plt.rcParams["axes.unicode_minus"] = False
        return font_name

    font_names = [
        "NanumGothic",
        "AppleGothic",
        "Malgun Gothic",
        "맑은 고딕",
        "Noto Sans CJK JP",
        "Noto Sans KR",
    ]
    available = {f.name for f in font_manager.fontManager.ttflist}
    for name in font_names:
        if name in available:
            plt.rcParams["font.family"] = name
            plt.rcParams["axes.unicode_minus"] = False
            return name

    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
    return "sans-serif"


font_name = set_korean_font()


days = ["월요일", "화요일", "수요일", "목요일", "금요일"]
study_hours = [2.5, 3.0, 1.8, 2.2, 2.9]

st.header("1. matplotlib 막대 그래프")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(days, study_hours, color="#5B8FF9")
ax.set_title("주간 공부 시간", fontsize=16)
ax.set_xlabel("요일", fontsize=12)
ax.set_ylabel("공부 시간 (시간)", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.5)
st.pyplot(fig)

st.header("2. seaborn 선 그래프")
sns.set_theme(font=font_name, style="whitegrid")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.lineplot(x=days, y=study_hours, marker="o", linewidth=2.5, color="#61DDAA", ax=ax2)
ax2.set_title("요일별 공부 시간 변화", fontsize=16)
ax2.set_xlabel("요일", fontsize=12)
ax2.set_ylabel("공부 시간 (시간)", fontsize=12)
ax2.set_ylim(0, max(study_hours) + 1)
st.pyplot(fig2)

st.header("3. plotly 파이 차트")
subjects = ["국어", "수학", "영어", "과학", "사회"]
subject_share = [20, 25, 30, 15, 10]
fig3 = px.pie(
    names=subjects,
    values=subject_share,
    title="과목별 공부 비중",
    hole=0.35,
)
fig3.update_traces(textposition="inside", textinfo="percent+label")
fig3.update_layout(
    font=dict(family="Malgun Gothic, NanumGothic, sans-serif", size=14),
    legend_title_text="과목",
)
st.plotly_chart(fig3, use_container_width=True)
