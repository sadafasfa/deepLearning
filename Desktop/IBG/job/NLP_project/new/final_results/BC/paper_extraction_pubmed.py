# import requests
# import pandas as pd
# import xml.etree.ElementTree as ET

# # Define the base URL for the NCBI E-Utils API
# base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# # Define the parameters for the search query
# # params = {
# #    "db": "pubmed",
# #    "term": '("DNA damage response" OR "DDR" OR "response to DNA damage") AND ("brain cancer" OR "brain neoplasms" OR "brain tumors" OR "intracranial neoplasms")',
# #    "retmode": "xml",
# #    "retmax": 4000
# # }

# # Define the parameters for the search query
# # params = {
# #    "db": "pubmed",
# #    "term": '("DNA damage response" OR "DDR" OR "response to DNA damage") AND ("breast cancer" OR "breast neoplasm" OR "breast tumors" OR "mammary cancer" OR "breast carcinoma" OR "mammary carcinoma" OR "malignant neoplasm of breast") AND ("tissue" OR "tissues" OR "tissue sample") AND ("lesions" OR "lesions" OR "damage" OR "injury" OR "injuries") NOT ("therapy" OR "treatment")',
# #    "retmode": "xml",
# #    "retmax":6000
# # }

# # Define the parameters for the search query for breast cancer
# # params = {
# #    "db": "pubmed",
# #    "term": '("DNA damage response" OR "DDR" OR "response to DNA damage") AND ("breast cancer" OR "breast neoplasm" OR "breast tumors" OR "mammary cancer" OR "breast carcinoma" OR "mammary carcinoma" OR "malignant neoplasm of breast") AND ("tissue" OR "tissues" OR "tissue sample") AND ("lesions" OR "lesions" OR "damage" OR "injury" OR "injuries") NOT ("therapy" OR "treatment")',
# #    "retmode": "xml",
# #    "retmax": 10000
# # }
# ####for lung cancer
# params = {
#    "db": "pubmed",
#    "term": '("DNA damage response" OR "DDR" OR "response to DNA damage") AND ("Pulmonary Cancer" OR "Lung Neoplasms" OR "Pulmonary Neoplasms" OR "Cancer of the Lung") AND ("tissue" OR "tissues" OR "tissue sample") AND ("lesions" OR "lesions" OR "damage" OR "injury" OR "injuries") NOT ("Chemotherapy" OR "Drug therapy" OR "Drug treatment" OR "Radiation therapy" OR "Radiotherapy" OR "Surgery")',
#    "retmode": "xml",
#    "retmax": 10000
# }

# # Send the search request to the NCBI E-Utils API
# response = requests.get(base_url + "esearch.fcgi", params=params)

# # Parse the XML response to extract the PubMed IDs of the articles
# root = ET.fromstring(response.text)
# pubmed_ids = [elem.text for elem in root.iter("Id")]

# # Print the extracted PubMed IDs
# print("PubMed IDs:", pubmed_ids)

# #save pubmed ids to excel
# pubmed_ids = pd.DataFrame(pubmed_ids)

# #save pubmed ids to excel
# pubmed_ids.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/pubmed_ids100000.xlsx',index=False, header=["pm_ids"])


# ####################From Pubmed IDs get abstracts, author, years##############
# #pip install lxml

# import requests
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



####################################search for seperate terms (DDR seperate, lung seperate) and get pubmed ids#################### NOT USED and not IMPORTANT
# import requests
# from lxml import etree

# # Define the base URL for the NCBI E-Utils API
# base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# # Define the parameters for the search query for lung cancer
# params_lung_cancer = {
#    "db": "pubmed",
#    "term": '("lung cancer" OR "pulmonary cancer" OR "lung neoplasms" OR "pulmonary neoplasms" OR "cancer of the lung")',
#    "retmode": "xml",
#    "retmax": 4000
# }

# # Define the parameters for the search query for DDR
# params_ddr = {
#    "db": "pubmed",
#    "term": '("DNA damage response" OR "DDR" OR "response to DNA damage")',
#    "retmode": "xml",
#    "retmax": 4000
# }

# # Send the search request to the NCBI E-Utils API for lung cancer
# response_lung_cancer = requests.get(base_url + "esearch.fcgi", params=params_lung_cancer)

# # Parse the XML response to extract the PubMed IDs of the lung cancer articles
# root_lung_cancer = etree.fromstring(response_lung_cancer.content)
# pubmed_ids_lung_cancer = set([elem.text for elem in root_lung_cancer.xpath("//Id")])

# # Send the search request to the NCBI E-Utils API for DDR
# response_ddr = requests.get(base_url + "esearch.fcgi", params=params_ddr)

# # Parse the XML response to extract the PubMed IDs of the DDR articles
# root_ddr = etree.fromstring(response_ddr.content)
# pubmed_ids_ddr = set([elem.text for elem in root_ddr.xpath("//Id")])

# # Find the intersection of the two sets of PubMed IDs
# pubmed_ids_intersection = pubmed_ids_lung_cancer.intersection(pubmed_ids_ddr)

# # Print the number of papers in the intersection
# print("Number of papers in the intersection:", len(pubmed_ids_intersection))

# # Print the PubMed IDs of the papers in the intersection
# print("PubMed IDs in the intersection:", pubmed_ids_intersection)


#  #save pubmed ids to excel
# pubmed_ids = pd.DataFrame(pubmed_ids_intersection)

# # #save pubmed ids to excel
# pubmed_ids.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/pubmed_ids_intersection.xlsx')


