##################################
#### This is first basic draft####
##################################


""" Query CGI"""
import cgi;
import cgitb
import business_rules as br
import functions as f
cgitb.enable()

""" Get values from the form """

form=cgi.FieldStorage()
gid=form.getvalue("gene-id")
acc=form.getvalue("Accession")
prot=form.getvalue("Protein")
loc=form.getvalue("Location")

""" Call gene info function to get detailed information """        
protein,dna,aacid = f.get_gene_info()

""" Print in html format on the browser """
	
html="<html>\n"
html+="<head>\n"
html+="<title> Detailed information about the Gene </title>\n"

html+="</head>\n"
html+="<body>\n"
html+="<pre>\n"
html+=gid
html+="</pre>\n"
html+="<p> The protein corresponding to this gene is: </p>\n"
html+="<pre>\n"
html+=protein
html+="</pre>\n"
html+="<p> The dna corresponding to this gene is: </p>\n"
html+="<pre>\n"
html+=dna
html+="</pre>\n"
html+="<p> The Amino Acid corresponding to this gene is: </p>\n"
html+="<pre>\n"
html+=aacid
html+="</pre>\n"
html+="</body>\n"
html+="</html>\n"
