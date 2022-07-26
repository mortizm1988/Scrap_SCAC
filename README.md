# Scrap_SCAC
This code downloads legal filings from Securities Class Action Clearinghouse (SCAC) and stores them in a CSV file.
Use with civic responsibility for research and education only.

# Running Instructions
 1. Clone the repository
 2. In file 'Scrapper.py', add the username and password used in [SCAC ](https://securities.stanford.edu/index.html)
 3. Run 'Scrapper.py'
 
An important part of the code is borrowed from [Kai Chen's website](http://kaichen.work/?p=1032). I appreciated that Kai made his code available.
I added extra variable extraction (judge, docket, industry, sector, class period dates, case summary) and modified part of the original code by encapsulating better the function and variable scopes. 
