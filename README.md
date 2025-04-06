<<<<<<< HEAD
# Data Analysis Chatbot

A Streamlit-based chatbot application that helps users analyze and visualize their data using natural language queries.

## Features

- Upload and analyze Excel (.xlsx) or CSV (.csv) files
- Natural language interface for data analysis
- Automatic detection of data issues (missing values, duplicates)
- Interactive visualizations
- Code snippet generation for common analysis tasks
- Retrieval-Augmented Generation (RAG) for enhanced responses

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd data_analysis_chatbot
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (usually http://localhost:8501)

3. Upload your data file (CSV or Excel)

4. Use the chat interface to ask questions about your data, such as:
   - "Show me missing values"
   - "Are there any duplicates?"
   - "What's the distribution of column X?"
   - "Show me correlations between numeric columns"

5. Use the sidebar options for additional analysis and visualizations

## Features in Detail

### Data Analysis
- Automatic detection of missing values
- Duplicate row identification
- Data type validation
- Statistical summaries
- Correlation analysis

### Visualizations
- Distribution plots
- Correlation heatmaps
- Missing value heatmaps
- Value count bar charts

### Code Generation
- Python code snippets for common analysis tasks
- Reproducible analysis code
- Best practices for data cleaning and visualization

## Dependencies

- streamlit
- pandas
- numpy
- seaborn
- matplotlib
- plotly
- openai
- langchain
- python-dotenv
- openpyxl

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 
