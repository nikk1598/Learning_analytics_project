#import os
#import yaml
import streamlit as st
#import uvicorn

CONFIG_PATH = '../config/params.yml'

def main_page():
    """
    Страница с описанием проекта
    :return:
    """
    st.image(
        "https://media.giphy.com/media/uyZPevMqDJ3r76phm1/giphy.gif",
        width=550
    )

    st.markdown("# Описание проекта")
    st.title("MLOps project: Learning Analytics Competition")
if __name__ == "__main__":
    main_page()