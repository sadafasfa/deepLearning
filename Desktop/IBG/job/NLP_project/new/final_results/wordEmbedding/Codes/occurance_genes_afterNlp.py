##################after word2vec with both comparing with pubmed downloaded genes and return occurance of genes on ABS ###############
# 
import pandas as pd
import re

# df_publications=pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/justAbstract.xlsx')

# #df_genes = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/common_genes_Lung_rgx.xlsx')
# #df_genes = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/genes_lung_pubmed_DL.xlsx')
# df_genes = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/common_genes_Lung_rgx.xlsx')
# df_publications.dropna(subset=['Abstract'], inplace=True)


# def extract_genes_from_text(text, gene_list):
#     matches = []
#     for gene in gene_list:
#         regex = r'\b{}\b'.format(gene)
#         if re.search(regex, text, re.IGNORECASE):
#             matches.append(gene)
#     return matches



# df_publications['matched_genes'] = df_publications['Abstract'].apply(lambda x: extract_genes_from_text(x, list(df_genes['genes'])))


# gene_counts = pd.Series(df_publications['matched_genes'].sum()).value_counts()

# #print(gene_counts)

# df_gene_counts = pd.DataFrame({'gene': gene_counts.index, 'count': gene_counts.values})
# df_gene_counts = df_gene_counts.sort_values(by='count', ascending=False)

# df_gene_counts.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/Count_genes_lung_rgx.xlsx',index=False)



#########################################Find occurance of genes with tehir like Tp53, p53 synonyms in abstracts ##############################
######################################

import pandas as pd
import re

df_publications = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/justAbstract.xlsx')

# df_genes = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/common_genes_Lung_rgx.xlsx')
df_genes = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/common_genes_Lung_rgx_alias.xlsx')

#remove nan from synonyms prevent error AttributeError: 'float' object has no attribute 'split'
df_genes['synonyms'] = df_genes['synonyms'].fillna('')

df_genes.set_index('genes', inplace=True)

df_publications.dropna(subset=['Abstract'], inplace=True)

df_genes = df_genes.reset_index()

def extract_genes_from_text(text, gene_list):
    matches = []
    for index, row in gene_list.iterrows():
        gene = row['genes']
        synonyms = row['synonyms']
        # Combine the gene and its synonyms into a single list
        aliases = synonyms.split(', ') + [gene]
        for alias in aliases:
            regex = r'\b{}\b'.format(alias)
            if re.search(regex, text, re.IGNORECASE):
                matches.append(gene)
                break
    return matches

df_publications['matched_genes'] = df_publications['Abstract'].apply(lambda x: extract_genes_from_text(x, df_genes))

gene_counts = pd.Series(df_publications['matched_genes'].sum()).value_counts()

df_gene_counts = pd.DataFrame({'gene': gene_counts.index, 'count': gene_counts.values})

df_gene_counts.set_index('gene', inplace=True)

df_gene_counts = df_gene_counts.sort_values(by='count', ascending=False)

df_gene_counts.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Lung/Count_genes_lung_rgx_alias.xlsx')

######################NO nlp just occurance uisng regex#####################

# import pandas as pd
# import re
# from collections import defaultdict

# df_publications = pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Breast/justAbstract.xlsx')

# def extract_genes_from_text(text):
#     regex = r'\b([A-Z0-9]+(?:\d+)?(?:/[A-Z0-9]+(?:\d+)?)*)\b'  # pattern to match any uppercase letters or numbers
#     matches = re.findall(regex, text, re.IGNORECASE)
#     return matches

# paper_gene_counts = defaultdict(set)

# for abstract in df_publications['Abstract']:
#     genes = extract_genes_from_text(abstract)
#     for gene in genes:
#         paper_gene_counts[gene].add(abstract)

# gene_counts = {gene: len(paper_set) for gene, paper_set in paper_gene_counts.items()}

# df_gene_counts = pd.DataFrame({'gene': list(gene_counts.keys()), 'occurance': list(gene_counts.values())})
# df_gene_counts = df_gene_counts.sort_values(by='occurance', ascending=False)

# df_gene_counts.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Breast/genes_occure_noNLP_rgx.xlsx', index=False)



################without NLP counting just not occurance#####################
# import pandas as pd
# import re

# # Load the dataframe with abstract column
# df=pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Breast/Breast_Abstract_100.xlsx')

# # Define a regular expression pattern to match gene symbols
# #gene_pattern = r'\b([A-Z0-9]+(?:\d+)?(?:/[A-Z0-9]+(?:\d+)?)*(?:c-Myc|mTORC1)?)\b'
# gene_pattern = r'\b([A-Z0-9]+(?:\d+)?(?:/[A-Z0-9]+(?:\d+)?)*)\b|c-Myc|mTORC1'


# # Extract gene symbols from abstracts
# genes = df['Abstract'].str.findall(gene_pattern)

# # Count gene occurrences
# gene_counts = {}
# for gene_list in genes:
#     for gene in gene_list:
#         if gene in gene_counts:
#             gene_counts[gene] += 1
#         else:
#             gene_counts[gene] = 1

# # Convert gene counts to a dataframe
# gene_df = pd.DataFrame({'Gene': list(gene_counts.keys()), 'Count': list(gene_counts.values())})

# # Sort by count in descending order
# gene_df = gene_df.sort_values('Count', ascending=False)

# # Save to Excel
# gene_df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Breast/genes_counts_NoNLP_myc.xlsx', index=False)

###############difultdict library count on Just Abstract because previous datafram had title and abs together#####################
# import re
# from collections import defaultdict
# import pandas as pd

# # Example dataframe with abstract column
# df= pd.read_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Breast/justAbstract.xlsx')

# # Regular expression to match gene names (here, we're using a simplified pattern for demonstration purposes)
# gene_pattern = r'\b([A-Z0-9]+(?:\d+)?(?:/[A-Z0-9]+(?:\d+)?)*)\b'

# # Create defaultdict to store gene counts
# gene_counts = defaultdict(int)

# # Loop through each abstract and extract gene names
# for abstract in df['Abstract']:
#     # Use regular expression to find all gene names in the abstract
#     matches = re.findall(gene_pattern, abstract)
#     # Add each match to the gene_counts dictionary
#     for match in matches:
#         gene_counts[match] += 1

# # Print gene counts
# for gene, count in gene_counts.items():
#     print(f'{gene}: {count}')

# #save to excel
# gene_df = pd.DataFrame({'Gene': list(gene_counts.keys()), 'Count': list(gene_counts.values())})

# # Sort by count in descending order
# gene_df = gene_df.sort_values('Count', ascending=False)

# # Save to Excel
# gene_df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Breast/Occure_NoNLP_defdict.xlsx', index=False)



#################withou NLP difultdict library occurance#####################

# from Bio import Entrez
# from Bio import Medline
# import pandas as pd
# import re
# from collections import defaultdict

# Entrez.email = 'sadaf.asfa@gmail.com'

# def extract_gene_names(text):
#     # Define a regular expression pattern to match gene names
#     gene_pattern = r'\b[A-Z]{1,2}[A-Z0-9]*\b'
#     # Use the regular expression to find all occurrences of gene names in the text
#     matches = re.findall(gene_pattern, text)
#     # Remove any matches that contain only uppercase letters (to exclude common words like "THE")
#     gene_names = [match for match in matches if match.isupper() and not match.isnumeric()]
#     return gene_names

# def count_gene_occurrences(df):
#     # Initialize a defaultdict to keep track of gene occurrences
#     gene_counts = defaultdict(int)
#     # Loop through each abstract in the dataframe
#     for abstract in df['Abstract']:
#         # Use BioPython to parse the abstract
#         records = Medline.parse(abstract)
#         for record in records:
#             # Extract the text of the abstract
#             text = record.get('AB', '')
#             # Extract gene names from the text
#             gene_names = extract_gene_names(text)
#             # Increment the count for each gene in the gene_counts dictionary
#             for gene in gene_names:
#                 gene_counts[gene] += 1
#     print (gene_counts)



# # #save the gene counts to a dataframe
# def save_gene_counts(gene_counts):
#     # Convert gene counts to a dataframe
#     gene_df = pd.DataFrame({'Gene': list(gene_counts.keys()), 'Count': list(gene_counts.values())})
#     # Sort by count in descending order
#     gene_df = gene_df.sort_values('Count', ascending=False)
#     # Save to Excel
#     gene_df.to_excel('/Users/sadaf/Desktop/IBG/job/NLP_project/new/final_results/wordEmbedding/Breast/Occur_NoNLP_biopython.xlsx', index=False)
