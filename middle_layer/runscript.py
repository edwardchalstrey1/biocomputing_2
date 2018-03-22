#############################################
### THIS SCRIPT USED FOR TESTING PURPOSES ###
#############################################

import business_rules as b

genes = b.get_gene_list()
	
html = "<html>\n"

html += "<head>\n"
html += "<title> List of genes in the database </title>\n"
html += "</head>\n"

html += "<body>\n"

html += "<ul>\n"

for gene in genes:

	html += "<li>" + gene + "</li>"

html += "</ul>\n"

html += "</body>\n"

html += "</html>\n"

print(html)