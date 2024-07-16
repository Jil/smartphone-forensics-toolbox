# Parse TCC JSON resulting from mvt-ios (yet another Chat GPT 4o generated script)
# install pandas in your venv (pyhton -m venv .env ; source .env/bin/activate)
import pandas as pd
import json
import sys 

if len(sys.argv) != 2:
        print("Usage: python parse_tcc_json.py <file_path>")
        print("Outputs simplified_tcc.csv in the current working directory.")
        sys.exit(1)
    
file_path = sys.argv[1]

# Mapping of TCC service identifiers to readable descriptions
service_mapping = {
    "kTCCServiceUbiquity": "kTCCServiceUbiquity (iCloud Drive)",
    "kTCCServiceSystemPolicyAllFiles": "kTCCServiceSystemPolicyAllFiles (Full Disk Access)",
    "kTCCServiceAppleEvents": "kTCCServiceAppleEvents (Automation)",
    "kTCCServiceLiverpool": "kTCCServiceLiverpool (iCloud data and services)",
    "kTCCServiceWillow": "kTCCServiceWillow (Apple Music and media library)",
}

# Load the JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Map the service identifiers to readable descriptions with a fallback for unknown values
df['service'] = df['service'].map(lambda x: service_mapping.get(x, x))

# Simplify the DataFrame to include only relevant columns
simplified_df = df[['client', 'service', 'auth_value', 'last_modified']]

# Rename columns for better readability
simplified_df.columns = ['App ID', 'Permission', 'Auth Value', 'Last Modified']

# Display the DataFrame
print(simplified_df)

# Optionally, save the simplified DataFrame to a CSV file
simplified_df.to_csv('simplified_tcc.csv', index=False)
