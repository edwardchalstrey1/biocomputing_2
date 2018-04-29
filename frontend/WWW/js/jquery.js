/* Programme:  jquery

File:       jquery.js

Version:    V1
            
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
V1      24/04/18        Original    By: TG  
*/

/* document.ready() call which will read the table id, scan through each column of the table and if the given value is found it will highlight the parent row*/
$(document).ready(function(){
	var freqArray = new Array();
	var freqChromArray=new Array();
	
	$('#codon_freq tr.high_codon td:nth-child(3)').each(function(){  /* Ref: https://stackoverflow.com/questions/7656860/jquery-highlight-row-based-on-column-value?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa*/
		freqArray.push($(this).text());
		
	});
	
		highfreqcodon=findMaxVal(freqArray) /* To find highest 3 and loweset 3 codon frequencies.*/
	    lowfreqcodon=findMinVal(freqArray)
	
	$('#codon_freq tr.high_codon td:nth-child(3)').each(function(){
		
		for(j=0;j<highfreqcodon.length;j++){
			if ($(this).text() == highfreqcodon[j]){
			
				$(this).parent().css('background-color', '#33ccff');
			
		}
		
		}
		
	
		for(j=0;j<lowfreqcodon.length;j++){
		if ($(this).text() == lowfreqcodon[j]){
			
			$(this).parent().css('background-color', '#ffd6cc');
		}
	}
		
		});	
		
	$('#codon_chrom_freq tr.high_chrom_codon td:nth-child(3)').each(function(){
		freqChromArray.push($(this).text());
	});
		highfreqcodon=findMaxVal(freqChromArray) /* To find highest 3 and loweset 3 codon frequencies.*/
	    lowfreqcodon=findMinVal(freqChromArray)
	
	$('#codon_chrom_freq tr.high_chrom_codon td:nth-child(3)').each(function(){
		for(j=0;j<highfreqcodon.length;j++){
			
			if ($(this).text() == highfreqcodon[j]){
			
			$(this).parent().css('background-color', '#33ccff');
		}
	}
		for(j=0;j<lowfreqcodon.length;j++){
			if ($(this).text() == lowfreqcodon[j]){
			
			$(this).parent().css('background-color', '#ffd6cc');
		}
	}
		
		
		});		
		
		
	})
/* Function to find the maximum value from the frequency array*/	
	function findMaxVal(freqArray1){
		
		var highfreqcodon=new Array();
		
		
		for(i=0;i<3;i++){	
			maxval=Math.max.apply(Math,freqArray1);
			highfreqcodon.push(maxval);
			maxval=maxval.toString();
			
			const maxIndex=freqArray1.indexOf(maxval);
			freqArray1 = freqArray1.filter(function(condition) { /* To remove multiple occurances of the number*/
			    return condition !== maxval;
			});
		
	}
		
		return(highfreqcodon)
}
/* Function to find mimimum value from the frequency array*/	
	function findMinVal(freqArray1){
		
		var lowfreqcodon=new Array();
		
		for(i=0;i<3;i++){	
		
		minval=Math.min.apply(Math,freqArray1);/*.filter(number=> number!=0));	/*To exclude 0*/
		lowfreqcodon.push(minval)
		minval=minval.toString();
		
		const minIndex=freqArray1.indexOf(minval)
		freqArray1 = freqArray1.filter(function(condition) { /* To remove multiple occurances of the number*/
		    return condition !== minval && condition!=0.0;
		});
		
		
		
	}
	
	return(lowfreqcodon)
}
	
	