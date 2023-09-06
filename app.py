import streamlit as st
import statistics as stat
from generator import generate_pdf

st.title("Mathematical Operations")

st.write("Enter three numbers for operations:")

#-----------------user input area-----------------#

num1, num2 , num3 = st.columns(3) 

with num1:
    x = st.number_input("",min_value=0, max_value=100, step=1, format="%d",key="1")

with num2:
    y = st.number_input("",min_value=0, max_value=100, step=1, format="%d",key="2")

with num3:
    z = st.number_input("",min_value=0, max_value=100, step=1, format="%d",key="3")

#-----------------Submition area-----------------#

s1 , s2 = st.columns(2)

with s1:
    submit_bt = st.checkbox("Submit")
    if submit_bt:
        number_list = [x,y,z]

        cal_mean = f"The Mean is: {stat.mean(number_list)}"
        cal_mode = f"The Mode is: {stat.mode(number_list)}"
        cal_median = f"The Median is: {stat.median(number_list)}"
        cal_stdev = f"The Standard Deviation is: {stat.stdev(number_list)}"

with s2:
    if submit_bt:
        st.write("The Values Are Saved!")

#-----------------Operations area-----------------#
if submit_bt:
    bt1, bt2 , bt3 , bt4 = st.columns(4)

    with bt1:
        mean_bt = st.button("Mean")


    with bt2:
        mode_bt = st.button("Mode")

    with bt3:
        median_bt = st.button("Median")

    with bt4:
        stdev_bt = st.button("Standard Deviation")

#-----------------Answers area-----------------#
try:
    if mean_bt:
        st.success(cal_mean)
    if mode_bt:
        st.success(cal_mode)
    if median_bt:
        st.success(cal_median)
    if stdev_bt:
        st.success(cal_stdev)
#-----------------Print area-----------------#
    document = generate_pdf(cal_mean, cal_mode, cal_median, cal_stdev, number_list)
    st.download_button(
        label="Print The Answers",
        data = document.getvalue(),
        file_name="result.pdf",
        key="pdf-donwload"
    )

except NameError:
    pass
    
#----------------------------------------------------------------------------------------#