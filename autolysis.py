
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
