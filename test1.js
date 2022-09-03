const fetch = require('node-fetch');

// var myHeaders = new Headers();
// myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
// myHeaders.append("Accept", '*');
// myHeaders.append("Access-Control-Request-Method", "POST");

var myHeaders = {"Content-Type": "application/x-www-form-urlencoded"};
var urlencoded = {
    "client_id": "b0c40e53-5c05-4737-86b4-02cb0b682c84",
    "client_secret": "02a123d5-7aba-4b3f-8d67-ef9ec0fd51ab",
    "grant_type": "password",
    "username": "thomasmuser@bestrun-apaco5.com",
    "password": "Police123",
    "credtype": "password"
  }
// var urlencoded = new URLSearchParams();
// urlencoded.append("client_id", "b0c40e53-5c05-4737-86b4-02cb0b682c84");
// urlencoded.append("client_secret", "02a123d5-7aba-4b3f-8d67-ef9ec0fd51ab");
// urlencoded.append("grant_type", "password");
// urlencoded.append("username", "thomasmuser@bestrun-apaco5.com");
// urlencoded.append("password", "Police123");
// urlencoded.append("credtype", "password");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: urlencoded
};

fetch("https://us.api.concursolutions.com/oauth2/v0/token", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error.message));