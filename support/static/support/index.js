function getCookie(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`)
    if (parts.length == 2) return parts.pop().split(';').shift(); 
}

function message(id, event){
    
    event.preventDefault();

    console.log("id",id);
    const content = document.querySelector('#content').firstChild.value;
    console.log(content)

    if (!content) return console.log({'Error': "Can't send blank message"});
   
    fetch(`/message_csr/${id}`,{
        method: 'POST',
        body: JSON.stringify({message: content}),
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(request => request.json())
    .then(data => console.log(data))
    .then(() => location.reload())
    .catch(error => console.log(error));

}

function save_changes(){
    alert('Changes saved clicked');
}