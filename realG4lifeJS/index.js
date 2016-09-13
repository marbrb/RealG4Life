'use strict';

var http = require('http');
var server = http.createServer().listen(8085);
var io = require('socket.io').listen(server);

io.sockets.on('connection', function(socket) {
  console.log('Client connected');

  socket.on('message', function(chanel, message){
    //TODO: Implement RabbitMQ functionnality
  });

  socket.on('send_message', function(message) {
    console.log('Client >', message);
  });

});

console.log('Server running at http://localhost:8085');
