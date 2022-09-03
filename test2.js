var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://us.api.concursolutions.com/oauth2/v0/token',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded'},
  form: {
    'client_id': 'b0c40e53-5c05-4737-86b4-02cb0b682c84',
    'client_secret': '02a123d5-7aba-4b3f-8d67-ef9ec0fd51ab',
    'grant_type': 'password',
    'username': 'thomasmuser@bestrun-apaco5.com',
    'password': 'Police123',
    'credtype': 'password'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
