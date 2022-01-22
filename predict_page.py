import streamlit as st
import numpy as np
import pickle
import sklearn

def load_model():
    with open('Saved_step.pkl',"rb")as file:
         data=pickle.load(file)
    return data
    

data=load_model()

regressor=data['model']
lb_country=data["lb_country"]
lb_edlevel=data["lb_edlevel"]


def show_predict_page():
    st.title("Data Scientist Annual Salary prediction")

    st.write("""### We need some information to predict""")

    countries=(
        "United States",       
        "India",              
        "United Kingdom",         
        "Germany",           
        "Canada",                
        "Brazil",                 
        "France",               
        "Netherlands",             
        "Poland",                
        "Australia",               
        "Spain",                   
        "Italy",                 
        "Russian Federation",     
        "Sweden" 
    )

    education=(
        'Bachelor’s degree', 
        'Master’s degree',
        'Less than a bachelor',
        'Post grad'
    )

    country = st.selectbox('Country',countries)
    education = st.selectbox('Education',education)


    experience=st.slider('Years of experience',0,50,3)
    
    ok =st.button('Calculate Salary')
    if ok:
        Features= np.array([[country,education,experience]])
        Features[:,0]=lb_country.transform(Features[:,0])
        Features[:,1]=lb_edlevel.transform(Features[:,1])
        Features = Features.astype(float)
        
        Salary=regressor.predict(Features)
        st.subheader(f'The estimated salary is ${Salary[0]:,.2f}')

   


