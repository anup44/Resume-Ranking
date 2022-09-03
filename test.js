var jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;
var $ = jQuery = require('jquery')(window);
process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;

var settings = {
    "url": "https://us.api.concursolutions.com/oauth2/v0/token",
    "method": "POST",
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded",
      //"Access-Control-Allow-Origin" : "*",
      //"x-csrf-token": 'fetch',
      //"Cookie": "_abck=8C091B07D32410433264B725D252637A~-1~YAAQ5gVaaER5a3Z4AQAAyBz8tAUcic83oKwc91SXxMd+Sgo5QqacSgovaRiSUG6KAeeKUjF1PYzfT8tOs3QjDJDCHFcuswnffuFnqMBoGAooUOx8J/VTh85c0Z938nIUqBaqMzMrRPmHe+yyMZFn8gDDLgM8DNqhNHUxt5A18do9EDWGkFsP3hVoeIsO0jcKV0p7KqBCswVYtsvb1hHoPUy7u1JLhnd5jLc8ZFax7Rka43uCbaIe+3SWdBWw/6lKNQOgU1RBXpZrlr1JUeDvJSQZEoZIjNKPtMcDGN+6Xyt6w3BzqPdUOjSifh+B+5ZDkrfQ7VmBPgiPfGBWigdyjX5Ym+UMTtccxLmJJxHSGa0uaxqGkMXjXzo5JkQyaIlcR7w=~-1~-1~-1; ak_bmsc=169A84807FDD464C64553605385A0B5DB856FA958D0900007BF7736084E2A922~plEIj/DVn5A+VtdP37Z+3RtJPdqMejXg6rEUL/uuXWjgEA4eJ3MIJvPVR+Nnk8dzKXl8MNT7sWHbI2OIxD+PX2c6bEPyOTDvmkZkI0VEwNmv/+XeAQ2Zt9NUb+bzLdGf08x3nL5P/J/HgvLfjmH/2Nu/W6df4mOVnDIuORHT2xw6D6vde3oKLi1qOG6OEriTGYuXa0fOg3oGjQZ5Cic5Z2hT1WKxZ2qqYh6fhcGvTnnqdIFbMNKFJMPrpv81pnVJqT"
    },
    //"rejectUnauthorized": false,
    
    "data": {
      "client_id": "b0c40e53-5c05-4737-86b4-02cb0b682c84",
      "client_secret": "02a123d5-7aba-4b3f-8d67-ef9ec0fd51ab",
      "grant_type": "password",
      "username": "thomasmuser@bestrun-apaco5.com",
      "password": "Police123",
      "credtype": "password"
    }
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });