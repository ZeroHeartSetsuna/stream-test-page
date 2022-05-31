import imp
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("Error!!")

st.write('Please check your xxxxxxx')
'Can not found _0x11111 file'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done'

left_column, right_column = st.columns(2)
button = left_column.button('詳しいを表示')
if button:
    right_column.write('Can not found text_1')

expander1 = st.expander('warning')
expander1.write('ObjectNotFound(conda:String)[],CommandNotFoundException')
expander2 = st.expander('loading failed')
expander2.write('問い合わせを書く2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせを書く3')