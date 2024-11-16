import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl', 'rb'))

introduction = """
### About This Project:

This is a machine learning app built using the Iris dataset. The model uses a Decision Tree Classifier  
to predict the species of an Iris flower based on the four features: Sepal Length, Sepal Width, Petal Length,  
and Petal Width. You can input these values and the model will predict the corresponding species.
"""

def display_instruction_window():
    with st.expander("💡 Information about the features", expanded=False):
        st.markdown("""
            #### Terminologies:
            1. SepalLengthCm: Length of the sepal (in cm).
            2. SepalWidthCm: Width of the sepal (in cm).
            3. PetalLengthCm: Length of the petal (in cm).
            4. PetalWidthCm: Width of the petal (in cm).
            """)

def page():
    st.title("Iris Flower Species Prediction")
    st.markdown(introduction)

page()
display_instruction_window()

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input('Enter the Sepal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)
    petal_length = st.number_input('Enter the Petal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)

with col2:
    sepal_width = st.number_input('Enter the Sepal Width (cm)', min_value=0.0, max_value=10.0, step=0.1)
    petal_width = st.number_input('Enter the Petal Width (cm)', min_value=0.0, max_value=10.0, step=0.1)

if st.button('Predict'):

    input_features = [[sepal_length, sepal_width, petal_length, petal_width]]

    prediction = model.predict(input_features)

    predicted_species = [prediction[0]]
    st.write(f'The predicted species is: **{predicted_species[0]}**')
