from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
import os

class RAGHandler:
    def __init__(self):
        try:
            # Get API key from environment
            self.api_key = os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            
            # Debug: Print the API key (first 10 characters)
            print(f"RAGHandler API Key (first 10 chars): {self.api_key[:10]}")
            
            if not self.api_key.startswith("sk-"):
                raise ValueError("Invalid OpenAI API key format. API key should start with 'sk-'")
            
            # Initialize OpenAI components with correct parameters
            try:
                self.embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
                self.llm = OpenAI(openai_api_key=self.api_key, temperature=0)
            except Exception as e:
                raise ValueError(f"Error initializing OpenAI components: {str(e)}")
            
            # Create or load vector store
            self.vector_store = self._create_vector_store()
        except Exception as e:
            raise ValueError(f"Error initializing RAGHandler: {str(e)}")
    
    def _create_vector_store(self):
        """Create a vector store with relevant documentation"""
        # Example documentation about data analysis
        docs = [
            "Pandas is a powerful data analysis library in Python.",
            "Use df.describe() to get statistical summary of numeric columns.",
            "df.isnull().sum() shows the count of missing values in each column.",
            "df.duplicated().sum() counts duplicate rows in the dataset.",
            "Use df.corr() to calculate correlation between numeric columns.",
            "df.dtypes shows the data type of each column.",
            "df.nunique() counts unique values in each column.",
            "Use df.groupby() to group data by specific columns.",
            "df.pivot_table() creates pivot tables for data analysis.",
            "Use df.plot() for basic plotting functionality.",
            "Seaborn and Plotly provide advanced visualization capabilities.",
            "Data cleaning involves handling missing values and outliers.",
            "Feature engineering creates new features from existing ones.",
            "Data validation ensures data quality and consistency.",
            "Exploratory Data Analysis (EDA) helps understand data patterns."
        ]
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.create_documents(docs)
        
        # Create vector store
        vector_store = FAISS.from_documents(texts, self.embeddings)
        return vector_store
    
    def get_context(self, query):
        """Get relevant context for the query"""
        try:
            # Create retrieval chain
            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store.as_retriever()
            )
            
            # Get response
            response = qa_chain.run(query)
            return response
        except Exception as e:
            return f"Error getting context: {str(e)}"
    
    def generate_code_snippet(self, analysis_type):
        """Generate Python code snippet for common analysis tasks"""
        code_snippets = {
            "missing_values": """
# Count missing values
missing_values = df.isnull().sum()
missing_percent = (missing_values / len(df)) * 100

# Visualize missing values
import seaborn as sns
sns.heatmap(df.isnull(), cbar=False)
plt.title('Missing Values Heatmap')
plt.show()
            """,
            "duplicates": """
# Find duplicate rows
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Remove duplicates
df_clean = df.drop_duplicates()
            """,
            "correlation": """
# Calculate correlation matrix
correlation_matrix = df.corr()

# Visualize correlation
import seaborn as sns
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
            """,
            "distribution": """
# Plot distribution for numeric columns
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    sns.histplot(data=df, x=col)
    plt.title(f'Distribution of {col}')
    plt.show()
            """
        }
        
        return code_snippets.get(analysis_type, "No code snippet available for this analysis type") 