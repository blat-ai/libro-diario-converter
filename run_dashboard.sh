#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Run the Streamlit dashboard
streamlit run app/streamlit_app.py --server.port 8501 --server.address 0.0.0.0

echo "Dashboard is running at http://localhost:8501"