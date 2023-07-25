# information-extractor-from-scientific-articles-on-the-internet-using-Chatgpt-prototype-
I have created this small program in python that scrapes the html structure through links of scientific articles, the main function of the program is to query the Chatgpt API so that the language model extracts the relevant information from the scientific articles. The program has a sqlite3 database, the option of using proxies to perform the query to the links and the use of multiprocesses to speed up the procedure.
Insert your OpenAI API KEY in the .env file, then it will be read as an environment variable. As for the links to scrape they must be placed in the links.txt file and the proxies in proxies.txt.
