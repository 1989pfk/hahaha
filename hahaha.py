import streamlit as st
import time

st.title("Progess")

# Create a progress bar with an initial value of 0%
progress_bar = st.progress(0)

# Simulate a task with a loop
for i in range(100):
    # Update the progress bar's value
    progress_bar.progress(i + 1)
    time.sleep(0.01)

st.success('Task complete!')    

st.balloons()