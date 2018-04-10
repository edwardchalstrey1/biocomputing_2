#!/usr/bin/env python3

""" Dummy data for use by middle layer whilst database layer unavailable - all code by Ed Chalstrey """

def get_entries(gene=None, prot=None, acc=None, loc=None, all=False):

	""" Should return a list of dictionaries. Each dict contains the gene, protein product, accession, location, CDS, DNA seq and AA seq """

	cds_coordinates_VPS4B = [[2676, 2702], [13357, 13468], [14489, 14645], [17436, 17503], [21109, 21228], [24232, 24388], [24739, 24887], [25612, 25693], [27682, 27901], [31386, 31526], [33859, 33960]]

	origin_seq_VPS4B = "ggatccaatccagaatcccatactgcatttagttgtcatcttcttagtctctacaatctgtgacagttcctcagtctttccttgtcttttatgatcttgacatttttgaggagcactggttattttgtagaagtagaaaaaccctccatatgaatttttctgatgttttctcatgattagattgaggttacaggtttgggaagcataccacagagctaatgtgcccttctccacatcaggggttccatcataacaacatggcttattactggtgataaaagaggggttttttgtttgtttgtttgtttttaccgattctcactctgttgcccaggctgaagtgcggtggtgtgatcttggctcactgcaatctctgcctcctgggttctagtgattctcctgcttcaccctcccaagtagctggagttacatgcaggcaccatcacgcctggctaatttttgtttgtttgttttgagacagagtttcgctctgtagcccaggctggagtgctgtggtgcgatctcagctcaccacaacctctgcctcctaggtcccggttcaagaaattctcctgcctcagcctcccgagtagctgggattacaggaacgcaccaccatgcccagctaatttttgtatttttagtagagacagggtttcaccatgttggccaggcgggtcttgaactgctgacctcaggtgatcgcccgccttggcctcccaaagtgctgggattacaggcgtgactcaccacacccggcctaatttttgtatttttagtagagatggagtttcaccatgttggccaggctggtctcgaactcctgacctcaagtgatccacccacctcggcctcccaaagtgctgggattacaggcgtgagtcaccacgcccggcccatctttgcttaaattataaactcagtttctcccacagttagttcagcctatgctcaggaatgtacaaggacagcttggaggttaaaagtaagatggagttggttaagttagatctctttcactgtctcagtcatcattttgcgaaggcaaattcacaagtgggaagaaaggacgggtagatgcagggcagagagagggctctgtgcttcgagcctggatgatacagatttggcaatactattctaaggagagaccagagaaagaagtttagggtagaaggtaattaattagagtatgttgaatttgtcttgcagaaaaaccctgtgaaggaaacctctgggaggctgttgtaaatgctgggctggggatggggtgggtctagagatccagatttgaagcaatttctagtctattgatagctgaagctcaagaagagagttagatgagcagaggtgaagagagaagaggacatcagactcttgagtaaattcagcttaagctcagggaggagtaagaaagggagacagtgaaggaagcagataaggaatattgggaagctggacaaacaagaactgggtagttgacaataccaatgaagagggaagaggagaggactttaattctttcggagatgccagatgagaaaaaattaagaaatgagtgagaaaaaaatgatggagtgattaaacatctatgttgctttcctttgagaatgttaactatgaaaagaagaaaagggtggtggtggctgcaaaccataggaaggctgagaaagggttttactttggttctgcctctaatccctgacgcattcaacctcctcaagccatttgcttgtaaacataactggcataaataatatctgatatgcccattttacaggacaagtgcttccctctcagaccacatactcgaggacagcggccgtccacgccttatttacattcatcttcccaacacaacagtcatttggaagatgccgagtggcgtgggaagaacaagcgggaacgagcgccgacccgcccgcggcctgactgctagcgcaccgctgtgcggccgcctcaccgcgcactccctcctgaattattcaccaccgagacgaggacggtgatcgcccccattccacagaggacacggagtgaaggcgcagtcacaggcccaaagcccccagtcggcgggtcttggaaatggacgactttttcactcaaaagctacgaggcaacaaagcatgtggatgaggagggaagggagccggggccaataattcatctcaaagtaaaagacgtccccgggggtggggaacaaacaaacaacaaaacccggctctgtgcttccgcgcttgcgctctcctaggtctgccaggctgccgcccgcgcctaggccagagtctcagtgcgcctgcgccgagcccgacttccgccagggctcgattggcttccaggctacttctcccggcccagggagggcctgcgctgtggctagagaagggagtctggtgactgggtgcgcgtgctgatgacgaaatcggaagtgcccggagcagaggcgggaccagaacctagagggcctcgggattgcggaagtttggtggggagggtcggagctctggtggagagagtgttgtctaaaacaagttccggaagggaggctgcccttcgcggtccgagaaccaccggcctccccagtttgagggctgttaccccgtgcgcgcttcgacgttgctgctgttggctctcctcgcccctcgttcccttgggaaccgcctgggaactccgccatgtcatccacttcgcccaacctccaggtatcattgctcatctcccgtccccctagggagctgggatcgaggggaggcgcgagaagcgggtggggggcggggagaagggaggaagcggccgcgcctgtggtcgaggcgcaggagggcgggtccggggacctgcagcaggtgggagaggggcccgttttccaacggaaaggtcgtttctggcccgctcttggggtctcccgagctactggctttgtgagactcttcacttttgttgacacttcccgcttccaaaccagccaagatctgggcaggtttctccaatcagggttaacggagaaagaaagaacgtaatttttgcaaagccctattctggaccagttgaagatagggtggtcatagttcggtcttagtttctcaagctgacagcagaccccttcattctgagctgtcaggtgagtagagatatgggaacagaccaagaatctgagattacagccagcctgcatgcaatctccgtgaagtcattgaatttatgtgcacactcctgtggctcccagatggtagtgtgtaagatcgaggagtattcttaaacctctgtgtggctccacttcccctcctctaccgcaatgagcacagtgttttgtacacaaatcatggaatcttaagattttaggcttaatcgttagtcctctgtggaatggaattcgttcagaaaagaaatttcttaatgtaatggtgtctcccatccccagaatggatctagggcttcagtggcgtttagaatgtaatgtggcttaatgtagaggactcccagtccagtaagtcaataaggcacaaaagagtagcctaaaatacttgtattgagtccccgtcgtggacttccggtagtttgttgaacaagcagttattggagtgcctgacagaggcatcaaaggtaatggaagaactccttaacccatgataattgattctgaagaaagaccactcaaagtagacccacttaaacagagattaaaatttcacacacacatacacaaaaagagtgggaaaggaggcttgcttgggactttcatcttgaaaatcgacctagaagattattaaaataattgttatctttcacaaaatattataattgtataattgcaacaatgactcattttgtggaataagtcaagtgttgatttgtctgtgtttttttccttttcttttctttctttttttttttttttttgagacggagtcttgcacggtcgcccaggcttgagtgcagtggcgtgatttcagctcactacaacctccacctcccaggttcaagcgattctcttgcctcagcctcctgagtacctgggactacaggcacccaccaccacgcccagctaatttttgtatttttagtagtagagatgaggtttcaccatgttggcccaggctggcctcttgacctcaggtgatccgcctacctcagcctcccaaagtgctgggattacaggcgtgagtcaccgtgcccggatgactatctttttcaccaaggttgtattaaactaagattcagcaatcttcacttgagttttttgtagctttttgtagtcctatttggaaaggttctttttggtaaacgtatttggaaaaagcgttggtcatttggtaaaagtatttttcccttgagtattaaaggtgactcttctgaagtgcccatcttgtcatcgttggctttttaacaatttttattccaccagcttttcatttgtcagagactttgcatgtgatttcgatactctacaacataatcttcatcatttgcaggtttttgttgttgttgttttgagacagtcttgctctgttgcccagactggagtgcagtggcgtgatcttggcgcactgcaacctccacctcccaggttcaagtgattcttgtgcctcagcctcccgagtagctgggattacaggtgcctgccaccacgcctggctaattttttctatttttagtagagacagggtttcaccatgttggccacgctggtcttgaactcctgacctcaagtgatccgcccgccttagcctcccaaagtgctgggttacaggtgtgagccaccgtgcccggccccagaatgcatcatacttgaattggactgttggctgttcttcagtgaatcagccagagactgaccaacatgaaaggcataattgttactcttaagcaggaaggatcttgaattgtaattttgttagtggtaggttcacatgtgtgctttctcattcaaccttttcaaccttctaacctaggaaatttggattaatattcatgtagtgattaacttcctgctgaacaaggcaaaaatctctgtggccagatgcttataatctaatgagggaatgcagataactaaaaatcaaaattatataatgtaataaagctgcacagtattctccacttccctgtggttttactttccacagtttcaataacccgaagttaacctgggtccaaaaattttaaatgaaatattctagaataaatagttcataattttgaaacactatgtcacaatgcctgtgtcattcacttcagttcatatcatgacgtaggcattttattatttcacataatcacaagaaggttgagaacagtgcaataagatgttgagagagagaaaccacattcacatcacttttattacagtatattgtaataaaatgtactgggcaaggaggcaaggtctgtgggatgggaggcggtaaggggccaaattagtagagtatccattcaaatgaagtggaaaggattgatcaaaggagaaaaattgaagatggagaagagtcaagcttgtatctgcatttatttttttttttttgagacagagtctcactctattgcccaggcaggagtgcagtggcatgatctcggcttatggtaacctccatctcccaggttcaagcgattcccctgcatcagccccccatgtagcagctgggattacaggcatgcaccaacacacccagctaatttttgtagagatggggattcgctgtgttggccaggccagtctcaaagtcctgaactcaggtgatccacccccgttggcctcccaaagtggtagaattacaggcgtgagccactgctccctgctgtatctgcattttaaaagtgagggaggaggaagagtctgagttttctcccagatttctgggttgggtatctgagtacccaactcaggtagggattggttctgggaatacaaaaggagagctatttggggccagggcaagggagcaaaataatttggttctaaacttgtcgagtttgagatgcttgtggagacaatcaaatggaaatgtccggtgaatatttgcatacatatgtgtagaagtagggagagtggactaggctggaaataaggatttattagcgtacaggtggtagcagaggttgtaggcatacagagtcacatcctggagagtttacagaataaggcaaaacaaagaccacgttagaaattctatggattagcgacagttaaggagagagaaatgggagcctggaaaagaattatgaatcaaaagtaaaaccaggccaggcgcagtggctcatgcctgtaatcccagtgttttgggaggccgaggcagcagatcgcttcagcttaggacttcgagaccagtctgggcaacatggtgaaaacccctctctacaaaaattagccaggtgtggtggtgcatgcctgtagtcccagctactccagaggctgaggtgggagaatggcttgagcccaggaggtggaggtaacactgaggcgtgatcacacccgtgtactccagcctgggtgacacagtgagaccctgtctaaaaaaaaaaaaatactaaaactagaagaaaatggtgtcatgacagccaggcaaggagacactgtcagggtatttgttgtgtgtgttaaatgctgcggagagggagtgagataagcatatgatttggctatcaggaggcagaaagcattgctgtgggagaaataggagatcaggaaactgggatgaacatgggtattctttgggattttgctgtggaggcaaagagatgagtgagatgtagggagaggagaaccgaggagctgaggagtgatggtgtgtagtttgtgttctgcagatgtgagtctgagataggacaacacatttttctgctgagggaaaaaaggaaaggttggagagaacagttgataggcatgtcattgatggagtaaatgtcagcagaggaaggtggggatcagctccacagcagaggagaaagaattggtctcaacagacagggcctgggacacctcttctgaggtaggtaattgtagaatttaccccatttctcagggttttctaaggtggatgtgtctggtactcctaagtggaacaggacaattccacatgttcccaacctttatacttccgtatggataactggatcctgactgatcctggggtgacacagtcattcagtcttgtgtcagccactgtgctagactctgggaatataaagaagtgaagacaacagacagaactgctcttctcctggagcttacattctaatagaagagagaggccaataaattaaaaaaaaacaaaaaaaacatatgcatgctcagacacacacatgcacacacaaagatcatcagccttaagtcactgatgtagggggggaggaaacagagagaaatgagtcccagcccacacctgatgaatatacttcattgtcacataagagaggaagaatcaatgaaggacgctgagaaggaggagccagaatggtgggaggaaaaccagcaaagtggtggttgggggctcagcagaggacagtgtccaagaaggaggaaataatcaactttgtaaaatgtcagaagatcaagaagacagagctggtgtttggatctagcatgctagagagccttgatatgagccgttttattatgtgatacaggaaagagaatagaggccactctggtgagatttttggctctaaaaggtagcagagaaacagaactaacaccgaacagtgttttgtcaaataagactttttaaaggagggctgtttgtatgtcgatggaaatatctagtggagagaaattgttaagaatgacagaagtgaagtaaccaaaaggaagaagatactgaaaaaggagtagggaattttttttttcattcgttaaacaatttcgagtacctgttgtatgccggcaccattctaggcatgggtagctcaaggtgaagtcctgtcctcatggaacctacctccctaaaggagacagccagtgggtgagcatacaggtaaatacaatgacagtgatgggatgagagagtgcagtgggggcagatagcaaagagaaggaatgaggtgcagcctttgctatagcaaattagggaggcctctctaaggacttgccatctgaactaggactgaaaaggagacatcatgcatctgtctggggaaaggagggaagagcattctaggtggaagggttcaactgcttgggctgcctgagtgcaggaggattctagggttcggggagaaccacacgtagctagggcccaggttatttcagaccttgtagatcagctctagcatcaggattttattgtttttaatgggagaccatcaaggttaccttttatgttttgaggtagcaagggtgggaacagactgaccactcacgaggctgggtagtagttttgacatatatgatagcagcttgaactagggtgttagcaagggagatggtgaggattatattcagaaagaaaattagctctggctgaaaagggaagataatgtttgatggaccagagcagatggagctggaagaggggaagacaggcaacagactctgccagtattatctgtctgagactgaagaactccagtcagtagtgaatgataacagccaggacctccagaggctgcaggcataaatgaatgaactcaatgcaaaagttcacctattgcaggaggagctacagctgctgcaggaacagggctcctgtataagggaagtagtccgggccatgaataaggagaaagtgttagtcaaggtgtatcccaagggcaagtttgtcttagatgtggacagaaacagcaacatcaatgacatgagacccaattgccaggggggcgctaagaaatgatagcgacacactgcacaatatcatacccagcaaagtagacccactggtgtcaccagtgatggtggagaaggtgccaaccttgatttaagagatgattggtggactggacaagcagattaaggacatcacagaagtgatcgagcagcctgttaagcattccaagctctttgaagcactgggtatcacacaacccagggtggtactgctgtacggacctctaggcactgggaagacactgtttgcctaggctgtggctcaccatacagactgtacctttgttcatatccctggctctgaatttgtatagaaattcatcggggaagggccaagaatggtgagggagctgtttgtcatggcatgaggacctgccatctgtcatcagctccatcagctcctcgcagctggaggggggttctggaggggacagtgaagtgctgcacatcgtgctggaactgctcaaccaactggacagctttgaggcccccaagaagatcaaggttatcatggaccactgcttcactcagggcacatcaacagaaaaattgaattccagctggacattttgaagatccattctctgaaaaggaacctgacccaggggatcaaccagagaaaaattgccaagcttatgccaggagcatcaggggctgaagtgaaagtcatatacagagaaagcagcatatatgccctgagggaacggcgagtgcatgtcacccaggaggactttgagatagcagtagccagcgtcatgcagaaggatagagagtaaaacatgtccatcaagaaactatggaagtgcggggatgtcctttgtatggatccctccggtaaagctttctggaatgaaaaaataaaataattagctctccagaattaaccatagaagacatggttaattttatttcaaatgaaaaatgctaacagacatggttaattttatttcagatgaaaaatgttaacagaaataaggttgaaatggtattcatcagcagaaaaaaaacagatgcatatcctcttaattcatcgtcttcgattaaaggtttaacgtgtgccacccagtacagtggctgcatgtggctattttaattacataaactcactcctcagtcacactagccacatttcaagtgctcagaagccatatacagacattctcatcatcagggaaaggctggtttaattagcactatgtttggagctagatgcttaaataatacccactgcagtataagagatttaacttaataaaaatcagtgtggtgcctcagtgaggcctgactgaatgagaggaacaagtggctgaagaggtgagtggcacagcatttcaaaatcacctgagaagaaaattatagttaggataagaaagagcttatttctaggccaggcacggtggctcacgcctgttatcccagcactttgggaggctgaggcaggtgtatcacctgaggtcaggagtttgagaccagcctggccaacatggtgaaatcccatctctactaaaaatacaaaaattagccaggcatggtggtgggtgcctgtaatcccagccactggggaggctgaggcaggagaatcacatgaacctgggaggcagagattgcagtgagccaagatggcgccattgcactccagtctgggcgacaagagtgagactccatctcaaaagaaaaaagaaaaaggatttatttctgctatgtggcttaaccactgaggctttgagatgcatttttttttttcttttttgagacagagtcttgctctgtcacccaggctagagtgcagtggcatgatctcggctcactgcaacctctgtctcccggattcaagcgattctcctgactcagcctcccaagtagctgggattacaggcgcctggctaatattttttgtatttttagagatggggtttcattatattggccaggctggtctcgaactcctgacctcaagtgatccgccctcctcggcctcccatactgctgggattacaggcgtgagccactgtgcttggcctcactctgtcacccaggctggagtgcagtggcacaatcttggctgtggtgcatttttatatgaccagtctgacctaaccaccacttgactgtgtgactccatgttttatgttcatatactagctgataaaacttgaaaatttagctttgaatttaggctacttgacctgtgagatacgtaactattacattttatcaattctgaagtaaaccatttatttttcttccctgctacaatagaggaagcatggtcttccagcgggagacctgttcctcccatttacagatctcagcccagttatatccaatccatgctcaactgccccaaaatgtaatattcttacacataattggtttttgcattgtttgaatgattttttgcttatgttatatacttactttttaatatctctaacaactgtcaattttcatttttttttactggcacctatttctgttgaatagttttactacctaaattaacccagttggaatgttttaataagtcatgtttgccctttatttgtatgtatctgtgcataatttttttttttttttttttgaggtggagtctcactctgttgcccaggctggagtgcagtggcatgatcttggctcactgcaaccaccgcctcccgggttcaagcaattctcctgcctcagtctcccaagtagctgggactataggcgcatgccgctacgcctggtcaattttttgtgttttagtagagacggggtttcactgtgttgcccacgctggtcgcaaactcctgagctcaggagaattttagtttgagataattgtagattcacacgcagttgtaagaaatactgagaatccagcattccctttatccagttgtctgcagtggcagcatcttgtagaactgggacaatatcacaaccaggatattgatattgatacattccaccactcttactcatattttcccagttttacttgtccttatgtgtttttatgtgtgtgggtgtggttgtttgtgcagttttatcacatgtagatatgtgttacattttgagagttctttatgtattctcgatactagttctttgttagatatgttttgcaaatatttctcccagtctatagattgtcctttcatccttttaacaaaatcttccagagagcaaaagttttgtcataagatccagttacctttttttttcttttatatagtatgcttttgatgtcaaatctaagaactctgcgcatccccagatcctaagttttccatgttttttctaaaagttttagctgggtgcggtggtgtggacttgtgatcctgctatttggggaggctgatgcaggatgatcacctgagcccaggagtttgaggctagcttggtcgacatagtgagatggagccccgtctcaacaaataaataagaatcaaagttttgtagttttacatttaattctatgatccatttttgagttaatttttgtaggaagtattaagtttaagtcagaattcttttaggtgtatgcttatggatgtctagttcctctagcaccacttcttaaaaagcctgactcggtgccattgactggctttttgcatcattttcaaaaatctcttggctttattagtatggatttatttctgggactttttaaaaaaatgccacaaaagtagtccatgttccttatggacattttttagaagatgtgaaaaagtagaaaatgaaaaatatatgttttatcaaagataaactctgtttaacaatttccttcccatctttttcctgtgctgcttttttctgctgttgtttcaaataaattcctgctacatataaaaagttgtgtcctgctttttaaaaatgcccattattaacactttccatattattacaaatatttcttaatgttattttagtgatcctttggtgttctgttttgtggcatcctttatgatttaagtttccaggttttgtttttgttatttaaaagacctctctgataatatctgtgctcagtaaaccttttagttaattactggattgaaatatatgagtatttttcagattcttgatatttcattgccccattgcttctgaagaggtttcaccccatttacatttccactattgttatatcttttagattaaagcagcatttaatttttgagaatttctctaaatgcttgtttagtttgaattttcacattctattatttcttattagccctaaatttaactttagctaagtgaaaattacatgtaaatgttagcgattggtactaaagtaacattcagtagcatttattcctataacatgtaatttgcatcttttcaacttgtaatttataataaaatacagttgtgagttagaaaaaaatgattttttagttactgtttattttttacttatttttgttttctttcacagcccagcaagctgagaagctttaaaaaaaaaaaaaactttcagtatgattatttacttcaaatttatgtttatgctttgatttaaatgttgttattttgcctccctcaaacagaaagcgatagatctggctagcaaagcagcgcaagaagacaaggctgggaactacgaagaagcccttcagctctatcagcatgctgtgcagtattttcttcatgtcgttaaatgtgaggccataggttatattttatttaaaaacacgaaaaggaaaatttattctgtttcatttctaaaaaattgaaatataatgccagacaattctaaacgatccatttgttaaaaaaaaaaaatactccactttctttctagtgatttttaagtattgagatgtagctagcaaatgtgacagccatcatagttattactttgtatatgtaaacatcttaaaatgtagtctagtcagtggaaaataggttaggagacattctatttgtgtctttacagatatgtattgcgtgtgtaccacgtggcaggcactggggatacaatggaaagaaatggttaagacccctgccctcatagctcttaaatggaatgcagttagatgattgaagatgttcttttgagcttctcccatttagttctgaggttttatgttaaagtgagactaagaatgagtcataacctgtaagctatgtggggctcatcccatctattgcacgtgttgccaaagttcactttgaaaacagctctgacagaggcctttgtgtagtaaaatttacgatgttggtattacacagaatatatgggatttccatcactttactcttctgaaataaagcttttgtagacattcatagaaatgattaatactgctttccttctatttgtcttttttataattgggtttgtctaagacaagcaactttgaactatctgcaaaaatgtaagggaaaaatatgaaagcttcagaatattaaataatttcctgttagttaacattaacttaatataccctgctgtcttgcttaggttgtttctgattcagacccactgttggtctccaaccctgctggaggaaggggtagaaaagaggtgataatcattggctatgatgagttagagatgatcttccctccttcttccaacatagaatttccttgtctgaaaaaatacatatttaagagttcaaacctttctacatagaatactaatggaaaaaaatctctctcatttccctttaatagatgaagcacagggtgataaagccaagcaaagtatcagggcaaagtgtacagaatatcttgatagagcagaaaaactaaaggagtacctgaaaaataaagagaaaaaagcacagaagccagtgaaagaaggacagccgagtccagcagatgagaaggggtacgtgtttaaaattgttcaattttattgtggctttttgctttcgatttgtgaaatttcttttgattaaaacaggtgtcagcaaactatggctcatgggccaaagctgcccagctgcctgtttttggaataagctttatcagaacacagccgtgcccattcttttacatattgttgtctagggctgctttcgtgccgtaacaacaaagttgtgtggttgtgtggagaccgtatggcccacgaaacctaaaatatttacttgtttggtcctttacaaaaaaaagtttgctgacccctagtttgccaagttgaatggataatattcctcaaacaacccttcctgactgcctgctagtaggaggagagaatgcttgtaggaatagtactcagttactctctggccattagctaatatggaagcttaaggttataggagtgaccagagagttaaacctttgaccacatggaaaaaatgaaaagtaactccaacaatgtaaattttttttggatatcttatgcaaaattttttgatgtgaatttgtgttagatttgctttatgttgtcattgtaaagaaaacaacacagcataacttataaacgttgaaactgatttttggcatgtcttcctagatgggggatgtatcacttctagatgcagaatttgtttattcagtacatgacatatgcgtgccaagtttgtgctcagcactgggaacatattctaaccacatcctctctggctgtcctattaattgatgccagtagttccaggtaacacacccttaagaaaatgagactctgggatggagttatctggcctgcttgggtttgaaaacagcgagattctgctcagctttagaggatgtggttctcattgttcatggtatgcagtggcgcaggttatttagacaataccctgtggtcacaaggaatgaagtgccttttaggcagtgctttggggcttcgtggctgctaccacagaccatttggaagtacatgaggaatataagaaccagtgttgacttggctgcttcaaactatgtggcagagtttgaaggaaatgataagcttaagctcaaggttttatattctctgttcaagatgtgatcggggaaccagggagtttctgtgacaccctaagaacatgttatcttcttcatcgatagcactgacttaacaaaaatcagatgatagtctgatcttacaaattactgaattccaacttagggtttcttatatgaaagtgaggacatttggtataaaacagggactccaaacatgaagtgaaaatattgggaagaatttagttgaccttgactgcccaggacctccagctgtcactgagactcccttgacagcagaagcttctcttcccttgtccatagaagctcttctctcttgcttgaaaaccctgtaaggatctcttctgagatgattacctgacaaggcgatgccagtttttcttttgtactgaacagcaatcttcgtttacagtaggacccactttggctaatttaagcaaaaagggatatattatagggtattaccttacagaatagtggggccagggaatcaggagaaatggccaacagtaccagggttgttcaagtagggatcccactgttgccaactcctctgctaagcactgatggtgcttgggagcaggtagtaaatcctctgcgcagctccctcagcaaaaccagtgccttcgcctgaagattctgtctccttgtgagcagcccccaccttcttggaagaatttaggtctcatgtggaaccctagctacaagggagatgagaaacggcagggttttttttgtttgtttgtttttaataaggacagcctttatagtactggacagcatgatagaaagaggttggagtgagtgtcatgtgaatcttttgcagtgtctacctcacccacagccccaccgtcctatgataaccaaggcaattccattttggcataaaacatgtcatgcttttatctccctttatatgttattgttttaaaaatgatataatgccttatttttggctttatcacttttatacttaacattgtatcaggaatatctttccaataaactatttctacatcacgtttaaatgttgcaatgtatcctgtcatatgctagtccctataatatgagttactttttccccttttgcaaacagtgtgggtgtgattatccttatggtcaaatgcttgaacttgtctaaaattatttcctcaagataaatccctagatatgaatgaaatgccttgatcgacctacttgttctttgggtgtagttcattgtcatcaggaagcttcctctgtcctttggaatccccagactaagggttgtagacctttgtaccttagtgttccagatttttttcctcctaatatgacctcttgttctaatttatatcttgcccagtcctgatgtttttactgttgttgtttgcagctctcctgtgattcatcttgaatccttcatggagtgatgtgtggggcatgcatttatgaattaatacatacctaaatatgtcatgggaatttggagctagttcctgacttcattctggtctttttgtccctttcttttacatgattctctattgatgataacgtgactgcttcttatttactacattctttaaaataagtaagcataacttttaatgtaaatgtctgattttgccactgaaattacaaatatttcaggttaatttttccttcatttttgccttatttgatagcaatgagtgatcatttgaatatattaaattctttttattaggaatgacagtgatggggaaggagaatctgatgatcctgaaaaaaagaaactacagaatcaacttcaaggttgctttagatttcatttttaaatttactatcctattaaaaagactcaaagtgaattgtctatttgaattgtttttgttctccctctatatttaaatgaagtttaagaactggctttggttcccaatagtcatgtgctggctttgtttagagtgttttcttagggtttgccctctaggatcatggtttggtcttttttatgtaatagttttgttggcttcacatctgcctttaaaaggctctcagtcaacttgctctttctttttgtttatttgccgccttttagagaaggtaacacttatactattagcacactgcaaaatttgatggtattaaaatttactactgtgggagaagttaggacttacacgtggcttttattgccgttgctgtagctcacttattgatggtttattttgtttcttaactgctcttcatctgcttttcagtgttcctgtttacatttaattgtttaagctttctgtgtttaccatccacacctgtaaagccctttcattctgttctactatagcacagtggcataacagaggggacataggtttttggctccattcagatcttgattctgttcaagggtctgccacttagaactttctaattgtgggcaagtgactgaatctctcagaaccagcgtcccccatctctaaaatagaaatgagcaatagcttcctttcagggcttttaagattaatgacagtgtaaaaactacctcatatatctgacgaagtctagggactcaataaatggtagcactgtttatctaaaaaggcatctatttgttggctggctttgttaatcactgagatttgattattcttcgaaataaattatctaacaatttttcagattgaattttttgctcacccattggtagtatgtattttgttcatttgaatcttaccaaatagaatgcataactgggaaggatttccattttataggttcagccttggttactgaatagtgaaaatacttacctgagccaaacttttagccttgctatactagtgtcttcgttttggtagtatttttgtcttgcctaccctactgggatgtctaggaaaacactgtaaggataatgtgttgacaacagaccaggtaatgaatagagaacatctttagatgccaagaacttcagtggtagatatagtccaagggcaaaatcttgagtttacactcaagcgtagtggtgtccccaccacctgaaactactggcacacactgcgcactcagttggcatttattgggtaacccagtgggtctgtgccaagtggccttattccagttgtaaagcaagacactttttttgtctgctctattggatttggttttgtttccctctccctaccctgccccaggtaaaaatcagttgcatatctttaattttcgaaaagatacattttttttttcttttttgtttttttgagacaagggtgtcgctgtgttgcccaggctggagtgcagtggcgcaatcacggcttactgcagcctcgaactcctgggttccagggattctcctgcctcagcctcctgagtagctgggaacacaggcacacaccaccatgcccggctaagtttttttttttgtttgtttgtttgtttgtttgtttgtttttgtagaggtggggtttggccatgttgcccaggctgctctcgaactcctgagctcaagtgatttgcccacttcagcctcccaaagagctgggattacaattgtgagccaccgcacttggccgatacaaccagtttttaatagggatttctctaaattccctatcacttacaataaaggccagaaatgtaaaacaaacaaataaaagagaaaaaaaaccaaatacttaaaacatttaaatgaggaaatgtatttgaaatttcaggatgaaatagaatatgaaaggagtcctagccttttatatttgaatatccttttttttctactttttaatggtttgctgctggatttcatactattgtatcttttttgaatttttccttgttttttgaacagtattttaaatcttttacttctgttttagattatgatattaagtgtatatttgttaaaattaaaaatcggtttgtgatttgagttttctgttagctaattttattcagtgaattttttgtgattaagtaatatactagtaaatagtatagtcaaagaccggataaatttatatcattggaagtacattccatttgttagcatttttcataatcccatcccccctttttaattttgcaaaccatgtctagtatgagattgtttatcagtaaacattccaaagtcaccttttaacttagaagtattatatatgaaaacaaatcatgacacatttttaaaatttatagcagaaatcttgagtcagacggtatacatatataaaataaagtttatttttgtttaactgacatgaaatcctaggattactaatcttaatgaaacataaaaaagacgaaatgaatttacttttttcttactttatagtagtctgaacttttggaatacaaaatgcttatggtttcatgtaattttaatctagtagctaaagattttcataatttagggaagtaagttgctagtaactagtcttagagtaacagattatctttcctaacaagaagaaacaatcagtagcagtgatttcataaagtaatagattgtataagtggtggtgttctgttacacttaaaacaactaactacatgtcatcttagaacaggctgcttcatagtttatagtggaacagtttccatattctagaaaattagaaaagcttttgataaaagagaactagaaaatttgtcagtaggctatattaaaagacatccttcttggactcttactgcaataattgctttggcttttgaatatactgcattcagaagctaaatcttccctgtaagttaactttgttaattaacaaaagttgtaaatagatctatttagcagccaaatagaaacttgggcaaatcttaggaaagtattgcaaatctgcaggggtatcttttctcggtttcccatcatctgcttccattccttcctttcctctctccttttccttctcccttctgtctgtctgcctatcttgagttaaatttgttaagcatattttttttttcagtggttgaggagaggattagatcaccttttcttttggttaacaggagaaatggtagaacaagtacttttgatactccaaaatcaatgtattcaaatataaccaccttatggaacgtttggtgcttttccaaacactctaatattcattatgtcatttgattttcgcaccaacctatctaagtagtttgggcagatggtattattttcatttcacaagtgaggaagctgaaacagaagggtaaagtaacatgccccaggttgtctagtcatccacctggttcctagtcctattgactactccctaacacctgcttcctgctcacgctatttcaaaaaggttgttagtacataaaactttcccaattttataatgcgtttctttaacatcattatttcatgttgtcttctaactttggtgaaatagtctttcttaatttaaagataacgtaattttttgcaggtgccattgttatagaacgaccaaatgtgaaatggagtgacgttgctggacttgaaggagccaaagaagcactgaaagaggctgtgatactgcctattaaatttcctcatctttttacaggtgacataacttttaaataattttatttcatgagtttgtaaaagttcattgatgactgaggtgaagcattgtcattcttgtcactaatgaattatcttaaataaattgtgactgttaaaaggtggtgatatatctttatacaagatgttttatttcttatacatatccatatttgcagtgtatatatattgcaaaacaacctaaatgtcaaccagtagggtaattcaccaacatgcagtggaatactatgcactcagtaaaatagagtgtacatctacattaataaattgaaatctgcattgtattttattgaagaatgtccacatctattgcaaagatcaaaaagcagttataaactgaatagtatgattccatgtttgctaaatgtgtatgctgagaagtaagtatagttagattcacatagaaatattaatatatgcctaggggataagattataggagatttttacttttgactttcatctgaatttttgcaatggttatgatttttaaagagtatttcttaaaaagaggagtaagaatcacttaacagtttcagaggaagtgcataacctctagtagcaaaaggacatttcattatcactgtgaagagaatattgctgacctaccatctggggaaacttacaagttctagttccagcagtaagtgatatgtctgtgctaaaccattcctttatattatccttcttgtgactgatagccttgactgtaatatggccacacccacagtctgacagtcagaggtttttccttttgcaaacatgttggtttatgtcaacagcaaatctgcaatgttggcctcagactgaagagtccagacagtcgtatcgtatagagcagtgatgaagagcaaaaagcctgtaggccacgcactgtccgcctagcttcaaggtgcagtttactacccaacttcaggagtatgaaacttaacagcataaaagttgacatcataatcctataaaagcacaaaaatatggttgaactcattttatggtatattacttataccactttttctcaaacatgagtcattgatgtatcatcttcatgaatttttccatgtatgtgtaccattactaatttttaatatttttctttgcttattttttagaacaacatttttactagagtatagcataaatatacagagacatacaggagcccctgggtgttgggcttccttaattgtcacaaagcaagcatgccagtgtcatcaaccagatccagaaataacagcattgccagggacctggcaggagccttctgcctcattcctcccgagaggtcatctctctctctcgacttctaacgccagagattattttgcctgtatttgaactttaaatcatctcacatatttttacttagtaacgttattgaaaagactgctttgtgcctttataagtggaaaaaaaagtgtttttccaatacacattaaaaaattatttaaagtatataccacctaaaagtacttcatgttataccagtggtatatgtaccatactcagacactgacttgtaaatgtatacatgtaaaataggaaaatgaaattcaagtaacagttgctttcataacagttaagtgaaacagtgttattcatctgcatatcattcttttgcagatactgtgtacacatccatagtttgcacctagcagttttttttgttttgttttgttttgtttctttttttgagacagagtttcactcttgtcacccaggctggaatgcaatggcgtggtctcgtttcactgcaacctccacctcccgagttcaagcaattctcctgcctcagcctcccgagtatttgggattacaggcatctgccaccacacccagctaatttttgtatttttactagagtcagggtttcaccatgttggccacagttgtcccgagctcctgacctcaggtgatccgcccatctcagcctctcaaagtgctgggattacatacatgagccaccatgcccagccatagttttttaaatgtatgtttgatagtttactgccagctgtaacccacctgttttattttaggcaggattataattgctcattagcaaaattgaggctcgaagagttgatgtattcactggttatattttggcaaaactaggatttaaagtagtatcacctttttgttacccaaccatgaaagtctgctacctagctggaggctgaggtgggcagatcacctgaggtcagaagatcgagaccagcctgaccaacatggtaaaaccccgtctctactaaaatacaaaaactagccaggcgtaatggcgggcacctataatctcagctacctgggaggctgaggcgggagaattgcttgaaaccaggaggcagaggttgcagtgagccgagatcgcaccactgccctccagcctgggcaacaagagtgagactctgtctcaaaaaaaataaaataaaagaaagtctgctacctataacactaacctgtgctttcctgtggaatcaagaattcagcagaaactcacaagtcatccaaactttgttaggttcacttttccaaagagcataaatattcaaagaaaatctcttccagctgcccattttttatggatataatttttgtacaatattctggtatcaagcagtgtacacagtagatgatcagaaagtaccttttaactgaactcttttcccctactagactccacgcagggcagaaatccttttgcctgtgcacatgttacggttttgatacatattggttgaatgaatgagcaaacaaatgtacttcctgttagaaggcttatgttatgcaagtctctttttgataaagtagtctctagaagaaacaaaatatatttaagacataccttagattgatttatttttaaaatattgttttgatccttagaggtttagagtgaaaatctttccagagtattcctcagtatagatgatacaattaagtgttaaaattctcatgacatttttctaaatctaaattttaggcaagagaacaccttggaggggaatcctattatttgggccgcctggaacaggaaagtcctacttagccaaagctgtagcaacagaagccaacaactcaacatttttttcaatatcttcctctgatcttgtttctaagtggctaggtgaaagtgaaaagtaagtagtaaatcaattttttaaagttttttctttgcctgtaattactgtatcactccttaatagatttcttacatcacttatagatattcagagaagtcatgtaatacaggtactcacttctctgtcaaatcagtctctaatctagaatttcttttgtgggaaaagatagcatatatctacaacctagtgaatcataaagtgaattatccagttgtagcattcttattttctgtacctgaaacatgattaggctttttaatctacagagttcttgtaatattgatatattactttgttttaatcttttactattttttagagacttaaaagttttcatttatttttagactggttaagaatttattccaacttgccagagagaacaagccctccattatcttcattgatgaaattgattctctctgtggttcaagaagtgaaaatgaaagtgaagccgcacgtagaattaagacggagttcctagtgcaaatgcaaggtagtgttactaattttttttttctttttgagacggagtctcactctgtcgcccaggctggagtgcagtggcgcgatctcagctcactacaacctccacctcccaggttcaagcaattctcatgcctcagcctcctgagtagctgggattacaggcgcgcaccaccatgcccggctaatttaatgttactgatttttaaagtcgtttttgtttattttataacaatttttataacagtaatgaaaaattcaagcagaatttctccattctaacaaactgtttcattttgccatgtttcattccaattgtcttccatatgcatacataatttttactcaattgtaattatcttgtaggactcactgacataaatagaaaagagatttaatgtattcatttataatgtaccaggaacaacttcagtaaaagtaatatgtagacttcgaatgaaatttttcaagaaatattttgaaacgaatgttaatagtattttccacaatctgggagatttgattcatatatttgcatcatattgcatcatagtgtatttggatcatattgccgtaaggtgatatttgattaaatacagttcttttccaaagacagactctcaagatgaagcactttaatggtaaagcaccacatttcttaacagaatatatggaagaagtttaaagaacaccaaaatgacaaattaattaaagcattacctattttaatgcaggggttggtgtagacaatgatggaattttggttctgggagctacaaatataccctgggttctggattctgccattaggcgaaggtaggataatatagtaaatatcttatttctcactgcagatgtaacaagtagatgataattctctttttgtcttgtcaggaagcattctaacaacttttcaaaagatttgtaatgtgctctaaccctgttgctcccctgccttgagtgggagaagggtggtcatttgcttgtttgtttccctagtttatcaaatatacaagatttccacacacttctgtctttcatattagaaaatatattacctaatgcttacctttcattctgattaagtttggtgggcactgatgcttcaaaaatttataaacatagtttgacaattcagtaaaaaccatttatataaaattttagcaaaatggcaattctataagtcaaaataagataaccaggtaagattttttttttttttttgagtcggagtctcactctgttgccaggctggagtgcggtggtgcgatctcggctcactgcatcctccacctcccgggttcaagtgattctcctgcctcagcctcccaagtagctgggactacaggtatgcaccaccacgcccagctaatttgtatatttttagtagagacgagatttcatcatgtggccaggatggtctcgatctcttgacctcatgatccacccgcctcagcctccgagagtgctggaattacagatgtgagccaccgtgcccagccaagattttttttttttttagtaaaaactatatgtcaggccgggtgtggtggctcatgcctgtaatcccagcactttgggaaaccaaggtaggcagattgcctgagctcaggagttcaaaaccaccctgggcaacgtggtgaaaccctgtctctactaaaatccaaaaaaattacctggccatggtggcgcacacctgtctgtagtcccagctactcgggaagctgaggtgggagaatcgcttgagcccaggaggcggaggttgcagtgagccaagattgtgccactgcactccagcttgggcaacagagtgagactccatctcaaaaaaaaatatatatatatatatatatgtgtgtgtgtgtgtatatatgtatatgtgtatatgtatatatgtatacacacacacatctatctatctaatttttaagttgaaaatgaaacttcagttctaggaaaggtatacggactcttcacttttcactcttcacagttctgtattacattcatttattttgtatggtaaaaattagcacttcagtttttgccacttttatcccattcacttgatgatttgcgccagcattctagcttaccatccagtaccaagaaaggaaatgtgcagggtatttttgaaaaattgccttattctgcacccatctctagaggcaacggaaactttaaattcttttcattgtcacagagagttacctggagaaaaaacagtctgctcagaccacttaaattatccctcatcgttgcttctctgtctccaaataccgaaattctaagaaagcaagcaaaattattgttaatgaaacatagtgtttattctttataatataggattgttctggatgtattcattaaagtggacattttgtgtaatatatatcctataagattgtgaggtaattctgttttgaatgtagagaattactgtgtcatctctactcctgttttatattgttaatcattagtcccttgatcaagagttcagagtacaattttgtgggaaactgtaaccctgtaggacctctttttatttcatgaattccagacataggaacactgtggccaaaataacccaaaaatgcacgaaagattcagccacttcaaactggctcccaggctattttgattttatttgtttgtttttaatgtgttctggatattatccctttaacctaaatatatatgtttaaccttggcacatacaggcccacttaacttagtatctgtttcttcttggaaatatcctaattttcaattaaatatattcttgatgtaatttctcttttaagatttgagaaacgaatttatattcccttgccggaaccccatgcccgagcagcaatgtttaaactgcacctagggaccactcagaacagtctcacggaagcagactttcgggaacttgggaggaaaacagatggttattcaggggcagatataagtatcattgtacgtgatgcccttatgcagcctgttaggaaagtacagtcagctactcattttaaaaaggtaagtcatttttatctatcctttcctatcttttttttttttttttgagacagtctcactctgttgcccaggctggagtgcagtggcactatctgggcttgctgcaacctccgcctcccgggttcaagcaattctcatgccttagcctcctgagtagctggaattacaggcgtgtgccaccacgcctggctaattttttgtatttttagtagagacaggatttcaccatgttggccaggctggtctcgaactcctgactccaggtgatccacccacctcggcctcccaaaggcgtgagccactgcgcctggcccttttcctgtatttttaaaatcaagtttcaagaccgtcattggtttgtcttcaaagaatttgggaggatttcagtgttgtataataataccataagtgggtttacataatagacatatttctgtgtcactgaaacaagttctttaataaagtttatttattggccatttttggctgggtgcagtgccccatacctgtaatcccagcactttaggaggccgaggtgggcagatctcttgagctcaggagagaccagcctcaggcaacatggcaaaaccccatctctgtaaaaaatacaaaaattagctggatgtggtggcacactcctgtagtcccagctacttgggaggctgaagtgggagaatctcttgagcccaggaggtggaggttgcagtgagccgagattgcaccagtgtactccagcctgggtgacacagtgagaccctgtcttaaaaaaagaaaaggccttattaatcatcctaatgtgttttaaattttcctatgaaatgatttttgaagtatttgtgtattattttgatataagtatagaaacttaaatgtacagatgtaaggctgcttctgacacatctagaatatttttgagtagaatctggtgcatttatacctcataaagtaaaaataataatagctaatatcttttaaatattcacatgcctggcactgtgttctgtcttttatcttactatttcatttggtcttcacaaaaatcagcaagagaggtacatgtagccagccacctaatggtggttagtcttggacgtaggtgctaacacagtagctagagtgggacagacatgtgatttgcctggaggtgaggtgtgtttccaaatctgaaatctcagccattctgctatcctgcccctcctgtgttctgttttgtctgcaagaacaagttaagcatctgtggctgagataaagttttataagaaggctgtggtcttgagatacccagtttgagtaacaatgaactaggtaatctggaccaacccttttgctgtgaacaacagtatccagtattactcatgaacatacatgtgaaaaactattagcaaacctaatctcataatgtatgtcaagactaatatgactaagtcacatacgtatatttatcatgtaccataataagatttttttaagttaacaagcttgaattaaaatctgaatttgaagcctggcaccatttacttgttatacctttttgagcaaattctattacttctttaaagctcatttttatcatttctaaaatggggatgtgataatgctattttgaagtcctttccaataatgaagtgatataatactcataaaacaccagtcgtggtacttcagatgcgtagggaatgttactcatccacccttcttcagccatttcattactgaagtactgttaagtttatgccacagccattatgttttttcttaaattctctttgccatttagaaactataaatgcataggaactcagtcctttcctactgagagtttgtcactcaattctgcatattactgccagggtgagctcacatgacgctgaagccaggtccttgttagtgggatgaaggtgacacagccagatgagttttatctctgcagctggggatcaccagctgcagcagacctctcagcggctccatcctttacttcttttaaagctgattatttcagttaacaagaagaagattccctgtttattttttgcatttactagtattttatttctaaaatactaatctgggaccggtggtagatcagaaagtagagcagtcaaaaaagacaaaaatccctgacctcatgcagctaaaatattagtgagtaaagacagtaaaatacacataataaggtgagagcatgtatttcttcacatctacactaatactgagataatatttaaagtcgattattgtgaaacagatgtgaaagtgcccccaagttggctgggcgcggtggctcacgcctgtaatcccagcactttgggaggccaaggtgggcggatcacaaggtcaggggttcgagaccagcctggccatcatgataaaaccccatctctactaaaaatacaaaaattagctcggcgtcagggcgggcgcctataatcccagctactcgggaggctgaggcaggagaattgcttgaaccctggaggtggaagttgcagtgagctgacatcgcaccactgccctccagcctgggctacaaagcgagactccgtctcaaaaaaaaaaaaaaagaagtgcctccaagttgatgcagactattgccatctaaatgtttacatgtgactatgtcacaaagattctttttctggatattgttaaaacttataaataagttgtacatgataaaatggcattgatactgcatttagcatacaattttgcacttagatttgagagcatttttgttgaaagagattcagtagtttcatactaaagttccaaatattacagaagtttctcagctatagagcaacttctgagaattttttaatatatctgtttttggtctttaagattactaccacttattaagcactagaggggaaaaagagaaagccacaggtaactattttttttttaactcatcttctatgtgtgatcatacaagcaatttattgtaggaaatttcaaaatatagaaagcatcaagaaaaaaactaaaagcagctgggtgcagtcgctcacacctgtaatcccagcactttgggaggccgaggctggcggatcacaaggtcaggagatcaagaccatcttggccaacatggtgaaaccccgtctctcctaaaaataaaaaaaaattagctgggtgtggtggcacatgcctgtaatcctagctactcgggaggctgagggatgagaatcccttgaacccaggaggtggaggttgcagtgagctgacatcgtgccacttcactccagcctggtgacagagcaagacgccctttcaaaaaaaaaactaaaagcaaccaaaatctatcccattacccaggggataactactttttgttgtatattcttaattttttttccaaaagtaaacattctaataaaacatacaaaactattatacattttaactttcctggtaatggattaagtcttaatgttcaattttgtttcaaatacatatttcagattactgtttatttcaggttcgcggaccttcccgagctgatcctaaccatcttgtagatgatctgctaacaccttgctctccaggtgaccctggtgccattgaaatgacatggatggatgtccctggagataaacttttggagccagttgtttccatggtttgaaattttgtttgtttttaagaaaatattttaaaacattatacttcataattttcagttatataagatttgctggaaaatcttagtataaacaggtgtattttacttaatattgttgactcattaaaaattatgaagttaattgaacttaaaatataaaaagtcattatttttaaactattttcttgggtttagaggaacctttaagtgaaaaagctattttttaaagcacaagattctgactttacaggtcttatagctagaatatctccaaaatgctcatatatagtataattattgtaaagacctaactaaaaaatagggttggtgaaatattttttttcccctgcatctcagattttttaaaataaccagaagtcacctgtaatcccagcactttgggaggccaaggcgggcagaccacttgaggccaggagtttgaaactggcctggccaacatggtgaaatgccatctctcctaaaaatacaaaaattagccaggcagtgtggtgcacacctgcaatccagctactcagctgaggcaggagaatcacgtgaaccagggaggcagaggttgcagtgagccgagattgcacaaccgcaccccagcctgggcaacagagcgagactctgtctccaaaaaaaaaacaaaaaatagggccaggtacggtggctcatgcctgtaatcccaacactttgggaggccgaggcgggtggatcatgaggtcaggagatcgagaccatcctggccaacacggtgaaaccccatctctactaaaaatacaaaaagttagccagacgtggtggcacgtgcgtgtagtcccagctacttgggaggctgaggcaggagaatagcttgaacccaggaggcggaggttgcagtgagccgagatcataccactgcactccagcctgggcaacagagcgagactctgtctcaaaaaacaacaacaacaaaaacaaaaaccagaaatactaatgcttgtatcattgtttttatagtgttttctatttcacttctcaaagctccatagaaagtttaaatattgtagttctatttttatttttaaaaattacagttaatatagtttatattggaagaattaaaataatctacaagacttactttgcaaggcatgttatttttagggaacttagggtgattgaaaagttgtttacttacagaagaacattctcagttttcaaaattttctgtcagtttcagatcttcaaagacctttaatggcaggtttaatagtaacttccagaggagaaacttttacacggtacatagatatacatgtaaatgtgtatacacccatatatttgtgtgtgaactaaccataatgcttatctgagaagttactcagaaacccctttgttttaatccttggtgtattattttttattttttgtactttgttcagctttgaagaatttttagtaacttagagtggtccttttcattatttttcatatccttttacaggagtctaggcttagaagttagttttttaatgaatctctgatattagcatatttttctaaccatttcgatcttaattgtaactaattattttaaaattctggttagtagatttttcatagaatggtattctgcttcacttaagtgtaagtgaatgatattttccttttgaattatactgacttggaaaattgatctcgtttaagaaaaagagataaggccagaaattagatcatgaacatactttggaggccttgatcctcagactaaggggattgtccttctgataagtattggggagccatttgatcagttcaggggaagaaagtatacgtttctacacaaaggaataacatgatcaaagatcatgaaagatctgtgaaagaataggggccgggtgcaggggcccacgcctgtaatcccagcacttcgcaaggcagaggcaggcggatcacctgaggtcaggggttcgagaccagcctgaccaacaaaacgaaaccccatctctactaaaaatacaaaaattagccaggtgtggtttcaggtgcctgtaatcccagctacttgggaggctgaggcaggagaatctcttgaacctgggaggcagaggttgcaatgagccaagatcacgccactgcgctccagcctgagccaacagagtgagactccaactcaaaaaaaaaaaaaaagaatagggagtttatcgttagtatcttatggcagactgcaaatattcatatttaaacttaggttaaagttcatagcaataatgataatatgacggttttttattttgttaactctattattaatatcctccctacccttctttttccctgacagtcggatatgttgcggtcactatctaacacaaaacctacagtcaatgaacatgacttgttgaaattaaagaagtttacagaagattttggtcaagaaggctaagccaaagacaaggaagatgcttaccatatgtattctttctttcatagatatttttgtctatttggatcgcattaattgtttccagtaaaactcttttaccacagggaaatacacatctcacttcagagttccattaggttttatattgtacttttcctccattacttattaaatactcctattaacaaaaggtacaaaataacaggttatgaggaaatgagcgatatatgaacggcataaaaacagaaattacccagtaaaaaggatgtcagaaattgacatacaaatatttacaatttttatgaatggtggtctttgcaaagagcatttatattttcttttttttttactaaaatgatatagggtttattttatattttcaaaaaaattgttaaacatcattcttatcaatgtaaaatttacgttattaaaaaattacaaatgatagaatctttactcagggatgggcaataaaacagcaaagagctttgtgattgggtttgaaagattttgaattatagacagtgctcttaatagtttttaataagttgatatttttttctgtgtagatttaaataatttctttaaaagcgtaagctttggctgggcatggtggcttatgcctgtaatcccagcactttgggaggctacgatgggtggatcacctgaggtcaggagttcaagaccagtctggccaacatggtgaaatgccgtctctactaaaaatacaaaaattagctgggcatgatggcgagtgtctgtaatcccagctactcaggaggctgaggcgggagaatcacttgaacctgggaggcagaggttgcagtgagctgagatcgcgctactgcattccagcctgggcgccgagatagcgccattgcactccagcctgggcgactgaataaaactctgtctcaaaaaaaaacaaaaacggtaagcttttatatttaattaactgatacctttcactgtgcaatctcaagaggaagattttctaaattagacattgtctttaccttaaagaagaaaattgtctatttcagtgtcttttttagcaagattgaccaaaacaggtggtaggtgtgtaatttttaactgtcatgaaatactgtaatgcgcacctttgctaataaggaaatggtctccctttgaattatgggaagtttcttgtctgtgatatggggtgtctgtgtacatatatgtatatttccttttttaatacaggataataatatggggtcttgtccttcaccttttaagttcagggaacagtttgtcctgaccacacatatgttatcagtgtaatgctttatgaagctttagaaatgagctcatgactcattaaaaaataataaacgatgctattttaatattttcaaataaataatctgaggatgtgtttcatactttagcatcaacgctgagttgtgccttgtagaattgcattgtctatacatgcaaaagactattaagttaggatgaactagattccctaattacagtgaaattctatcttgcaaatgctatagaataacttgcattttaaagtgtatttgcacattttacatatgctatgtggttgcctttgggttttctgtacagattgtttttgttattaaatggaaaaggcctgaattatgctcttatgtgaagtaaattgatataacctattgactgtattctgtgtattattctttattttgggaccttctgtgtaaaagaaaatattacctaaattggttagatacaaagaaatcattaaaattattaatgtatatatgaaaattctgtttttcaatgacttttatgtgaggattgagaactaacttagtaaactaacactgaattctttgtggataagataatttatacatcttacctgtttatcagcctcagaattatacagtactgctgtgtgttctttatggacagatactcaaaggaatccgaatgggcatgttctatttctctggctcttgaccagtaattataaagtttaggtagacattttctgagccagcaagtagatcatagttgttaagcatctctatgacttacaccctggatatttgaaagcattttgtctcaccctgagaaatctataaggactctataattataaaacatgtcaatagagaattgacttctgagtccactgtcaactacatgcagaaaaacagaatgagtgtacttgattagtgccacagaagcaccatttagccactttcagagttgataaagaggcatacctacctgatggtgctgtatgttgcaagtgaagcaacacagtgcccattgttgacactaatgttattttaagtttgtgagttttcacaggtgcccttttctttcctactttcatcccttcatttgtatcctcctcttattttaatatggtatctttcttttttttgctagtccacatcacgtatttccattaaaacctaatgatgatgaaccatgtaacctcttgcaggaagaccacccaaactacccccaccctacttttgggtttctttagcagttaaattgctgctgctgctgtgttaagatttttctctggagcatgttctattgatcatgtttagatcatttagattgtaagttctgagagttacattttccccagcaattaatatagtgttgagtgcttttaggtacttagtaaagacttggggaaaaaaaaagggagttatatttttattttgatctacctcatggattatgtgagagacttataaaataggtaagtttataaagtggctttgttcttactggtctagtgaagttatgataaatttctgtctcggtgattgagaactacacaatcaaaaatgtattcaaactagctcaccctggcccaccaaaaccgatagtacatctttcccagctgcgagttcagtgacctcatactagtaatttaaagtctgctctgatgggaatatttataccatagaaaccagcaagagttcagttagccgtaaaaaatcaaggactgcctgtaacttaaaataggaagattaatactatttactgcatttatggaaataaaggagacaagttctttatagatgcataaaaagcaatacaattcagcacttgctttttttttaactgcacaaactaggaatagaagggaacttcttaatagaagaagttctacaaaaaaaacctagagccaacatatttaattgtgaatttttgaaaagcgtattcctccagagatcaggaaaaaggcaaaggtgcccactatcaccactttttctcaactttgtacagattctagccagtgcaagcaaaagaaatgaaaggcttacagataagaaataaaattgtcattcacagatgacatgattgtagaaaattgatataaacgtagaaataatgtgaatttaacaaggttgcaggatacaaagtcaaaattatcttagcaacaattagaaattgaaattatgagagtggtgtgtgcctatagtcccaactattggggaattgaagtgggaggatcacttgagcccaggagttcgaggctgcagtgagctattaccacaccactgcactccagcctgggtgagggaacgagaccctgtctcaaaaaaaaaaaaaaaaaaaaggaaaatactaattacaatagtatcagagagcatcaaatgcctcaaa"

	protein_translation_VPS4B = "MSSTSPNLQKAIDLASKAAQEDKAGNYEEALQLYQHAVQYFLHVVKYEAQGDKAKQSIRAKCTEYLDRAEKLKEYLKNKEKKAQKPVKEGQPSPADEKGNDSDGEGESDDPEKKKLQNQLQGAIVIERPNVKWSDVAGLEGAKEALKEAVILPIKFPHLFTGKRTPWRGILLFGPPGTGKSYLAKAVATEANNSTFFSISSSDLVSKWLGESEKLVKNLFQLARENKPSIIFIDEIDSLCGSRSENESEAARRIKTEFLVQMQGVGVDNDGILVLGATNIPWVLDSAIRRRFEKRIYIPLPEPHARAAMFKLHLGTTQNSLTEADFRELGRKTDGYSGADISIIVRDALMQPVRKVQSATHFKKVRGPSRADPNHLVDDLLTPCSPGDPGAIEMTWMDVPGDKLLEPVVSMSDMLRSLSNTKPTVNEHDLLKLKKFTEDFGQEG"

	product_VPS4B = "vacuolar protein sorting factor 4B"

	accession_VPS4B = "AF282904"

	map_VPS4B = "18q21-q22"

	VPS4B_dict = {
		"gene": "VPS4B",
		"prot": product_VPS4B,
		"acc": accession_VPS4B,
		"cds": cds_coordinates_VPS4B,
		"dna": origin_seq_VPS4B,
		"aa": protein_translation_VPS4B,
		"loc": map_VPS4B
	}

	restriction_sites = {}
	restriction_sites['EcoRI'] = [[1, 5], [8, 10]]
	restriction_sites['BamHI'] = [[13, 16]]
	VPS4B_dict["restriction_sites"] = restriction_sites

	entries = []

	entries.append(VPS4B_dict)

	return(entries)

def get_gene_list():

	return(['SCCA1', 'SMAD4', 'ME2'])

def get_protein_product_list():

	return(['U58b small nucleolar RNA', 'U58a small nucleolar RNA', 'Putative U58 small nucleolar RNA'])

def get_genbank_accession_list():

	return(['AB065574', 'AB065915', 'AF025886'])

def get_chromosomal_location_list():

	return(['18p11.2', '18q21.1', '18q21.2-q22'])