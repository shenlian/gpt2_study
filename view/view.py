"""
run: streamlit run ./view/view.py
brief: 使用streamlit框架快速搭建
    机器学习交互展示的前端demo，前
    端属性值改变会触发文件重新加载执行

"""

import streamlit as st
import datetime


st.write("hello world")
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

appointment = st.slider(
    "Schedule your appointment:",
    value=(datetime.time(11, 30), datetime.time(12, 45)))
st.write("You're scheduled for:", appointment)
print('[{}] now age:{}'.format(datetime.datetime.now(), str(age)))