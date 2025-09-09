# import libraries
import streamlit as st
import pandas as pd
import pickle

def run():
    # load model
    with open('model_akhir.pkl', 'rb') as file:
        model = pickle.load(file)
    
    st.title('Predict Player Rating')

    # pembuatan form
    with st.form('player_data'):
        st.write('## Isi Dengan Data Pemain')

        name = st.text_input('Nama Pemain:', placeholder= "John Doe")
        age = st.number_input('Usia Pemain:', min_value = 10, max_value= 100,
                              value = 20 )
        height = st.number_input('Tinggi Badan Pemain:', min_value = 10, max_value= 300,
                              value = 180 )
        weight = st.number_input('Berat Badan Pemain:', min_value = 10,
                                value = 50)
        price = st.number_input('Harga Pemain dalam Euro:', min_value = 10,
                                value = 100000)
        
        attacking_wr = st.select_slider('Attacking Work Rate:', 
                                        ['Low', 'Medium', 'High'], value = 'Medium')
        defensive_wr = st.select_slider('Defensive Work Rate:', 
                                        ['Low', 'Medium', 'High'], value = 'Medium')
        
        # slider
        pace = st.slider('Pace Total:', 0, 100, 50)
        shooting = st.slider('Shooting Total:', 0, 100, 50)
        passing = st.slider('Passing Total:', 0, 100, 50)
        dribbling = st.slider('Dribbling Total:', 0, 100, 50)
        defending = st.slider('Defending Total:', 0, 100, 50)
        physicality = st.slider('Physicality Total:', 0, 100, 50)

        # submit button harus ada untuk form
        predict = st.form_submit_button('Predict')

    data_inf = {
    'Name': name,
    'Age': age,
    'Height': height,
    'Weight': weight,
    'Price': price,
    'AttackingWorkRate': attacking_wr,
    'DefensiveWorkRate': defensive_wr,
    'PaceTotal': pace,
    'ShootingTotal': shooting,
    'PassingTotal': passing,
    'DribblingTotal': dribbling,
    'DefendingTotal': defending,
    'PhysicalityTotal':physicality}

    if predict:
        data = pd.DataFrame([data_inf])
        st.dataframe(data.T, width= 500, height = 500)
        # predict
        prediction = model.predict(data)
        st.write(f'## Rating Pemain: {int(prediction[0])}')


if __name__ == '__main__':
    run()