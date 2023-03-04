import pandas as pd

# read in constituent information and email data
cons = pd.read_csv('https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv')
email = pd.read_csv('https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv')

# merge constituent information and email data on cons_id
cons_email = pd.merge(cons, email, on='cons_id')

# read in constituent subscription status data
sub_status = pd.read_csv('https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv')

# keep only subscription status where chapter_id is 1
sub_status = sub_status[sub_status['chapter_id'] == 1]

# fill in missing subscription status with is_unsub = False
sub_status = sub_status.fillna({'is_unsub': 0})

# merge subscription status with cons_email on cons_email_id and email_id
cons_email_sub = pd.merge(cons_email, sub_status, on=['cons_email_id', 'email_id'], how='left')

# keep only relevant columns
people = cons_email_sub[['email', 'source', 'is_unsub', 'created_dt', 'updated_dt']]

# rename columns
people.columns = ['email', 'code', 'is_unsub', 'created_dt', 'updated_dt']

# save people file as CSV with header
people.to_csv('people.csv', index=False, header=True)
