import pandas as pd

# Read in the cons.csv file
cons_df = pd.read_csv('cons.csv', dtype={'is_deleted': 'bool'})

# Filter out deleted constituents
cons_df = cons_df[~cons_df.is_deleted]

# Convert created_dt column to datetime format
cons_df['created_dt'] = pd.to_datetime(cons_df['created_dt'])

# Group constituents by acquisition date and count the number of acquisitions per date
acq_facts_df = cons_df.groupby(cons_df['created_dt'].dt.date)['cons_id'].count().reset_index()

# Rename columns to match required schema
acq_facts_df = acq_facts_df.rename(columns={'created_dt': 'acquisition_date', 'cons_id': 'acquisitions'})

# Save to CSV file with header
acq_facts_df.to_csv('acquisition_facts.csv', index=False)
