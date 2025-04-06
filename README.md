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
=======
# Fitness Assistant Chatbot

## Overview
The **Fitness Assistant Chatbot** is an AI-powered chatbot designed to create a **customized 120-day fitness plan** based on user responses. It interacts with users through a chat interface, gathering relevant fitness details and generating structured workout and diet plans. Built using **Streamlit** and **OpenAI GPT-4**, this chatbot ensures a smooth and interactive experience.

## Features
- **Interactive Chat Interface** 💬
  - Engages users step-by-step to build their fitness plan.
- **Personalized 120-Day Fitness Plan** 🏋️‍♂️
  - Includes workout routines, meal recommendations, and recovery tips.
- **Unique Weight Input Handling** ⚖️
  - Ensures the user specifies kg/lbs before proceeding.
- **Restricts Non-Fitness Queries Post Finalization** 🚫
  - After generating the plan, the chatbot will only respond to fitness-related queries.

## Installation & Setup
### Prerequisites
- Python
- OpenAI API Key
- Streamlit

    ```
   Run the chatbot:
   python -m streamlit run fitnessBot.py
   ```


## License
This project is licensed under the **MIT License**.

>>>>>>> c072262606821e162e2b7df89da55bc73e42bcbb
