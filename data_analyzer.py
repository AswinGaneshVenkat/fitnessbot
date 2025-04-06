import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from rag_handler import RAGHandler

class DataAnalyzer:
    def __init__(self, df):
        self.df = df
        self.rag_handler = RAGHandler()
        
    def analyze(self, query):
        """Analyze the data based on user query"""
        try:
            # Use RAG to get relevant context
            context = self.rag_handler.get_context(query)
            
            # Basic analysis based on query
            if "missing" in query.lower():
                return self.get_missing_values()
            elif "duplicate" in query.lower():
                return self.get_duplicates()
            elif "summary" in query.lower():
                return self.generate_summary()
            elif "distribution" in query.lower():
                # Find column name in query
                for col in self.df.columns:
                    if col.lower() in query.lower():
                        return self.plot_distribution(col)
            else:
                return self.generate_summary() + "\n\n" + context
        except Exception as e:
            return f"Error analyzing data: {str(e)}"
    
    def get_missing_values(self):
        """Get information about missing values"""
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df)) * 100
        missing_info = pd.DataFrame({
            'Missing Values': missing,
            'Percentage': missing_percent
        })
        return f"Missing Values Analysis:\n{missing_info.to_string()}"
    
    def get_duplicates(self):
        """Get information about duplicate rows"""
        duplicates = self.df.duplicated().sum()
        return f"Number of duplicate rows: {duplicates}"
    
    def generate_summary(self):
        """Generate a comprehensive data summary"""
        summary = []
        summary.append(f"Dataset Shape: {self.df.shape}")
        summary.append(f"\nColumn Information:")
        
        for col in self.df.columns:
            dtype = self.df[col].dtype
            unique = self.df[col].nunique()
            missing = self.df[col].isnull().sum()
            
            col_summary = f"\n{col}:"
            col_summary += f"\n  - Data Type: {dtype}"
            col_summary += f"\n  - Unique Values: {unique}"
            col_summary += f"\n  - Missing Values: {missing}"
            
            if pd.api.types.is_numeric_dtype(dtype):
                col_summary += f"\n  - Mean: {self.df[col].mean():.2f}"
                col_summary += f"\n  - Median: {self.df[col].median():.2f}"
                col_summary += f"\n  - Std Dev: {self.df[col].std():.2f}"
            
            summary.append(col_summary)
        
        return "\n".join(summary)
    
    def plot_distribution(self, column):
        """Create a distribution plot for the specified column"""
        if pd.api.types.is_numeric_dtype(self.df[column]):
            fig = px.histogram(self.df, x=column, title=f"Distribution of {column}")
        else:
            value_counts = self.df[column].value_counts()
            fig = px.bar(x=value_counts.index, y=value_counts.values, 
                        title=f"Value Counts for {column}")
        return fig
    
    def plot_correlation(self):
        """Create a correlation heatmap for numeric columns"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) < 2:
            return "Not enough numeric columns for correlation analysis"
        
        corr_matrix = self.df[numeric_cols].corr()
        fig = px.imshow(corr_matrix,
                       title="Correlation Heatmap",
                       labels=dict(x="Columns", y="Columns", color="Correlation"),
                       x=numeric_cols,
                       y=numeric_cols)
        return fig
    
    def validate_data_types(self):
        """Validate data types and identify potential issues"""
        issues = []
        for col in self.df.columns:
            # Check for mixed data types
            if self.df[col].apply(type).nunique() > 1:
                issues.append(f"Column '{col}' has mixed data types")
            
            # Check for numeric columns with non-numeric values
            if pd.api.types.is_numeric_dtype(self.df[col]):
                non_numeric = pd.to_numeric(self.df[col], errors='coerce').isna().sum()
                if non_numeric > 0:
                    issues.append(f"Column '{col}' has {non_numeric} non-numeric values")
        
        return "\n".join(issues) if issues else "No data type issues found" 