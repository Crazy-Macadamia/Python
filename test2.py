import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

# st.header('Unit 5. Plotly chart')

# https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv 읽고 확인하기
medal = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv')
medal

st.subheader('5-1. Plotly Pie/Donut chart') 
fig = px.pie(medal,values="gold",names = "nation",title="올림픽양궁 금메달")
fig.update_traces(textposition='inside',textinfo='percent + label')

fig.update_layout(font=dict(size=16))
# fig.update(layout_showlegend=False)  # 범례 표시 제거
st.plotly_chart(fig)

st.subheader('5-2. Plotly Bar chart')
# text_auto=True 값 표시 여부
fig =  px.bar(medal, x="nation", y=["gold", "silver", "bronze"],
text_auto=True, title="올림픽 양궁 메달 현황")


st.plotly_chart(fig)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\test2.py