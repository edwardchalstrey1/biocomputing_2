/* Programme:  jquery

File:       jquery.js
            
Date:       24/04/18

Function:   Highlights over and underused codons

Copyright:  (c) Trupti Gore, Birkbeck College, 2018
Author:     Trupti Gore
Address:    Msc Bioinformatics with Systems Biology (First Year)
            Department of Biological sciences
            Birkbeck,University of London
            London WC1E 7HX


Description:
------------

document.ready()function is written which scans the table codon_freq and codon_chrom_freq. In the table column cell
if it satisfies the frequency criteria then based on the value it highlights the parent row.

-----------------------------------------------------------------------------------------------------------

*/

/* document.ready() call which will read the table id, scan through each column of the table and if the given value is found it will highlight the parent row*/
$(document).ready(function(){
	
	
	$('#codon_chrom_freq tr.high_chrom_codon td:nth-child(3)').each(function(){  /* Ref: https://stackoverflow.com/questions/7656860/jquery-highlight-row-based-on-column-value?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa*/
		var chromCodonFreq=$(this).text() /* freq from chrom table*/
		
		var over=$(this).parent().text().substring(0,3);/* codon */
		
		$('#codon_freq tr.high_codon td:nth-child(1)').each(function(){
			var geneCodonFreq=$(this).parent().text().substring(4,8)
			
			if($(this).text()==over &&  geneCodonFreq > (150 * chromCodonFreq)/100){  /* Overused codons if more than 150% of the corresponding codon in the entire chromosome*/
				
				$(this).parent().css('background-color', '#33ccff');
			}
			if($(this).text()==over &&  geneCodonFreq < (50 * chromCodonFreq)/100){  /* Underused codons if less than 50% of the corresponding codon in the entire chromosome*/
				
				$(this).parent().css('background-color', '#85929E');
			}
			
		})
			
				
		
	
		

		
		});	/* Codon table ends*/
		

		
		/* Finding rare codons. The criterion is if the said codon has very low frequence (0.50) in the entire chromosome , then it is a rare codon.
		If these rare codons with frequency more than that of in the chromosome tabble , are found in the given gene on the chromosome then 
		it might be an interesting informatio for the user.*/
		$('#codon_chrom_freq tr.high_chrom_codon td:nth-child(3)').each(function(){
			
			
				if ($(this).text() < 0.50){ 
					
					var rare_codon_freq=$(this).text();
					var rare =  $(this).parent().text().substring(0,3); /* extracting the codon from the string*/
					
				}
				$('#codon_freq tr.high_codon td:nth-child(1)').each(function(){	
					if($(this).text()==rare && $(this).parent().text().substring(4,8) > rare_codon_freq && $(this).parent().text().substring(4,8) != 0.0){
						
				$(this).parent().css('background-color', '#cb4335');
			}
		
		})
		
		
			});	/* Rare codon calculation end*/	
		
		
	})/* main functio ends*/

	
	