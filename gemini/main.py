## Integrate our code OpenAI API


import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

#customize here

st.markdown("<h1 style='text-align: center;'>DDS Python Tutor Bot</h1>", unsafe_allow_html=True)
input_text = st.text_input("Search the Python topic you want to Understand", key="input_text", value="")



## Prmpt Template

first_input_template = PromptTemplate (
    input_variables =['name'],
    template = "Explain me about the topic {name} in python in a simple manner to a 6th grader with a code syntax and elaborate example"
)

## OPENAI LLMS
llm=OpenAI(temperature=0.0)
##chain

chain=LLMChain(llm=llm ,prompt=first_input_template ,verbose=True)




# Search button
if st.button('Search'):
    if input_text:
        st.write(chain.run(input_text))

# Reset button
if st.button('Reset'):
    input_text = ''