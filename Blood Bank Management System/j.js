


function formsubmit()
{
   
     var c=confirm("Are you sure you want to submit?");
    if(c)
    {
        var fname=document.form1.fnames.value;
        var lname=document.form1.lnames.value;
        var email=document.form1.Email.value;
        var pas=document.form1.pass.value;
        var mob=document.form1.number.value;
        
        var pas2=document.form1.pass2.value;
        var se=document.form1.sex.value;
        var ge;
        
         if(pas != "" && pas == pas2) {
      if(pas.length < 6) {
        alert("Error: Password must contain at least six characters!");
     
        return;
      }
         }
        var re = /[0-9]/;
      if(!re.test(pas)) {
        alert("Error: password must contain at least one number (0-9)!");
       return;
      }
      re = /[a-z]/;
      if(!re.test(pas)) {
        alert("Error: password must contain at least one lowercase letter (a-z)!");
        return;
      }
      re = /[A-Z]/;
      if(!re.test(pas)) {
        alert("Error: password must contain at least one uppercase letter (A-Z)!");
       return;
      }
        
        if(pas!=pas2)
    { document.form1.uspassword2.focus();
	alert("The passwords don't match!");
     return;
	
    }
         re = /[a-z]/i;
    if(!re.test(fname+lname)) {
      alert("Error: Username must contain only letters!");
      
      return;
    }
          re= /[0-9]/;
    if(!re.test(mob)) {
      alert("Error: should contain only numbers ");
      
      return;
    }

      if(se=="M"){
          ge="Mr.";
      }
        else{
            ge="Ms.";
        }
        
    var n=fname+" "+lname;
        var a=confirm("We sent SMS to +91 "+mob+" number."+"\n"+ "we sent an confirmation email to "+email+" Click OK if you recived.");
        if (a){
        alert("Hi,"+"\n"+ge+n+"\n"+"You are successfully registered ! Thanks for saving someone's life.");
        }
        else{
            alert("Please wait ....");
        }
        
        
    }
    
}
function changecol()
{ 
document.getElementById("if").style.backgroundColor='#424242';
 document.getElementById("if").style.color='#eceff1 ';
     document.getElementById("if").style.fontSize='40px';
   
}
function chn()
{ 
document.getElementById("if").style.backgroundColor='#424242';
 document.getElementById("if").style.color='#eceff1 ';
 document.getElementById("if").style.fontSize='35px';   
   
}

