import streamlit as st
from bardapi import Bard
import os

os.environ["_BARD_API_KEY"] = "YAgjeMPVabFgw6DJFnFsesPrDxnRBc9ls8M8OlkmKca_7R06wa9TcIzyzr3dp9OOadNpcg."
st.header("Abozekry's AI")

prompt = st.text_input('', 'Enter a prompt')

def open_exe(exe_path):
  os.startfile(exe_path)

st.text((Bard().get_answer(str(prompt))['content']))

#print(Bard().get_answer(str(message))['content'])
