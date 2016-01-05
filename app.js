var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.type('text/plain');
  res.send("I am a train!")
});

app.listen(process.env.PORT || 4200)
