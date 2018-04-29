
/*  This function disbles  the submit button and rest of the dropdown lists based on the selection */
function disable(optid){
	document.getElementById("submit").disabled=false;
	switch(optid){
		case "protid":
			document.getElementById("locid").disabled=true;
			document.getElementById("accid").disabled=true;
			document.getElementById("geneid").disabled=true;
			
			break;
		case "locid":
			document.getElementById("protid").disabled=true;
			document.getElementById("accid").disabled=true;
			document.getElementById("geneid").disabled=true;
			document.getElementById("submit").enabled=true;
			break;
		case "geneid":
			document.getElementById("locid").disabled=true;
			document.getElementById("accid").disabled=true;
			document.getElementById("protid").disabled=true;
			document.getElementById("submit").enabled=true;
			break;
		case "accid":
			document.getElementById("locid").disabled=true;
			document.getElementById("protid").disabled=true;
			document.getElementById("geneid").disabled=true;
			document.getElementById("submit").enabled=true;
			break;
}
}
/* This function enables  the submit button and rest of the dropdown lists based on the selection */	
function enable(){

			document.getElementById("locid").disabled=false;
			document.getElementById("accid").disabled=false;
			document.getElementById("geneid").disabled=false;
			document.getElementById("protid").disabled=false;
			document.getElementById("submit").disabled=true;
			
			
}

/*function showElement(element)
{
   document.getElementById(element).style.display = 'block';
}
function hideElement(element)
{
   document.getElementById(element).style.display = 'none';
}

function toggleElement(element)
{
   if(document.getElementById(element).style.display == 'none')
   {
      showElement(element);
   }
   else
   {
	   hideElement(element);
   }
}*/

/* After loading the index.html page , this function directs it to the index.py */   
function loadIndex() {
    document.location = "/frontend/src/cgi-bin/index.py";
}



/* Accordion : https://www.w3schools.com/howto/howto_js_accordion.asp*/

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}


/*Hide email : */

function printem(name, domainName, character)
{
   var emAddress = name + "@" + domainName;
   
   emAddress = emAddress.replace(RegExp(character, "g"), ".");
   /* alert(emAddress); */
   
   document.write("<span class='em'>");
   document.write("<a href='mailto:" + emAddress +"'>" + emAddress + "</a>");
   document.writeln("</span>");
}



	


                      

	
	
	
	
	

    