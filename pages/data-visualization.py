# Streamlit을 활용한 간단한 데이터 시각화 앱 예시
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
# 한글 폰트 설정 (NanumGothic)

font_path = 'fonts/NanumGothic-Regular.ttf'
if os.path.exists(font_path):
	fontprop = fm.FontProperties(fname=font_path)
	plt.rc('font', family=fontprop.get_name())
else:
	st.warning(f"폰트 파일을 찾을 수 없습니다: {font_path}. 기본 폰트로 대체합니다.")
	fontprop = None

st.title('간단한 데이터 시각화')

# 임의의 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
	'x': np.arange(1, 21),
	'y': np.random.randint(10, 100, 20)
})

st.subheader('데이터 테이블')
st.dataframe(data)

st.subheader('라인 차트')
st.line_chart(data.set_index('x'))

st.subheader('바 차트')
st.bar_chart(data.set_index('x'))

st.subheader('산점도 (matplotlib)')
fig, ax = plt.subplots()
ax.scatter(data['x'], data['y'], color='orange')
if fontprop:
	ax.set_xlabel('x', fontproperties=fontprop)
	ax.set_ylabel('y', fontproperties=fontprop)
	ax.set_title('산점도', fontproperties=fontprop)
else:
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_title('산점도')
st.pyplot(fig)
