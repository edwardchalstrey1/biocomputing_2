/* Programme:  jquery

File:       jquery.js

Version:    V1 : Original
            
Date:       24/04/18

Function:   Highlights over and underused codons

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

document.ready()function is written which scans the table codon_freq and codon_chrom_freq. In the table column cell
if it satisfies the frequency criteria then based on the value it highlights the parent row.

-----------------------------------------------------------------------------------------------------------
Revision History:
-----------------
V7      24/04/18        Original    By: TG  
*/


$(document).ready(function(){
	$('#codon_freq tr.high_codon td:nth-child(3)').each(function(){  /* Ref: https://stackoverflow.com/questions/7656860/jquery-highlight-row-based-on-column-value?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa*/
		if ($(this).text() > 2.00){
			
			$(this).parent().css('background-color', '#33ccff');
			
		}
		
	
	
		else if ($(this).text() < 0.5){
			
			$(this).parent().css('background-color', '#ffd6cc');
		}
		
		});	
		
	$('#codon_chrom_freq tr.high_chrom_codon td:nth-child(3)').each(function(){
		if ($(this).text() > 2.00){
			
			$(this).parent().css('background-color', '#33ccff');
		}
		else if ($(this).text() < 0.5){
			
			$(this).parent().css('background-color', '#ffd6cc');
		}
		
		
		});		
		
		
	});
	
