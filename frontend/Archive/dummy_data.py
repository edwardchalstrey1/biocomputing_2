""" Added Dummy Data"""

def get_gene_list():

	genes = ['ABC', 'XYZ', 'ETC', 'VPS4B'] # dummy

	import xml.etree.ElementTree as ET

	genes_xml = ET.Element('genes')

	for gene in genes:

		gene_tag = ET.SubElement(genes_xml, 'gene')
		gene_tag.text = gene
	
	return(ET.tostring(genes_xml))
	
def get_accession_list():

	acc = ['AF282904', 'AF282903', 'AF282908', 'AF282906'] # dummy

	import xml.etree.ElementTree as ET

	acc_xml = ET.Element('acc')

	for ac in acc:

		acc_tag = ET.SubElement(acc_xml, 'accession')
		acc_tag.text = ac
	
	return(ET.tostring(acc_xml))
	
def get_protein_product_list():
	proteins = ['U58b small nucleolar RNA', 'U58a small nucleolar RNA', 'Putative U58 small nucleolar RNA'] # dummy

	import xml.etree.ElementTree as ET

	prot_xml = ET.Element('proteins')

	for  prot in proteins:

		prot_tag = ET.SubElement(prot_xml, 'protein')
		prot_tag.text = prot
	
	return(ET.tostring(prot_xml))

	



def get_chromosomal_location_list():
	locations = ['18p11.2', '18q21.1', '18q21-q22'] # dummy

	import xml.etree.ElementTree as ET

	loc_xml = ET.Element('locations')

	for  loc in locations:

		loc_tag = ET.SubElement(loc_xml, 'location')
		loc_tag.text = loc
	
	return(ET.tostring(loc_xml))