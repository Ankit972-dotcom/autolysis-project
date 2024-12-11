from google.colab import drive
drive.mount('/content/drive')


import os
project_path = '/content/drive/My Drive/csv-analyzer'
os.makedirs(project_path, exist_ok=True)
os.chdir(project_path)
print("Current working directory:", os.getcwd())


!pip install pandas matplotlib seaborn openai


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai

print("Libraries installed and ready!")


script_content = """
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import sys

def main():
    # Parse command-line arguments
    csv_file = sys.argv[1]

    # Read the CSV file
    data = pd.read_csv(csv_file)
    print(data.head())

    # Perform summary statistics
    summary = data.describe(include='all')
    print(summary)

    # Save a correlation heatmap as an example visualization
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.savefig("correlation_heatmap.png")
    print("Heatmap saved as correlation_heatmap.png")

if __name__ == "__main__":
    main()
"""

with open("autolysis.py", "w") as f:
    f.write(script_content)

print("autolysis.py script created!")


data = pd.read_csv('goodreads.csv')  # Replace with your test CSV file
print(data.head())

!git clone https://github.com/Ankit972-dotcom/autolysis-project.git


!git clone https://github.com/Ankit972-dotcom/autolysis-project.git /content/drive/My\ Drive/autolysis-project # provide the full path for cloning

os.chdir('/content/drive/My Drive/autolysis-project') # Now this directory exists and os.chdir will succeed

!cp /content/drive/My\ Drive/csv-analyzer/autolysis.py /content/drive/My\ Drive/autolysis-project/


import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import sys


openai.api_key = os.getenv("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZHMzMDAwMTEzQGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.UKX59anJvqbwgkM3OCOzMt8RicH3ea8synwexqOsqmc")


import argparse
import sys

if __name__ == "__main__":
    # Check if running in an interactive environment
    if hasattr(sys, 'ps1'):
        # Directly set the CSV file for interactive environments like Colab
        csv_file = "/content/drive/My Drive/csv-analyzer"  # Replace with the actual file path
    else:
        # Use argparse for command-line usage
        parser = argparse.ArgumentParser(description="Automated analysis of CSV data.")
        parser.add_argument("csv_file", help="The CSV file to analyze")
        args = parser.parse_args()
        csv_file = args.csv_file

    print(f"Analyzing file: {csv_file}")


import argparse

# Check if running in an interactive environment
if __name__ == "__main__" and not hasattr(sys, 'ps1'):
    # Only parse arguments if running as a script
    parser = argparse.ArgumentParser(description="Automated analysis of CSV data.")
    parser.add_argument("csv_file", help="The CSV file to analyze")
    args = parser.parse_args()
    # Now you can access the CSV file path using args.csv_file
    csv_file = args.csv_file
    print(f"Analyzing file: {csv_file}")
else:
    # For interactive environments, set the CSV file path directly
    csv_file = "/content/drive/My Drive/csv-analyzer/goodreads.csv"  # Replace with the actual file path
    print(f"Analyzing file: {csv_file}")

# Instead of using args.csv_file, use the csv_file variable
# which is already defined in the previous cell
data = pd.read_csv(csv_file)

summary_stats = data.describe(include='all')
missing_values = data.isnull().sum()


# Select only numerical columns before calculating correlation
numerical_data = data.select_dtypes(include=['number'])
correlation_matrix = numerical_data.corr()

sns.heatmap(correlation_matrix, annot=True)
plt.savefig("correlation_heatmap.png")


# Replace 'column_name' with an actual column name from your DataFrame
sns.histplot(data['book_id'], kde=True)  # Example: Replace 'book_id' with your desired column
plt.savefig("distribution_plot.png")

!pip install --upgrade openai==0.28 # Install older version

!pip install requests


import requests
import os

# Replace with your AIPROXY_TOKEN (Do not expose your token publicly)
AIPROXY_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZHMzMDAwMTEzQGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.UKX59anJvqbwgkM3OCOzMt8RicH3ea8synwexqOsqmc'

# Set the headers for authentication
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {AIPROXY_TOKEN}'
}

# Prepare the data for the request
data = {
    'model': 'gpt-4o-mini',  # You can change this to another supported model if needed
    'messages': [
        {'role': 'user', 'content': 'Analyze the following dataset: summary stats and missing values.'}
    ]
}

# Send the request to the AI Proxy API for chat completions
response = requests.post(
    'https://aiproxy.sanand.workers.dev/openai/v1/chat/completions',  # AI Proxy endpoint
    headers=headers,
    json=data
)

# Check if the response is successful
if response.status_code == 200:
    result = response.json()
    print("Response from AI Proxy:")
    print(result['choices'][0]['message']['content'])  # The generated message
else:
    print(f"Error: {response.status_code}, {response.text}")
