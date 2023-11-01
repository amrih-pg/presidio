import streamlit as st
import pandas as pd
import numpy as np

# Install Presidio dependencies
st.system("python -m spacy download en_core_web_lg")
st.title('Presidio testing')

# Import other necessary libraries
import presidio_analyzer
import presidio_anonymizer
import spacy


# Run the Streamlit app
if __name__ == "__main__":
    st.run_app()