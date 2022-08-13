import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('youtube_nationalist_comments')

#user input 
st.title("NATIONALIST COMMENTS CLASSIFIER")
ip = st.text_input("Enter your message:")

#predict if the entered message is nationalist or not 
op = model_nb.predict([ip])
if st.button('IS NATIONALIST'):
  st.title(op[0])  #prints the output as true if comment is nationalist and false otherwise  
           
