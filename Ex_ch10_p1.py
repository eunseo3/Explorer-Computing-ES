# 아래에 코드를 작성해주세요.

import streamlit as st
import pandas as pd

st.markdown("# 나의 소개 페이지")
st.header("자기소개")
st.text("안녕하세요, 제 이름은 전은서입니다.")
st.write("저는 **경제학부**에 재학중이고 *21살*입니다.")

st.header("좋아하는 것")
st.write("저는 **해외여행**을 좋아합니다.")
st.write("제 여행 메이트는 *친언니*입니다.")

st.header("앞으로의 목표")
st.write(pd.DataFrame({"목표": ["토익 시험보기","관심있는 과목들 수강하기","운동 꾸준히 하기"]}))
