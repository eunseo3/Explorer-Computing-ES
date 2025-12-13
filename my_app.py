import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 기본 설정
st.set_page_config(
    page_title="환율과 물가 프로젝트",
    page_icon="📊",
    layout="wide"
)

# 데이터 불러오기
@st.cache_data
def load_data():
    # --- CPI ---
    cpi_raw = pd.read_csv("CPI.csv", encoding="cp949")
    cpi_raw.columns = cpi_raw.columns.str.strip()

    cpi = cpi_raw[cpi_raw["시도별"] == "전국"]
    cpi = cpi.melt(
        id_vars=["시도별"],
        var_name="Date",
        value_name="CPI"
    )
    cpi["Date"] = pd.to_datetime(cpi["Date"], format="%Y.%m")

    # --- USD/KRW ---
    usd = pd.read_csv("USD_KRW.csv", encoding="utf-8-sig")
    usd["Date"] = pd.to_datetime(usd["Date"])

    # --- EUR/KRW ---
    eur = pd.read_csv("EUR_KRW.csv", encoding="utf-8-sig")
    eur["Date"] = pd.to_datetime(eur["Date"])

    return cpi, usd, eur

cpi_df, usd_df, eur_df = load_data()

# 메뉴1: 홈
def home():
    st.title("📊 환율 상승과 물가 변화")
    st.markdown("### 환율은 어떻게 우리의 일상 경제를 바꾸는가")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📌 프로젝트 배경")
        st.markdown("""
        - 원화 약세 장기화로 환율 변동성이 확대되고 있다.  
        - 환율 상승은 금융시장을 넘어 생활물가와 소비 구조에 영향을 준다.  
        - 본 프로젝트는 **데이터와 뉴스 사례를 결합**하여 그 흐름을 분석한다.
        """)

    with col2:
        st.markdown("### 🎯 프로젝트 목표")
        st.markdown("""
        - 환율과 소비자물가(CPI)의 관계 이해  
        - 환율이 체감 물가로 전이되는 구조 파악  
        - 뉴스 사례를 통한 현실 경제 해석
        """)

    st.divider()

    st.markdown("### 🔎 분석 흐름 요약")
    st.markdown("""
    **① 환율 추이 분석** → **② 물가 지표 확인**  
    **③ 환율-물가 비교 분석** → **④ 뉴스 기반 시사점 도출**
    """)

# 메뉴2: 환율 추이
def fx_trend():
    st.title("💱 주요 환율(USD·EUR) 추이")
    st.info("📌 최근 원화 약세로 USD/KRW와 EUR/KRW 환율 모두 상승 추세를 보이고 있다.")

    fig, ax = plt.subplots()
    ax.plot(usd_df["Date"], usd_df["USD/KRW"], label="USD/KRW")
    ax.plot(eur_df["Date"], eur_df["EUR/KRW"], label="EUR/KRW")
    ax.set_xlabel("Date")
    ax.set_ylabel("KRW")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

# 메뉴3: CPI 추이
def cpi_trend():
    st.title("📈 소비자물가지수(CPI) 추이")
    st.info("📌 소비자물가지수는 단기 변동보다 중장기적으로 완만한 상승 흐름을 보인다.")

    fig, ax = plt.subplots()
    ax.plot(cpi_df["Date"], cpi_df["CPI"], marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("CPI")
    ax.grid(True)

    st.pyplot(fig)

# 메뉴4: 환율-물가 비교
def compare():
    st.title("🔍 물가-환율 비교 분석")

    st.markdown("""
    소비자물가지수(CPI)와 환율의 시계열 변화를  
    **이중축 그래프**를 통해 비교하였다.
    """)

    option = st.radio(
        "비교할 환율 선택",
        ["CPI – USD/KRW", "CPI – EUR/KRW"]
    )

    fig, ax1 = plt.subplots()
    ax1.plot(cpi_df["Date"], cpi_df["CPI"], label="CPI")
    ax1.set_ylabel("CPI")
    ax1.grid(True)

    ax2 = ax1.twinx()

    if option == "CPI – USD/KRW":
        ax2.plot(usd_df["Date"], usd_df["USD/KRW"], linestyle="--", label="USD/KRW")
        ax2.set_ylabel("USD/KRW")
    else:
        ax2.plot(eur_df["Date"], eur_df["EUR/KRW"], linestyle="--", label="EUR/KRW")
        ax2.set_ylabel("EUR/KRW")

    st.pyplot(fig)

    st.success("""
    ✔ 환율 상승과 CPI 상승은 중장기적으로 동반되는 경향을 보인다.  
    ✔ 환율 변화는 즉각적 영향보다 **시차를 두고 물가 압력으로 작용**한다.
    """)

# 메뉴5: 뉴스 요약
def news_summary():
    st.title("📰 환율·물가 변화: 뉴스로 본 시사점")

    st.markdown("""
    데이터 분석에서 확인한 환율과 물가의 흐름은  
    실제 경제 전반에서 다음과 같은 결과로 나타나고 있다.
    """)

    st.markdown("---")

    st.markdown("""
    **🛢️ 환율 상승과 소비자물가**

    고환율 지속으로 석유류·수입식품 가격이 상승하며  
    소비자물가 상승 압력이 확대되고 있다.

    🔗 [기사 바로가기](https://www.yna.co.kr/view/AKR20251202022451002?input=1195m)
    """)

    st.markdown("---")

    st.markdown("""
    **🧺 생활물가 및 체감 물가 압박**

    생활물가지수와 신선식품 가격 상승으로  
    소비자가 체감하는 물가 부담이 커지고 있다.

    🔗 [기사 바로가기](https://www.dnews.co.kr/uhtml/view.jsp?idxno=202512021056316950034)
    """)

    st.markdown("---")

    st.markdown("""
    **🍞 구조적 물가 상승 사례**

    빵 가격 사례는 환율·원자재 가격 외에도  
    유통 구조가 물가에 영향을 미침을 보여준다.

    🔗 [기사 바로가기](https://www.kmib.co.kr/article/view.asp?arcid=1757313516&code=11171314&cp=nv)
    """)

    st.markdown("---")

    st.markdown("""
    **✈️ 환율 상승과 소비 구조 변화**

    해외여행 비용 상승으로 소비 패턴이 변화하는 반면,  
    인바운드 관광에는 긍정적 효과가 나타나고 있다.

    🔗 [기사 바로가기](https://www.traveltimes.co.kr/news/articleView.html?idxno=414676)
    """)

    st.warning("""
    📌 환율 상승은 물가·소비·산업 구조 전반에  
    연쇄적인 영향을 미치는 핵심 변수임을 확인할 수 있다.
    """)

# 메인
def main():
    menu = st.sidebar.radio(
        "대시보드 메뉴",
        [
            "🏠 프로젝트 개요",
            "💱 주요 환율(USD·EUR) 추이",
            "📈 소비자물가지수(CPI) 추이",
            "🔍 물가-환율 비교 분석",
            "📰 관련 뉴스 및 시사점"
        ]
    )

    if menu == "🏠 프로젝트 개요":
        home()
    elif menu == "💱 주요 환율(USD·EUR) 추이":
        fx_trend()
    elif menu == "📈 소비자물가지수(CPI) 추이":
        cpi_trend()
    elif menu == "🔍 물가-환율 비교 분석":
        compare()
    elif menu == "📰 관련 뉴스 및 시사점":
        news_summary()

if __name__ == "__main__":
    main()

