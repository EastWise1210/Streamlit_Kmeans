import streamlit as st
import time


def run_progress():
    # 방법 1 progress bar 
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'작업 진행 중 {i+1}')
        bar.progress(i + 1)
        time.sleep(0.05)
        # 0.05 초 마다 1씩증가

    st.balloons()
    # 시간 다 되면 풍선 이펙트 보여주기 