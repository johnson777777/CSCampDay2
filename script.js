document.getElementById("myForm").addEventListener('submit', function(event) {
    const fname = document.getElementById('fname').value;
    const lname = document.getElementById('lname').value;
    alert('First name: ' + fname + '\nLast name: ' + lname);
});