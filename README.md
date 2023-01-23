# n-MYC-FRET
A simple Python script that automates calculations of ensemble single-molecule FRET CSV data obtained from Oxford Nanoimager

Raw csv files that are exported from the Nanoimager software contain additional lines at the start of the excel sheet which cannot be parsed by pandas.
To avoid this, delete the first few lines until the row showing the trace IDs.
There is probably a way around to edit the code to remove these lines for us, but I am a tired university student with insufficient time to figure this out. This is the next best option.
