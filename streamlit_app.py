# Streamlit Cloud entry point
# This file is required for Streamlit Cloud deployment
import sys
import os

# Ensure the app can find modules
sys.path.insert(0, os.path.dirname(__file__))

# Import and run the main app
from app import *
