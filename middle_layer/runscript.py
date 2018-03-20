#############################################
### THIS SCRIPT USED FOR TESTING PURPOSES ###
#############################################

import business_rules as b

gene_list_XML = b.get_gene_list()

from xml.dom import minidom

doc = minidom.parseString(gene_list_XML)
	
html = "<html>\n"

html += "<head>\n"
html += "<title> List of genes in the database </title>\n"
html += "</head>\n"

html += "<body>\n"

html += "<ul>\n"

for gene in doc.getElementsByTagName('gene'):

	html += "<li>" + gene.firstChild.data + "</li>"

html += "</ul>\n"

html += "</body>\n"

html += "</html>\n"

print(html)