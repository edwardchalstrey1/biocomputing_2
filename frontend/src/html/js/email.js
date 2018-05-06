/* 

Programme:  jQuery Function
File:       email.js
            
Date:       22/04/18
Function:   Displays  the email address. It is hidden from the parsing software
Copyright:  (c) Trupti Gore, Birkbeck College, 2018
Author:     Trupti Gore
Address:    Msc Bioinformatics with Systems Biology (First Year)
            Department of Biological sciences
            Birkbeck,University of London
            London WC1E 7HX

Ref: http://www.bioinf.org.uk/teaching/bbk/biocomp2/js/page02.html*/


function printemail(name, domainName, character)
			   {
			      var emailAddress = name + "@" + domainName;
   
			      emailAddress = emailAddress.replace(RegExp(character, "g"), ".");
			      
   
			      document.write("<span class='em'>");
			      document.write("<a href='mailto:" + emailAddress +"'>" + emailAddress + "</a>");
			      document.writeln("</span>");
			   }


			   printemail("trupti_gore", "yahoo#com", "#");
			   document.write("</br>");
			   printemail("edwardchalstrey","gmail#com","#");
