# Systematic Review Pipeline for High-Citation Articles in Q1 and Q2 Journals

This repository provides a Python-based pipeline for conducting systematic reviews of high-citation articles from Web of Science (WoS) journals ranked Q1 or Q2 according to the Scientific Journal Rankings (SJR). It includes a step-by-step methodology, requirements, and usage instructions for the provided script.

---

## Methodology

### Step 1: Exporting Articles from Web of Science

**Perform Initial Search**:
   - Log into the [Web of Science Core Collection](https://www.webofscience.com/).
   - Define search terms relevant to your topic (e.g., "Industry 5.0" or "Digital Twins").
   - Apply filters for years **2020-2024** to ensure recent studies.
   - Export the results in `Tab Delimited File` format (`.txt`). Under `Record Content`, select `Full Record` to ensure the output contains all metadata, including `Journal Title` (SO), `Citations` (Z9), and other relevant fields.

<!-- 2. **Filter Articles by Citations**:
   - Select articles with **Z9 (number of citations) > 20** for higher relevance. -->

---

### Step 2: Downloading the SJR CSV File

Visit the [SJR website](https://www.scimagojr.com/) and download the most recent journal rankings in CSV format.
   - Ensure the CSV file includes columns like `Title`, `SJR`, and `SJR Best Quartile`.
   - Save the file as `sjr_file.csv` in the working directory.

<!-- 2. Filter for journals ranked **Q1** and **Q2**. -->

---

### Step 3: Python Script Workflow

#### Overview of the Python Script

This Python script processes exported `.txt` files from Web of Science, cross-checks journals against the SJR rankings, and applies citation filters. The script outputs a CSV file containing only the articles that meet the specified criteria.

1. **Input Files**:
   - Folder containing `.txt` files exported from Web of Science.
   - The `sjr_file.csv` file with Q1 and Q2 journal rankings.

2. **Processing Steps**:
   - Load and parse `.txt` files from the specified folder.
   - Validate that the `Z9` (citations) and `Journal` (SO) columns exist.
   - Filter articles based on:
     - Citation count greater than e.g. **20**.
     - Journals ranked as Q1 or Q2 in the SJR data.
   - Combine the filtered results from all `.txt` files into a single CSV file.

3. **Output**:
   - A single CSV file containing filtered articles.

---

## How to Use the Script

### Prerequisites

- Python 3.7+
- Required libraries: `pandas`, `os`

Install the required libraries using pip:
```bash
pip install pandas
```

### Script Usage

1. **Place Files in the Correct Folder**:
   - Save your `.txt` files exported from Web of Science in a dedicated folder.
   - Save the `sjr_file.csv` in the same directory or specify its path.

2. **Run the Script**:
   - Edit the `folder_path` and `sjr_file_path` variables in the script to match your file locations.
   - Execute the script:
     ```bash
     python filter_articles.py
     ```

3. **Specify Parameters**:
   - You can modify the following parameters:
     - `folder_path`: Path to the folder containing `.txt` files.
     - `output_file`: Path to the output CSV file.
     - `citation_threshold`: Minimum number of citations (default is 20).
     - `sjr_file`: Path to the SJR CSV file.

### Example Configuration

```python
filter_high_citation_articles_in_folder(
    folder_path="./wos_exports",
    output_file="filtered_articles.csv",
    citation_threshold=20,
    sjr_file="sjr_file.csv"
)
```

### Output

- The output CSV file, `filtered_articles.csv`, will contain:
  - Articles published in Q1 or Q2 journals.
  - Articles with more than 20 citations.

---

## Example Workflow

1. **Input Data**:
   - `wos_exports/`: Folder containing `.txt` files from Web of Science.
   - `sjr_file.csv`: CSV file of SJR journal rankings.

2. **Command**:
   ```bash
   python script.py
   ```

3. **Output File**:
   - `filtered_articles.csv` containing the final curated list of articles.

---

## Notes and Tips

- Ensure that the `Journal` (SO) field in the `.txt` files matches the `Title` field in the SJR file.
- If you encounter errors, verify the file formats and column names.
- Use the script iteratively to refine filters and achieve desired results.

---

Feel free to raise issues or contribute to this repository by submitting pull requests or suggestions.

