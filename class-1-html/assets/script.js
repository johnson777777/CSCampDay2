document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("messageForm").addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const message = document.querySelector('textarea[name="message"]').value; // Get the textarea value
        alert(name + '說' + message);
    });
});