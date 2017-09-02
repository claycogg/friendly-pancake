## Pricing Statistics
This is the repository for the question as was posed. I have avoided mentioning the individuals and company involved in
this project so as to reduce search-ability for this repository.

## Instructions
There is no true CLI for this project beyond providing system arguments. I was working on a more complex one but felt
that since I was past the deadline a minimalistic approach was necessary.

The main cli.py file is expecting some command-line args on execution: a file-path and two dates. The dates must be
formatted like the dates in the sample files:

    2017-03-01T13:37:59Z
    yyyy-mm-ddThh:mm:ssZ

python .\cli.py PATH_TO_FILE [DATE1] [DATE2]

Example:

    python .\cli.py data_samples/sample1.txt 2017-03-01T13:37:59Z 2017-05-19T05:49:34Z

## Testing
The testing was done without nose.py in favor of using pure coverage.py. The commands below were executed from Windows
PowerShell in order to verify coverage of the classes in pricestats.py.

    coverage run .\tests.py
    coverage report -m
