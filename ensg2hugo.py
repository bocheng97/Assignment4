#!/usr/bin/python
import argparse
import sys
import re
import csv
parser = argparse.ArgumentParser()
#parser.add_argument('-i', metavar='in-file', type=argparse.FileType('rt'))

parser.add_argument("input", nargs='?',type=argparse.FileType('r'), default=sys.stdin, help= 'your csv file with 9 columns')
#parser.add_argument("output", nargs='?',type=argparse.FileType('w'),default=sys.stdout, help='your output file name')
parser.add_argument("-f","--columns",nargs='?', type=int, default=1,help='the column which will be gene_name')
args = parser.parse_args()

file = open('/Users/bocheng/PycharmProjects/pythonProject1/Homo_sapiens.GRCh37.75.gtf', "r")
GRCh3775_dic = {}
for line in file:
    match_obj = re.search(r'(.*)\t(.*)\t(.*)\t(\d+)\t(\d+)\t(.*)\tgene_id\s\"(.*?)\"(.*)gene_name\s"(.*?)"\;', line)
    #if match_obj.group(3) == 'gene':
    gene_name = match_obj.group(9)
    gene_id = match_obj.group(7)
    GRCh3775_dic[gene_id] = gene_name
    #else:
    #    continue
#print(GRCh3775_dic)
dic_list = []
#file1 = open('/Users/bocheng/PycharmProjects/pythonProject1/qqq.csv', 'r')
file1 = args.input
for line in file1:
    match_obj = re.search(r'"(.*?)","(.*?)","(.*?)",(.*?)\,(.*)', line)
    if match_obj.group(2) != 'gene_id': #skip headline of csv files
        match_obj_geneid = re.search(r'(.*)\.(\d+)', match_obj.group(2))
        if match_obj_geneid.group(1) in GRCh3775_dic:
            dic={}
            if args.columns == 1:
                dic = {'':GRCh3775_dic[match_obj_geneid.group(1)] , 'gene_id': match_obj.group(2),
                   'gene_type': match_obj.group(3),
                   'logFC': match_obj.group(4), 'AveExpr': match_obj.group(5),'t':'','P.Value':'','adj.P.Val':''}
            elif args.columns ==2:
                dic = {'': match_obj.group(1), 'gene_id': GRCh3775_dic[match_obj_geneid.group(1)],'gene_type': match_obj.group(3),
                    'logFC': match_obj.group(4), 'AveExpr': match_obj.group(5),'t':'','P.Value':'','adj.P.Val':''}
            elif args.columns ==3:
                dic = {'': match_obj.group(1), 'gene_id': match_obj.group(2),
                       'gene_type': GRCh3775_dic[match_obj_geneid.group(1)],
                       'logFC': match_obj.group(4), 'AveExpr': match_obj.group(5),'t':'','P.Value':'','adj.P.Val':''}
            elif args.columns ==4:
                dic = {'': match_obj.group(1), 'gene_id': match_obj.group(2),
                       'gene_type': match_obj.group(3),
                       'logFC': GRCh3775_dic[match_obj_geneid.group(1)], 'AveExpr': match_obj.group(5),'t':'','P.Value':'','adj.P.Val':''}
            elif args.columns == 5:
                dic = {'': match_obj.group(1), 'gene_id': match_obj.group(2),
                       'gene_type': match_obj.group(3),
                       'logFC': match_obj.group(4), 'AveExpr': GRCh3775_dic[match_obj_geneid.group(1)],'t':'','P.Value':'','adj.P.Val':''}
            elif args.columns == 6:
                dic = {'': match_obj.group(1), 'gene_id': match_obj.group(2),
                       'gene_type': match_obj.group(3),
                       'logFC': match_obj.group(4), 'AveExpr': match_obj.group(5), 't': GRCh3775_dic[match_obj_geneid.group(1)],
                       'P.Value': '', 'adj.P.Val': ''}
            elif args.columns ==7:
                dic = {'': match_obj.group(1), 'gene_id': match_obj.group(1),
                       'gene_type': match_obj.group(3),
                       'logFC': match_obj.group(4), 'AveExpr':match_obj.group(5), 't': '',
                       'P.Value': GRCh3775_dic[match_obj_geneid.group(1)], 'adj.P.Val': ''}
            elif args.columns ==8:
                dic = {'': match_obj.group(1), 'gene_id': match_obj.group(1),
                       'gene_type': match_obj.group(3),
                       'logFC': match_obj.group(4), 'AveExpr':match_obj.group(5), 't': '',
                       'P.Value': '', 'adj.P.Val': GRCh3775_dic[match_obj_geneid.group(1)]}
        else:
            dic = {'': match_obj.group(1), 'gene_id': match_obj.group(2)+ 'NA', 'gene_type': match_obj.group(3),
                   'logFC': match_obj.group(4), 'AveExpr': match_obj.group(5),'t':'','P.Value':'','adj.P.Val':''}
        dic_list.append(dic)
    else:
        continue
#print(dic_list)
#import csv

with open('output.hugo.csv', mode='w') as csv_file:
    fieldnames = ['', 'gene_id', 'gene_type','logFC','AveExpr','t','P.Value','adj.P.Val']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n = 0
    writer.writeheader()
    for n in range(0,len(dic_list)):
        writer.writerow(dic_list[n])
        n +=1







