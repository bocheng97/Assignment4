# Hello, This is Bo Cheng, a begginer in python programmer. Thank you for visiting my github page.
## So, to begin with, this is a python3(compatible to python3) program to help you convert ensembl gene_id to hugo name. 
## Usage:ensg2hugo.py [-h] [-f [COLUMNS]] [input]
## The input file should have exact same structure with the example.csv file.So if you have a different structure csv file, just convert it to this structure, I think this will be easy. 
## "-f" will be limited to [1-8], the default f is 1.
## Because I am a begginer, to write this program is a little bit hard, so I do not set output option, the output file will be default by output.hugo.csv.
## And if the ensembl gene_id cannot match the gene_id we want to convert, "NA"will add on the gene_id, like the gene_id will be gene_id + "NA", so that you can find the un-matching easily. However, the un-matching will not change the column as the -f option change.
## The dictionary is generated from Homo_sapiens.GRCh37.75.gtf. So you can get the file by"curl -o Homo_sapiens.GRCh37.75.gtf http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf".
## ensg2hugo.py is deferent from ensg2hugo.1.py.
###ensg2hugo.py can process the file of unit test(https://github.com/davcraig75/unit), the data structure like example.csv.
### ensg2hugo.1.py can process data structure like example.1.csv 
## In the end, This program has been tested using example.csv, so I believe you can use it to help you! Thank you again for visiting my github page.

