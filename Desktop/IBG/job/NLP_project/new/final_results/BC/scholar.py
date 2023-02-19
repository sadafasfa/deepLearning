# ####################get scholars publications just abstracts are incomplete##################### it worked but the second time got nothing maybe sholar band me

# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# # Specify the base URL of the Google Scholar search results page
# base_url = 'https://scholar.google.com/scholar'

# # Specify the search query
# query = ('("DNA damage response" OR "DDR" OR "response to DNA damage") AND '
#          '("Pulmonary Cancer" OR "Lung Neoplasms" OR "Pulmonary Neoplasms" OR "Cancer of the Lung") AND '
#          '("tissue" OR "tissues" OR "tissue sample") AND '
#          '("lesions" OR "lesions" OR "damage" OR "injury" OR "injuries") NOT '
#          '("Chemotherapy" OR "Drug therapy" OR "Drug treatment" OR "Radiation therapy" OR "Radiotherapy" OR "Surgery")')

# # Set the starting index of search results to 0
# start = 0

# # Create an empty list to hold the results
# results = []

# # Loop through all the pages of search results
# while True:
#     # Define the parameters for the current page of search results
#     params = {
#         'hl': 'en',
#         'as_sdt': '0,5',
#         'q': query,
#         'start': start
#     }

#     # Send a GET request to the current page of search results and parse the response using BeautifulSoup
#     response = requests.get(base_url, params=params)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find all the search results on the page
#     search_results = soup.find_all('div', {'class': 'gs_r gs_or gs_scl'})

#     # If no search results are found, break out of the loop
#     if len(search_results) == 0:
#         break

#     # Loop through each search result and extract the title, abstract, and year
#     for result in search_results:
#         title = result.find('h3', {'class': 'gs_rt'}).text
#         abstract = result.find('div', {'class': 'gs_rs'}).text
#         year = result.find('div', {'class': 'gs_a'}).text.split(' - ')[-1].strip()
#         results.append({'Title': title, 'Abstract': abstract, 'Year': year})

#     # Increment the starting index of search results by 10 to move to the next page
#     start += 10

# # Create a pandas DataFrame from the results list
# df = pd.DataFrame(results)

# # Print the DataFrame
# print(df)


# Print the DataFrame
#print(df)

# Save the DataFrame to a excel file
#df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/output.xlsx')

####################get abstracts as well with slenium but timed out and did not work#####################
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# # Set up ChromeDriver
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# service = Service('/usr/local/bin/chromedriver')
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Specify the base URL of the Google Scholar search results page
# base_url = 'https://scholar.google.com/scholar'

# # Specify the search query
# query = ('("DNA damage response" OR "DDR" OR "response to DNA damage") AND '
#          '("Pulmonary Cancer" OR "Lung Neoplasms" OR "Pulmonary Neoplasms" OR "Cancer of the Lung") AND '
#          '("tissue" OR "tissues" OR "tissue sample") AND '
#          '("lesions" OR "lesions" OR "damage" OR "injury" OR "injuries") NOT '
#          '("Chemotherapy" OR "Drug therapy" OR "Drug treatment" OR "Radiation therapy" OR "Radiotherapy" OR "Surgery")')

# # Set the starting index of search results to 0
# start = 0

# # Create an empty list to hold the results
# results = []

# # Loop through search results until no more results are found
# while True:

#     # Define the URL for the current search request
#     url = f'{base_url}?hl=en&as_sdt=0,5&start={start}&q={query}'

#     # Load the Google Scholar page
#     driver.get(url)

#     # Wait for the search results to load
#     wait = WebDriverWait(driver, 10)
#     try:
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gs_ri')))
#     except TimeoutException:
#         print("Timed out waiting for page to load")
#         continue

#     # Find all of the search result elements on the page
#     search_results = driver.find_elements(By.CLASS_NAME, 'gs_ri')

#     # If no more search results are found, break out of the loop
#     if len(search_results) == 0:
#         break

#     # Extract the title, abstract, and year for each search result
#     for result in search_results:
#         title = result.find_element(By.CLASS_NAME, 'gs_rt').text.strip()
#         abstract = result.find_element(By.CLASS_NAME, 'gs_rs').text.strip()
#         year = result.find_element(By.CSS_SELECTOR, '.gs_a').text.strip().split()[-1]

#         # Append the title, abstract, and year to the results list
#         results.append({'Title': title, 'Abstract': abstract, 'Year': year})

#     # Increment the starting index for the next search request
#     start += 10

# # Close the ChromeDriver
# driver.quit()

# # Create a DataFrame from the results list
# df = pd.DataFrame(results)

# # Print the DataFrame
# print(df)


# # Save the DataFrame to a excel file
# df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/output_selen.xlsx')


################get compelet abstract from title############# did not work
# import pandas as pd
# import retrying
# import requests
# from retrying import retry

# # Define the base URL of the CrossRef API
# base_url = 'https://api.crossref.org/works'

# # Load the DataFrame from the Excel file
# df = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/output.xlsx')

# # Define the retry strategy
# @retry(stop_max_attempt_number=3, wait_fixed=2000)
# def get_abstract(title):
#     # Define the query parameters for the CrossRef API
#     params = {'query.bibliographic': title}

#     # Send a GET request to the CrossRef API with the query parameters and a timeout of 10 seconds
#     response = requests.get(base_url, params=params, timeout=10)

#     # Raise an exception if the status code is not 200 (OK)
#     response.raise_for_status()

#     # Parse the JSON response and get the abstract
#     data = response.json()
#     if 'abstract' in data['message']['items'][0]:
#         abstract = data['message']['items'][0]['abstract']
#         return abstract
#     else:
#         return None

# # Loop through each row in the DataFrame
# for i, row in df.iterrows():
#     # Get the title of the current row
#     title = row['Title']

#     # Call the get_abstract function with the title and retry if it fails
#     try:
#         abstract = get_abstract(title)
#     except:
#         abstract = None

#     df.at[i, 'Abstract'] = abstract

# # Save the updated DataFrame to an Excel file
# df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/output_with_abstracts.xlsx')

#######does not work I wanted to get part by part abstracts#################
# import pandas as pd
# import retrying
# import requests
# from retrying import retry

# # Define the base URL of the CrossRef API
# base_url = 'https://api.crossref.org/works'

# # Load the DataFrame from the Excel file
# df = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/Title.xlsx')

# # Define the retry strategy
# @retry(stop_max_attempt_number=3, wait_fixed=2000)
# def get_abstract(title):
#     # Define the query parameters for the CrossRef API
#     params = {'query.bibliographic': title}

#     # Send a GET request to the CrossRef API with the query parameters and a timeout of 10 seconds
#     response = requests.get(base_url, params=params, timeout=10)

#     # Raise an exception if the status code is not 200 (OK)
#     response.raise_for_status()

#     # Parse the JSON response and get the abstract
#     data = response.json()
#     if 'abstract' in data['message']['items'][0]:
#         abstract = data['message']['items'][0]['abstract']
#         return abstract
#     else:
#         return None

# # Loop through the first 10 rows in the DataFrame
# for i in range(10):
#     # Get the title of the current row
#     title = df.at[i, 'Title']

#     # Call the get_abstract function with the title and retry if it fails
#     try:
#         abstract = get_abstract(title)
#     except:
#         abstract = None

#     df.at[i, 'Abstract'] = abstract

# # Save the updated DataFrame to an Excel file
# df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/output_with_abstracts_part1.xlsx')

# # Loop through the rest of the rows in the DataFrame
# for i in range(10, len(df)):
#     # Get the title of the current row
#     title = df.at[i, 'Title']

#     # Call the get_abstract function with the title and retry if it fails
#     try:
#         abstract = get_abstract(title)
#     except:
#         abstract = None

#     df.at[i, 'Abstract'] = abstract

# # Save the updated DataFrame to an Excel file
# df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/output_with_abstracts_part2.xlsx')


# import pandas as pd
# from Bio import Entrez

# # Enter your email address below
# Entrez.email = "sadaf.asfa@gmail.com"

# # Read in the titles from the DataFrame
# df = pd.read_excel("/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/Title.xlsx")
# titles = df["Title"].tolist()

# # Search for the PubMed IDs corresponding to the titles
# id_list = []
# for title in titles:
#     handle = Entrez.esearch(db="pubmed", term=title)
#     record = Entrez.read(handle)
#     id_list.append(record["IdList"])

# # Flatten the list of PubMed IDs
# id_list = [item for sublist in id_list for item in sublist]

# # Fetch the abstracts of the articles
# articles = []
# for article_id in id_list:
#     handle = Entrez.efetch(db="pubmed", id=article_id, rettype="abstract", retmode="text")
#     abstract = handle.read()
#     articles.append(abstract)

# # Print the abstracts
# for article in articles:
#     print(article)

# #save the abstracts in a excel file
# df = pd.DataFrame(articles)
# df.to_excel("/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/abs.xlsx")

import pandas as pd
from Bio import Entrez

# Enter your email address below
Entrez.email = "sadaf.asfa@gmail.com"

# Read in the titles from the DataFrame
df = pd.read_excel("/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/Title.xlsx")


title_chunks = [df['Title'][i:i+100].tolist() for i in range(0, len(df), 100)]

# Initialize an empty list to store the pmids
pmid_list = []

# Loop over the title chunks and query them one by one
for titles in title_chunks:
    # Join the titles into a single string separated by OR
    title_query = " OR ".join(titles)
    
    # Search for the titles in PubMed
    handle = Entrez.esearch(db="pubmed", term=title_query, retmax=100, usehistory='y')
    record = Entrez.read(handle)
    handle.close()
    
    # Append the list of pmids to the pmid_list
    pmid_list.extend(record['IdList'])

# Convert the pmid_list to a dataframe
pmid_df = pd.DataFrame(pmid_list, columns=['PubMed ID'])

# Save the pmid_df to an Excel file
pmid_df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/pmid_df.xlsx')  