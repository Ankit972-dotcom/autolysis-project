import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import chardet  # Import chardet to detect encoding

def main():
    # Specify the dataset file name
    csv_file = "media.csv"  # Change this to the file name of your dataset

    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"Error: The file '{csv_file}' does not exist in the current directory.")
        return

    # Read the CSV file
    print(f"Reading data from '{csv_file}'...")
    
    # Detect file encoding using chardet
    with open(csv_file, 'rb') as rawdata:
        result = chardet.detect(rawdata.read())
    encoding = result['encoding']

    data = pd.read_csv(csv_file, encoding=encoding)  # Pass encoding to read_csv

    # Display the first few rows of the dataset
    print("Dataset Preview:")
    print(data.head())

    # Perform summary statistics
    print("\nGenerating summary statistics...")
    summary = data.describe(include='all')
    print(summary)

    # Save the summary statistics to a CSV file
    summary_filename = "media_summary.csv"
    summary.to_csv(summary_filename)
    print(f"Summary statistics saved to '{summary_filename}'.")

    # Generate a correlation heatmap
    print("\nCreating correlation heatmap...")
    
    # Convert date columns to datetime objects
    # Replace 'Date' with the actual name of your date column
    date_columns = ['Date']  # List of columns containing date values
    for col in date_columns:
        if col in data.columns:  # Check if column exists in DataFrame
            data[col] = pd.to_datetime(data[col])

    # Select only numerical features for correlation analysis
    numerical_data = data.select_dtypes(include=['number']) 
    
    correlation_matrix = numerical_data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    heatmap_filename = "media_correlation_heatmap.png"
    plt.title("Correlation Heatmap")
    plt.savefig(heatmap_filename)
    plt.close()
    print(f"Heatmap saved as '{heatmap_filename}'.")

    # Generate a distribution plot for a numerical column
    print("\nCreating distribution plot...")
    # Replace 'column_name' with the name of a numerical column from your dataset
    numerical_columns = data.select_dtypes(include='number').columns
    if len(numerical_columns) > 0:
        column_name = numerical_columns[0]  # Automatically selects the first numerical column
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column_name], kde=True, bins=20, color='green')
        plt.title(f"Distribution Plot for {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        distplot_filename = f"{column_name}_distribution_plot.png"
        plt.savefig(distplot_filename)
        plt.close()
        print(f"Distribution plot saved as '{distplot_filename}'.")
    else:
        print("No numerical columns found for distribution plot.")

    print("\nAnalysis completed successfully!")

if __name__ == "__main__":
    main()
