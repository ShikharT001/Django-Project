document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    if (username && email && password) {
      alert(`Welcome, ${username}! You have successfully registered.`);
      this.reset(); // Reset form fields
    } else {
      alert('Please fill in all the fields.');
    }
  });
  