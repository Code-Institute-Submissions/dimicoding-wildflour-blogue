function sendMail(contactForm) {
    emailjs.send("Dmytro M.", "template_n1n2xnb", {
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.emailaddress.value,
        "project_request": contactForm.projectsummary.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            document.getElementById("success-message").style.display = "block";
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
    }
