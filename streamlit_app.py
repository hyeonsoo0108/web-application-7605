import streamlit as st

st.set_page_config(page_title="자기소개 페이지", page_icon="👋", layout="centered")

st.title("👋 안녕하세요!")
st.markdown("""
이 페이지는 간단한 자기소개를 위한 기본 템플릿입니다.
왼쪽 사이드바에서 항목을 선택하여 내용을 채워주세요.
""")

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Go to",
        ["소개", "경력", "기술 스택", "연락처"],
    )

if page == "소개":
    st.header("소개")
    st.write("여기에 자기소개 텍스트를 입력하세요.")
    st.write("예: 이현수, 직업, 관심사(영어교육), 목표 등")

elif page == "경력":
    st.header("경력")
    st.write("여기에 주요 경력과 경험을 작성하세요.")
    st.write("예: 이전 직장, 프로젝트, 인턴십 등")

elif page == "기술 스택":
    st.header("기술 스택")
    st.write("여기에 사용 가능한 기술과 도구를 정리하세요.")
    st.markdown("- Python\n- Streamlit\n- 데이터 분석\n- 웹 개발")

elif page == "연락처":
    st.header("연락처")
    st.write("여기에 연락 가능한 이메일이나 링크를 입력하세요.")
    st.write("예: email@example.com, GitHub, LinkedIn")
