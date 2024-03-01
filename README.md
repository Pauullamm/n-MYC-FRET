# n-MYC-FRET
A simple Python script that automates calculations of ensemble single-molecule FRET csv data obtained from Oxford Nanoimager

Mote: Unfortunately raw csv files that are exported from the Nanoimager software contain additional lines at the start of the excel sheet which cannot be parsed by pandas.
To avoid this, delete the first few lines until the row showing the trace IDs.
