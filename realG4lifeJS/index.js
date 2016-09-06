'use strict';

var http = require('http');

var server = http.createServer(function(req, res) {
  res.end('Hello world')
});

server.listen(8085, function() {
  console.log('Server running at http://localhost:8085');
})
