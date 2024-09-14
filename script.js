function sendEmail() {
  let contact = document.getElementById("contact_question").value;
  let name = document.getElementById("contact_name").value;
  let email = document.getElementById("contact_email").value; 

  if (contact != null && name != null && email != null && contact.trim() != "" && email.trim() != "" && name.trim() != "" ) {
    console.log("New recommendation added");
    showPopup(true);

    const url = process.env.NEXT_PUBLIC_LOCAL_HOST_URL  + "/sendemail"

    const encodedURL = encodeURI(`${url}`)
    
    fetch(encodedURL,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, email: email, contact: contact}),
    })
    
    // Reset the value of the textarea
    contact.value = "";
    name.value = "";
    email.value = "";
  }
}

function showPopup(bool) {
  if (bool) {
    document.getElementById('popup').style.visibility = 'visible'
  } else {
    document.getElementById('popup').style.visibility = 'hidden'
  }
}
