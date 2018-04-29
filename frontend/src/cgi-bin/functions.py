#!/usr/local/bin/python3


""" 
Programme:  Python Functions
File:       functions.py

Version:    V1 Original
            
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

This programme is has functions which are used in query.py file.

-----------------------------------------------------------------------------------------------------------
Revision History:
-----------------
V7      12/04/18        Original    By: TG  Previous versions are not tracked.
V7.1    28/04/18        Added 

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
def highlight_original(dna):
    """ This function is written to keep the alignment same for both ,highighted dna and original dna in the browsers . As in the highlight(dna),it replaces the delimeter by 
    <span> so it is rendered as highlighted region on the webpage. Here while highlighting, the background color is kept white
    >>> hilite("abc[def]ghi[jkl]")
    'abc<span class= \"highlight\">def</span>ghi<span class= \"highlight\">jkl</span>'
    """
    
    high_dna=dna.replace("[","<span class= \"highlight-original\">")
    high_dna=high_dna.replace("]","</span>")
    #p=re.compile(r'[AGTC]')
    #high_dna=p.sub('-',high_dna)
    
    return(high_dna)    
def hilight(dna):
    """ This function replaces the delimeter by <span> so it is rendered as highlighted
    region on the webpage 
    >>> hilite("abc[def]ghi[jkl]")
    'abc<span class= \"highlight\">def</span>ghi<span class= \"highlight\">jkl</span>'
    """
    
    high_dna=dna.replace("[","<span class= \"highlight\">")
    high_dna=high_dna.replace("]","</span>")
    #p=re.compile(r'[AGTC]')
    #high_dna=p.sub('-',high_dna)
    
    return(high_dna)

def hilight_res(dna):
    """ This functions replaces the delimeters with <span highlight_res class> to 
    highlight the restriction enzymes
    >>> hilite("abc[def]ghi[jkl]")
    'abc<span class= \"highlight\">def</span>ghi<span class= \"highlight\">jkl</span>'
    """
    
    high_res_dna=dna.replace("[","<span class= \"highlight_res\">")
    high_res_dna=high_res_dna.replace("]","</span>")
    
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

def hilite_dash(dna):
    high_res_dna=dna.replace("1","<span class= \"highlight_res\">")
    high_res_dna=high_res_dna.replace("2","</span>")
    return(high_res_dna)   
  
#p=re.compile(r'[a-zA-Z]')
#match=p.sub('-','fdfdfdf[fdfdfdf]fdfdfdfdf')
#print(match)
#print(check_res_enzyme('BsuMI',[[8,10],[20,22]],{'BamHI': [[1, 6], [29,32]], 'EcoRI': [[3,7], [10, 15]], 'BsuMI': [[2, 6], [7, 9]]})) 
######## Test Function ####

if __name__ == "__main__":
   import doctest
   doctest.testmod()