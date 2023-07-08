import streamlit as st
from bardapi import Bard
import os

os.environ["_BARD_API_KEY"] = "YAgjeMPVabFgw6DJFnFsesPrDxnRBc9ls8M8OlkmKca_7R06wa9TcIzyzr3dp9OOadNpcg."
st.header("Abozekry's AI")

prompt = st.text_input('', 'Enter a prompt')

def open_exe(exe_path):
  os.startfile(exe_path)

if "sublime" in message:
    open_exe("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
    print("opening sublime")
elif "vs" in message:
    open_exe('C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
    print("opening visual studios code")
elif "pycharm" in message:
    open_exe("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.3\\bin\\pycharm64.exe")
    print("PyCharm")
elif "qtd" in message:
    open_exe()
else:
    st.text((Bard().get_answer(str(prompt))['content']))

#print(Bard().get_answer(str(message))['content'])
