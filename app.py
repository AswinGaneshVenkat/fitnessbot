import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from data_analyzer import DataAnalyzer
from rag_handler import RAGHandler
import os

# Set page config - MUST be the first Streamlit command
st.set_page_config(
    page_title="Data Analysis Chatbot",
    page_icon="📊",
    layout="wide"
)

# Set OpenAI API key directly
OPENAI_API_KEY = "OPENAI_API_KEY"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Debug: Print the API key (first 10 characters)
st.write(f"API Key (first 10 chars): {OPENAI_API_KEY[:10]}")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'df' not in st.session_state:
    st.session_state.df = None
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = None
if 'rag_error' not in st.session_state:
    st.session_state.rag_error = None

# Title and description
st.title("📊 Data Analysis Chatbot")
st.markdown("""
    Upload your Excel or CSV file and ask questions about your data. 
    The chatbot will help you analyze and visualize your data.
""")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.session_state.df = df
        try:
            st.session_state.analyzer = DataAnalyzer(df)
            st.session_state.rag_error = None
        except ValueError as e:
            st.session_state.rag_error = str(e)
            st.error(f"Error initializing analyzer: {str(e)}")
        
        st.success("File uploaded successfully!")
        st.write(f"Shape of the dataset: {df.shape}")
        
        # Display basic info
        st.subheader("Dataset Preview")
        st.dataframe(df.head())
        
        # Display column information
        st.subheader("Column Information")
        col_info = pd.DataFrame({
            'Column': df.columns,
            'Data Type': df.dtypes.astype(str),  # Convert dtypes to string
            'Non-Null Count': df.count(),
            'Unique Values': df.nunique()
        })
        st.dataframe(col_info)
        
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")

# Chat interface
st.subheader("Chat with your data")
user_input = st.text_input("Ask a question about your data", key="user_input")

if user_input and st.session_state.df is not None:
    if st.session_state.rag_error:
        st.error(f"Chat functionality is disabled due to: {st.session_state.rag_error}")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            # Get response from analyzer
            response = st.session_state.analyzer.analyze(user_input)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error getting response: {str(e)}")
        
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

# Sidebar for additional options
with st.sidebar:
    st.header("Analysis Options")
    
    if st.session_state.df is not None:
        if st.button("Generate Data Summary"):
            if st.session_state.analyzer is None:
                st.error("Analyzer not initialized. Please check your API key and try again.")
            else:
                try:
                    summary = st.session_state.analyzer.generate_summary()
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error generating summary: {str(e)}")
        
        if st.button("Show Missing Values"):
            if st.session_state.analyzer is None:
                st.error("Analyzer not initialized. Please check your API key and try again.")
            else:
                try:
                    missing = st.session_state.analyzer.get_missing_values()
                    st.write(missing)
                except Exception as e:
                    st.error(f"Error getting missing values: {str(e)}")
        
        if st.button("Show Duplicates"):
            if st.session_state.analyzer is None:
                st.error("Analyzer not initialized. Please check your API key and try again.")
            else:
                try:
                    duplicates = st.session_state.analyzer.get_duplicates()
                    st.write(duplicates)
                except Exception as e:
                    st.error(f"Error getting duplicates: {str(e)}")
        
        # Visualization options
        st.subheader("Visualizations")
        selected_column = st.selectbox("Select column for visualization", st.session_state.df.columns)
        
        if st.button("Show Distribution"):
            if st.session_state.analyzer is None:
                st.error("Analyzer not initialized. Please check your API key and try again.")
            else:
                try:
                    fig = st.session_state.analyzer.plot_distribution(selected_column)
                    st.plotly_chart(fig)
                except Exception as e:
                    st.error(f"Error creating distribution plot: {str(e)}")
        
        if st.button("Show Correlation Heatmap"):
            if st.session_state.analyzer is None:
                st.error("Analyzer not initialized. Please check your API key and try again.")
            else:
                try:
                    fig = st.session_state.analyzer.plot_correlation()
                    st.plotly_chart(fig)
                except Exception as e:
                    st.error(f"Error creating correlation heatmap: {str(e)}") 