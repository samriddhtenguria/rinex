import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('')

#user input 
st.title("COMMENTS CLASSIFIER")
ip = st.text_input("Enter your message:")

#predict if the entered message is spam or ham 
op = model_nb.predict([ip])
if st.button('TRUE/FALSE'):
  st.title(op[0])  #prints the output as spam or ham  

       
                                    
  
