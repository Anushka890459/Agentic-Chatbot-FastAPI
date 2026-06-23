#!/bin/bash

# Start FastAPI Backend in the background on port 9999
python backend.py &

# Start Streamlit Frontend in the foreground on port 8501
streamlit run frontend.py --server.port=8501 --server.address=0.0.0.0