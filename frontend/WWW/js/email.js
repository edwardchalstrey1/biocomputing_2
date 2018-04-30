/* Javascript file to print email addresses 
Ref: http://www.bioinf.org.uk/teaching/bbk/biocomp2/js/page02.html*/


function printem(name, domainName, character)
			   {
			      var emAddress = name + "@" + domainName;
   
			      emAddress = emAddress.replace(RegExp(character, "g"), ".");
			      /* alert(emAddress); */
   
			      document.write("<span class='em'>");
			      document.write("<a href='mailto:" + emAddress +"'>" + emAddress + "</a>");
			      document.writeln("</span>");
			   }


			   printem("t.gore", "mail#cryst#bbk#uk", "#");