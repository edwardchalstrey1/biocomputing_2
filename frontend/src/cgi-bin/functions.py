#!/usr/local/bin/python3


""" 
Programme:  Python Functions
File:       functions.py
            
Date:       12/04/18
Function:   Get Gene information for Chromosome 18 from index.cgi, process and display

Copyright:  (c) Trupti Gore, Birkbeck College, 2018
Author:     Trupti Gore
Address:    Msc Bioinformatics with Systems Biology (First Year)
            Department of Biological sciences
            Birkbeck,University of London
            London WC1E 7HX


Description:
------------

This programme is has functions which are used in query.py file.

-----------------------------------------------------------------------------------------------------------

"""



import re





def highlight_coding_seq(complete_dna,cds):
    """ This functions takes complete dna sequence and coding 
    region/restricted enzymes co-ordinates
    and adds delimeter at the start and end of coding region
    
    >>> highlight_coding_seq("ggatccaatccagaatcccatactgcatttagttgtcatcttcttagtctctacaatct", [[1, 3], [17, 19], [25, 27]])
    '[gga]tccaatccagaat[ccc]atact[gca]tttagttgtcatcttcttagtctctacaatct'
    
    
    """
    
    offset=0
    for c in cds:
        offset+=1
        start=c[0] + offset
        offset+=1
        end=c[1] + offset
        complete_dna=complete_dna[:start-2]+'['+complete_dna[start-2:]
        complete_dna=complete_dna[:end-1]+']'+complete_dna[end-1:]
    
    return(complete_dna)
 
def hilight(dna):
    """ This function replaces the delimeter by <mark> so it is rendered as highlighted
    region on the webpage 
    >>> hilite("abc[def]ghi[jkl]")
    'abc<mark class= \"highlight\">def</mark>ghi<mark class= \"highlight\">jkl</mark>'
    """
    
    high_dna=dna.replace("[","<mark class= \"highlight\">")
    high_dna=high_dna.replace("]","</mark>")
    #p=re.compile(r'[AGTC]')
    #high_dna=p.sub('-',high_dna)
    
    return(high_dna)

def hilight_res(dna):
    """ This functions replaces the delimeters with <mark highlight_res class> to 
    highlight the restriction enzymes
    >>> hilite("abc[def]ghi[jkl]")
    'abc<mark class= \"highlight_res\">def</mark>ghi<mark class= \"highlight_res\">jkl</mark>'
    """
    
    high_res_dna=dna.replace("[","<mark class= \"highlight_res\">")
    high_res_dna=high_res_dna.replace("]","</mark>")
    
    return(high_res_dna)

def highlight_res_site(complete_dna,res_site):
    """ This functions takes complete dna sequence and coding 
    region/restricted enzymes co-ordinates
    and adds delimeter at the start and end of coding region
    
    >>> highlight_coding_seq("ggatccaatccagaatcccatactgcatttagttgtcatcttcttagtctctacaatct", [[1, 3], [17, 19], [25, 27]])
    '[gga]tccaatccagaat[ccc]atact[gca]tttagttgtcatcttcttagtctctacaatct'
    
    
    """
    
    offset=0
    for res in res_site:
        offset+=1
        start=res[0] + offset
        offset+=1
        end=res[1] + offset
        complete_dna=complete_dna[:start-2]+'['+complete_dna[start-2:]
        complete_dna=complete_dna[:end-1]+']'+complete_dna[end-1:]
    
    return(complete_dna)
    

def check_res_enzyme(res_enzyme,cds,res_site):
    """  This function checks if the restriction enzyme cut sites are not within the coding region of the gene.
    From the coding region coordiantes (cds) it calculates the first coordinates of first pair and last
    coordiante of the last pair.  
    
    >>> check_res_enzyme('BamHI',[[8,10],[20,22]],{'BamHI': [[1, 6], [29,32]], 'EcoRI': [[3,7], [10, 15]], 'BsuMI': [[2, 6], [7, 9]]})
    'False'
    
    """
    resflag='False'
    codon_start= cds[0][0]
    codon_end= cds[-1][1]
    
    i=0
    for enzyme,coordinates in res_site.items():
   
        while res_enzyme ==enzyme and i < len(coordinates):
            if coordinates[i][1] < codon_start  or coordinates[i][1] > codon_end :
              
                i+=1
            else:
               
                i+=1
                resflag='True'
    return(resflag)        



######## Test Function ####

if __name__ == "__main__":
   import doctest
   doctest.testmod()