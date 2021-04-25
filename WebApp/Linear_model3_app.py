import streamlit as st
import pandas as pd
import numpy as np
import pickle
import math

pkl_filename = 'pickle_model.pkl'
with open(pkl_filename,'rb') as file:
    pickle_model = pickle.load(file)

def load(Mileage,Years):
    input = np.array([[Mileage,Years]]).astype(np.float)
    prediction = math.floor(pickle_model.predict(input))
    return prediction


def main():
    st.title('Predict Car Selling Price')
    Mileage = st.text_input('Mileage','Enter Here')
    Years = st.text_input('Years','Enter Here')

    if st.button('Predict'):
        res = load(Mileage,Years)
        st.success('Predicted Price : {} USD'.format(res))

if __name__ == '__main__':
    main()
