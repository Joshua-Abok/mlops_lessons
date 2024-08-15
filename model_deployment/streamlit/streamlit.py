import numpy as np 
import pandas as pd 

import streamlit as st

from sklearn import preprocessing
# import pickle

from predictions import predict


def main(): 
    st.title("Survival Prediction") 
    html_temp = """

    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Survivor prediction app </h2>
    </div>

    """

    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.text_input("Age", "0")
    PClass = st.selectbox("PClass", ["1", "2", "3"])
    Fare = st.text_input("Fare", "0")
    Embarkment = st.selectbox("Embarkment", ["0", "1", "2"])

    if st.button("predict"): 
        result = predict(np.array([[int(age), int(PClass), int(Fare), int(Embarkment)]]))
        st.text(result[0])




if __name__ == "__main__":
    main()