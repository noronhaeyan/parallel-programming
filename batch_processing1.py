import pandas as pd

# Function to process each batch
def process_batch(batch_data):

    # Perform data transformations here
    processed_data = batch_data.apply(lambda x: x * 2)  # Example transformation: doubling the values 
    return processed_data

# Read the CSV file in chunks
chunk_size = 10  # Adjust the chunk size as per your system's memory constraints
csv_file = "large_data.csv"  # Replace with your CSV file's path
output_file = "processed_data.csv"  # Replace with the desired output file path

# Read the CSV file in batches and process each batch
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    processed_chunk = process_batch(chunk)
    processed_chunk.to_csv(output_file, mode="a", header=False, index=False)