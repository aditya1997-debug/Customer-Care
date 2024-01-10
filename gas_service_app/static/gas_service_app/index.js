document.querySelector('#myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    const formData = new FormData(event.currentTarget);
 
    
    fetch('/submit_request', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response = response.json())
    .then(data => {
        if (data.success) {
            // Handle success here, e.g., display a success message on the page.
            console.log("Success: Your complaint has been registered successfully.");
        } else {
            // Handle any other response or error here.
            console.log("Error: Something went wrong.");
        }
    })
    .catch(error => {
        console.error("Error: Something went wrong.", error);
    });
    


});


function getCookie(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`)
    if (parts.length == 2) return parts.pop().split(';').shift(); 
}

function resolved_requests(event){
    event.preventDefault();
    //console.log("resolved")
    window.location.assign("/resolved_requests");
}

function submitted_requests(event){
    event.preventDefault();
    //console.log("resolved")
    window.location.assign("/submitted_requests");
}

function view_request(id){
    window.location.assign(`/view_request/${id}`);
}

function message(id, event){
    
    event.preventDefault();

    //console.log("id",id);
    const content = document.querySelector('#content').firstChild.value

    if (content == '') return console.log({'Error': "Can't send blank message"});
   
    fetch(`/message_csr/${id}`,{
        method: 'POST',
        body: JSON.stringify({message: content}),
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(request => request.json())
    .then(() => location.reload())
    .catch(error => console.log(error));

    
}

