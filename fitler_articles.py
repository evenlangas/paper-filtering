import pandas as pd
import os

def filter_high_citation_articles_in_folder(folder_path, output_file, citation_threshold=20, sjr_file=None):
    """
    Filters articles with citations (Z9) greater than a given threshold and filters by SJR ranking (Q1 or Q2)
    using an external SJR file. Combines filtered results from all TSV files in a folder and saves to a single CSV file.

    Parameters:
        folder_path (str): Path to the folder containing TSV files.
        output_file (str): Path to the output CSV file.
        citation_threshold (int): Minimum number of citations required to include an article.
        sjr_file (str): Path to the SJR file (CSV) for cross-referencing journal rankings.
    """
    # Load the SJR file
    if sjr_file:
        try:
            sjr_df = pd.read_csv(sjr_file, sep=';', dtype=str)
            sjr_df = sjr_df[sjr_df['SJR Best Quartile'].isin(['Q1', 'Q2'])]
            sjr_journals = set(sjr_df['Title'].str.lower())
        except Exception as e:
            print(f"Error loading SJR file: {e}")
            return
    else:
        print("SJR file is required for filtering.")
        return

    all_filtered_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            try:
                # Read the input file with flexible options
                df = pd.read_csv(
                    file_path,
                    sep='\t',  # Assuming tab-separated
                    engine='python',
                    quoting=3,  # Ignore quotes
                    escapechar='\\',  # Handle escape characters
                    dtype=str  # Read everything as string for troubleshooting
                )
                print(f"Processing file: {filename}")
            except Exception as e:
                print(f"Error reading the file {filename}: {e}")
                continue

            # Handle columns
            if 'Z9' not in df.columns or 'SO' not in df.columns:
                print(f"Error: Required columns ('Z9', 'Journal') not found in the file {filename}. Columns found: {df.columns}")
                continue

            # Ensure Z9 is numeric
            df['Z9'] = pd.to_numeric(df['Z9'], errors='coerce')
            
            # Filter rows based on the citation threshold
            filtered_df = df[df['Z9'] > citation_threshold]

            # Filter by SJR ranking
            filtered_df = filtered_df[filtered_df['SO'].str.lower().isin(sjr_journals)]

            print(df['SO'])
            # Append to the list of all filtered data
            all_filtered_data.append(filtered_df)

    # Combine all filtered data into a single DataFrame
    if all_filtered_data:
        combined_df = pd.concat(all_filtered_data, ignore_index=True)
        try:
            # Save the combined data to the output CSV file
            combined_df.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"Filtered data from all files saved to {output_file}")
        except Exception as e:
            print(f"Error writing to the output file: {e}")
    else:
        print("No data to save. No articles met the citation and SJR criteria.")

# Example usage
# Replace 'folder_path', 'output_file_path.csv', and 'sjr_file_path.csv' with actual paths
filter_high_citation_articles_in_folder(
    folder_path="./wos_exports",
    output_file="filtered_articles.csv",
    citation_threshold=20,
    sjr_file="sjr_file.csv"
)