#!/usr/bin/env python
""" 
Programme:  Query
File:       query.cgi

Version:    V7...
            
Date:       12/04/18
Function:   Get Gene information for Chromosome 18 from index.cgi, process and display

Copyright:  (c) Trupti Gore, Birkbeck College, 2018
Author:     Trupti Gore
Address:    Msc Bioinformatics with Systems Biology (First Year)
            Department of Biological sciences
            Birkbeck,University of London
            London WC1E 7HX

----------------------------------------------------------------------------------------------------------

This programme is released under the GNU Public Licence (GPL V3)

----------------------------------------------------------------------------------------------------------

Description:
------------

This programme accepts a Gene id or Location or Accession Number or Protein name for the genes
on Chromosome 18 from index.cgi. After accepting the values it accesses the middle layer functions which inturn 
queries the database and passes the information back to this programme to display on the webpage.

-----------------------------------------------------------------------------------------------------------
Revision History:
-----------------
V7      12/04/18        Original    By: TG  Previous versions are not tracked.
V8      13/04/18        Added Codon Table
V8.1    16/04/18        Codon list from function

"""


print("Content-Type: text/html\n")	

#**************************************
#******Import python modules***********
#**************************************

import cgi;
import cgitb
cgitb.enable()
import xml.etree.ElementTree as ET
import re
import operator
from operator import itemgetter
import business_rules as br
import functions as f
import dummy_data as dd

#**************************************
#***Get form values from index.cgi*****
#**************************************


form=cgi.FieldStorage()
gid=form.getvalue("Gene")
acc=form.getvalue("Accession")
prot=form.getvalue("Protein")
loc=form.getvalue("Location")
res_enzyme=form.getvalue("Enzyme")

#*******************************************
#***** Access Gene information dictionary***
#*******************************************
gene_dict=br.get_entries(gid,prot,acc,loc)  # Detailed information of the gene in a dictionary format
        
for gene in gene_dict:
    for gene_info in gene:
    	
    	if gene[gene_info]==gid or gene[gene_info]==acc or gene[gene_info]==prot or gene[gene_info]==loc:
    		
            protein=gene['prot']
            dna=gene['dna'].upper()
            gene_name=gene['gene']
            amino_acid=gene['aa']
            cds=gene['cds']
            res_site=gene['restriction_sites']
            #cseq=d['cds_seq']
            break;
        else:
            protein='The infomation about the protein is not available for this gene'
            dna='The infomation about the dna is not available for this gene'
            amino_acid='The infomation about the amino acid is not available for this gene'


#codon_freq=br.count_codons(dna)  
#******************************************************************
#*** Codon frequency table for the gene and entire chromosome******
#******************************************************************

codon_list= br.dna_codon_to_amino_acid_dict.keys() 
codon_dict=dd.get_codon_usage_frequencies(codon_list)
gene_codon_dict=br.get_table_data(codon_dict)
chrom_codon_dict=dd.get_table_data_entire_chromosome()


#for key in d.values():
 #   print(key)
  #  print('aa is :',key['aa'])
   # print('ratio is :',key['ratio'])
    #print('freq is :',key['freq'])
#for k,v in d.items():
 #   #print(v)
  #  for key in v:
   #     print(key)
    #    print('v is ',v[key])
      
    
  
     
#******* Get Coding Sequence*********


coding_sequence=br.get_coding_seq(dna,cds)

#***********Get Amino Acid  - Aligned**********
aligned_amino_acid=''
for a in amino_acid:
    aligned_amino_acid += a + "  "

#***************Highlight coding parts of the dna**************
original_dna=dna
dna=f.highlight_coding_seq(dna,cds)    
coding_highlighted_dna=f.hilite(dna)
    
#********** Restriction enzyme site. Highlight only******* 
#*****if these sites are not found in between the start********
#*********and End of coding region.**********

enzdict={} # Dictionary is pre populated to display the highlighted restriction enzymes according to the selection
for enzyme,coordinates in res_site.items():
    
    resflag=f.check_res_enzyme(enzyme,cds,res_site) # resflag checks if the restriction cut sites are outside the coding region.
    
    if resflag!='True':
        coordinates=sorted(coordinates, key=itemgetter(1))
        restricted_dna=f.highlight_coding_seq(original_dna,coordinates)
        restricted_dna=f.hilite_res(restricted_dna)
            
    else:
        
        restricted_dna=' The selected restriction enzyme {} cuts within the coding region and hence not a useful enzyme to use for the genetic manipulation of this gene.'.format(enzyme)     
    enzdict[enzyme]=restricted_dna     
    

i=0 # variable for indicator scale

#***********************************************
#************Main CGI Script********************
#***********************************************
	
html="<html>\n"
html+="<head>\n"
html+="<title> Detailed information about the Gene </title>\n"
html+="<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"


html+="<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>\n"
html+="<script src='http://localhost/BioCW/WWW/JS/bootstrap.min.js'></script>\n"
html+="<link rel='stylesheet' href='http://localhost/BioCW/WWW/CSS/bootstrap.min.css'></script>\n"
html+="<script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js'></script>"

html+="<link rel='stylesheet'  type='text/css'  href='http://localhost/BioCW/WWW/CSS/style.css'/>\n"
html+="</head>\n"
html+="<body ng-app=''>\n"  # Angular JS functionality to display restriction enzyme cut sites as per the user input
html+="<table name='GeneIntro'>"
html+="<tr>"
html+="<th class='firstcol'>"
html+="<p> Name  </p>"
html+="</th>"
html+="<td>"
html+="<pre>"
html+=gene_name
html+="</pre>"
html+="</td>"
html+="</tr>"
html+="</tr>"
html+="<tr>"
html+="<th>"
html+="<p> The protein </p>"
html+="</th>"
html+="<td>"
html+="<pre>"
html+=protein
html+="</pre>"
html+="</td>"
html+="</tr>"
html+="<tr>"
html+="<th>"
html+="<p> CDS : </p>"
html+="</th>"
html+="<td>"

coding_coordinates=''
for c in cds:
   coding_coordinates+=''.join('%s'%c)# for x in l)
html+="<div class='scroll'>"
html+="<pre>"
html+=coding_coordinates
html+="</pre>"
html+="</div>"
html+="</td>"
html+="</tr>"
html+="</table>"

html+="<table name='GeneDetailInfo'>" # Table to display dna sequences
html+="<tr>"
html+="<td class='firstcol'>"

#html+="<p>Indicator Scale</p>\n"

html+="<p> Original Sequence </p>\n"
html+="<br>"
html+="<br>"
html+="<p> Highlighted coding region: </p>\n"
html+="<br>"
html+="<p> " 'Select Restriction Enzyme to check' "</p>\n"

html+="<form>"
html+="<input type='radio' ng-model='myVar' value='bm'>BamHI"
html+="<input type='radio' ng-model='myVar' value='bs'>BsuMI"
html+="<input type='radio' ng-model='myVar' value='ec'>EcoRI"  
html+="</form>"


html+="</td>"
html+="<td> " # second column
html+="<div class='scroll'>" # div to scroll
#html+="<div class='child'>" # child for label
#html+="<pre>"
#while i<len(dna):
#    html+="<label>" +str(i)+"</label>"
#    i+=1000

#html+="</div>"  # end label child
html+="<div class='child'>" # first child
html+="<pre>\n"

html+=original_dna
html+="</pre>"
html+="</div>"               # end first child 

html+="<div class='child'>\n"  #second child
html+="<pre>\n"
html+=coding_highlighted_dna 
#html+="<br>"
#html+="<br>"
#html+="<br>"
html+="</pre>\n"
html+="</div>\n"            # end second child


html+="<div id= 'res_dna' class='child'>\n" # thild child
#html+="<div id='showHide' display = none'>\n"
html+="<div ng-switch='myVar'>"  # parent div of angular.    AngularJS code taken from https://www.w3schools.com/angular/tryit.asp?filename=try_ng_form_radio
html+="<div ng-switch-when='bm'>" # first child div of angular
html+="<p>" + enzdict['BamHI'] +"</p>" 

html+=str(res_site['BamHI']) 
html+="</div>"                  # first child div of angular ends
html+="<div ng-switch-when='bs'>" # second child div of angular
html+="<p>" + enzdict['BsuMI'] +"</p>" 
html+=str(res_site['BsuMI'])     
html+="</div>"                      # second child div of angular ends
html+="<div ng-switch-when='ec'>"   # third child div of angular
html+="<p>" + enzdict['EcoRI'] +"</p>" 
html+=str(res_site['EcoRI'])    
html+="</div>"                      # third child div of angular ends

html+="</div>"   

                   # parent div of angular ends
html+="</div>\n"                    # scroll div ends



html+="</td>"
html+="</tr>"
html+="</table>"
html+="<table>"
html+="<tr>"
html+="<td class='firstcol'>"
html+="<p> The coding sequence:</p>\n"
html+="<br>"

html+="<p> The Amino Acid: </p>\n"
html+="<br>"
html+="<br>"

html+="</td>"
html+="<td>"
html+="<div class='scroll'>"    # div to scroll

html+="<div id=class='child'>\n" # first child
#html+="<br>"
html+="<pre class='display'>\n"
html+=  coding_sequence 
html+="</pre>\n"                    # first child ends
html+="</div>"
html+="<br>"

html+="<div class='child'>\n" # second child
html+="<pre class='display'>\n"
html+=aligned_amino_acid

html+="</pre>\n"

html+="</div>"              # second child ends

html+="</div>"              # scroll div ends
html+="</td>"
html+="</tr>"
html+="</table>"
html+="<p> The codon usage frequency is:</p>\n"

#******* Create accordian to display codon table ***********. https://www.w3schools.com/howto/howto_js_accordion.asp

html+="<button class='accordion'>Codon Frequency Table</button>"
html+="<div class='panel'>"
clist=['A','C','G','T']
html+="<div class='container-fluid'>"
html+="<div class='row'>"
html+="<div class='col-sm-6'>"
#html+="<div class='wrapper'>"
#html+="<div class='left'>"
#html+="<md-grid-list md-cols-lg='12' md-cols-gt-lg='15' md-cols-xs='3' md-cols-sm='6' md-cols-md='9' md-row-height-gt-md='1:1' md-row-height-md='1:1' md-row-height='1:2' md-gutter-gt-md='16px' md-gutter-md='8px' md-gutter='4px'>"
#html+="<md-grid-tile ng-repeat='contact in contacts' md-colspan='3' md-rowspan-gt-sm='4' style='background:red;'>"
           
html+="<table border='1', style='border-collapse: collapse' >"
html+="<tr>"
    
html+="<td></td>"
html+="<th> Codon </th>"
html+="<th> Amino</th>"
html+="<th> Frequency </th>"
html+="<th> Ratio </th>"
html+="</tr>"

for c in clist:
    html+="<tr>"
    html+="<td rowspan='65'>" +c+ "</td>"
    #html+="</tr>"
    for key,value in sorted(gene_codon_dict.items()):
        html+="<tr>"
        if key[0]==c:
           
            html+="<td>"+key+"</td>"
           
            for v in value:
                
                html+="<td>"+str(value[v])+"</td>"
        html+="</tr>"     
                
    html+="</tr>"

html+="</table>"  
#html+="</div>" # left
html+="</div>"  # columnn
#html+="<div class='right'>"
html+="<div class='col-xs-6,col-sm-6'>"
html+="<table border='1', style='border-collapse: collapse' >"
html+="<tr>"
    
html+="<td></td>"
html+="<th> Codon </th>"
html+="<th> Amino</th>"
html+="<th> Frequency </th>"
html+="<th> Ratio </th>"
html+="</tr>"

for c in clist:
    html+="<tr>"
    html+="<td rowspan='65'>" +c+ "</td>"
    #html+="</tr>"
    for key,value in sorted(chrom_codon_dict.items()):
        html+="<tr>"
        if key[0]==c:
           
            html+="<td>"+key+"</td>"
           
            for v in value:
                
                html+="<td>"+str(value[v])+"</td>"
        html+="</tr>"     
                
    html+="</tr>"

html+="</table>"
#html+="</div>" # right
html+="</div>" # column2
#html+="</md-grid-tile>"
#html+="</md-grid-list>" 
html+="</div>" # row
html+="</div>" # conainer
#html+="<table>"
#html+="<tr>" "<th>" 'Codon' "</th> " "<th>" 'Frequency' "</th>" "</tr>"
#for k,v in codon_freq.items():
    #html+="<tr>" "<td>" + k + "</td>"
    #html+="<td>" + str(v) + "</td>" "</tr>"
#html+="</table>"

html+="</div>" # panel
html+="</div>" # wrapper

#html+="<div style='overflow-x:auto;'>"
#html+="<table>"
#html+="<tr>" "<th>" 'Codon' "</th> " "<th>" 'Frequency' "</th>" "</tr>"
#for k,v in codon_freq.items():
 #   html+="<tr>" "<td>" + k + "</td>"
  #  html+="<td>" + str(v) + "</td>" "</tr>"
#html+="</table>"


#html+="</div>"

html+="<div class='footer'> Trupti Gore</div>"
html+="<script type='text/javascript' src='http://localhost/BioCW/WWW/JS/biocw.js'></script>\n"
html+="<script type='text/javascript' src='http://localhost/BioCW/WWW/JS/lastmodified.js'></script>\n"
html+="</body>\n"

html+="</html>\n"

print(html)
		
