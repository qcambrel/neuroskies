import streamlit as st

from datasets.uploader import S3Uploader

st.title("Neuroskies")

session: str = None
session_type: str = "forecast"

persistence_token: str = st.text_input("Token", type="password")

upload_file: bytes = st.file_uploader("Upload NetCDF file", type=["nc", "nc4"])

selected_model: str = st.selectbox("Select a model", ["Nevergrad", "PSO"])

if upload_file is not None:
    st.write(upload_file)
    file_id: str = None
    uploader: S3Uploader = S3Uploader("neuroskies")
    key: str = f"{session_type}/{session}/{file_id}"
    uploader.upload_fileobj(upload_file, key)