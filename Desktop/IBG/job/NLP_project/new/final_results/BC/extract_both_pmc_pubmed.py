# # import requests
# # import xml.etree.ElementTree as ET
# # import pandas as pd

# # base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


# # params = {
# #    "db": "pmc",
# #    "term": '("DNA damage response" OR "DDR" OR "response to DNA damage") AND ("Pulmonary Cancer" OR "Lung Neoplasms" OR "Pulmonary Neoplasms" OR "Cancer of the Lung") AND ("tissue" OR "tissues" OR "tissue sample") AND ("lesions" OR "lesions" OR "damage" OR "injury" OR "injuries") NOT ("Chemotherapy" OR "Drug therapy" OR "Drug treatment" OR "Radiation therapy" OR "Radiotherapy" OR "Surgery")',
# #    "retmode": "xml",
# #    "retmax": 10000
# # }

# # # Send the search request to the NCBI E-Utils API
# # response = requests.get(base_url + "esearch.fcgi", params=params)

# # # Parse the XML response to extract the PubMed IDs of the articles
# # root = ET.fromstring(response.text)
# # pubmed_ids = [elem.text for elem in root.iter("Id")]

# # # Print the extracted PubMed IDs
# # print("PubMed IDs:", pubmed_ids)

# # # Save the PubMed IDs to an Excel file
# # pubmed_ids_df = pd.DataFrame(pubmed_ids, columns=["pm_ids"])
# # pubmed_ids_df.to_excel("/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/pubmed_ids.xlsx", index=False)


# import requests
# import xml.etree.ElementTree as ET
# import pandas as pd

# base_url_pubmed = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
# base_url_pmc = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# # Search parameters for both PubMed and PMC
# params = {
#    "term": '("DNA damage response" OR "DDR" OR "response to DNA damage") AND ("Pulmonary Cancer" OR "Lung Neoplasms" OR "Pulmonary Neoplasms" OR "Cancer of the Lung") AND ("tissue" OR "tissues" OR "tissue sample") AND ("lesions" OR "lesions" OR "damage" OR "injury" OR "injuries") NOT ("Chemotherapy" OR "Drug therapy" OR "Drug treatment" OR "Radiation therapy" OR "Radiotherapy" OR "Surgery")',
#    "retmode": "xml",
#    "retmax": 10000
# }

# # Send the search request to the PubMed API
# params_pubmed = params.copy()
# params_pubmed["db"] = "pubmed"
# response_pubmed = requests.get(base_url_pubmed, params=params_pubmed)

# # Parse the XML response to extract the PubMed IDs of the articles
# root_pubmed = ET.fromstring(response_pubmed.text)
# pubmed_ids = [elem.text for elem in root_pubmed.iter("Id")]

# # Send the search request to the PMC API
# params_pmc = params.copy()
# params_pmc["db"] = "pmc"
# response_pmc = requests.get(base_url_pmc, params=params_pmc)

# # Parse the XML response to extract the PMC IDs of the articles
# root_pmc = ET.fromstring(response_pmc.text)
# pmc_ids = [elem.text for elem in root_pmc.iter("Id")]

# # Merge the PubMed and PMC IDs
# all_ids = pubmed_ids + pmc_ids

# # Print the extracted IDs
# print("PubMed IDs:", pubmed_ids)
# print("PMC IDs:", pmc_ids)
# print("All IDs:", all_ids)

# # Save the IDs to an Excel file
# ids_df = pd.DataFrame(all_ids, columns=["ids"])
# ids_df.to_excel("/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/pubmed_pmc_ids.xlsx", index=False)

##############################paper from pmid##################

import requests
# import pandas as pd
# from bs4 import BeautifulSoup


# # Define the base URL for the NCBI E-Utils API
# base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


# # Import the excel file
# df = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/pubmed_ids100000.xlsx')


# # Define the list of PubMed IDs
# pubmed_ids = df['pm_ids'].tolist()
# pubmed_ids = [str(i) for i in pubmed_ids]


# # Define the parameters for the fetch request
# params = {
#   "db": "pubmed",
#   "retmode": "xml"
# }


# # Break the list of PubMed IDs into smaller chunks
# chunk_size = 100
# num_chunks = len(pubmed_ids) // chunk_size + (len(pubmed_ids) % chunk_size != 0)


# records = []
# for i in range(num_chunks):
#   chunk = pubmed_ids[i*chunk_size:(i+1)*chunk_size]
#   params["id"] = ",".join(chunk)


#   # Send the fetch request to the NCBI E-Utils API
#   response = requests.get(base_url + "efetch.fcgi", params=params)


#   # Load the raw XML text into a BeautifulSoup object
#   soup = BeautifulSoup(response.text, "xml")


#   # Extract the relevant data from the BeautifulSoup object
#   for pubmed_article in soup.find_all("PubmedArticle"):
#       record = {}
#       pmid = pubmed_article.find("PMID").text
#       article_title = pubmed_article.find("ArticleTitle").text
#       years = pubmed_article.find("Year")
#       if years is not None:
#           years = years.text
#       abstract_texts = pubmed_article.find_all("AbstractText")
#       abstract = " ".join([abstract_text.text for abstract_text in abstract_texts]) if abstract_texts else None


#       record["PMID"] = pmid
#       record["ArticleTitle"] = article_title
#       record["Abstract"] = abstract
#       record["Year"] = years
#       records.append(record)


# # Convert the list of dictionaries to a Pandas DataFrame
# df = pd.DataFrame(records)


# # Preview the resulting DataFrame
# print(df.head())


# df.to_excel("/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/pubmed_lung_allINFO.xlsx", index=False)


