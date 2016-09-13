var socket_server = '10.20.232.45';
var socket_port = 8085;

var socket = io.connect(socket_server, {port: socket_port});

socket.on('connect', function() {
  console.log('connected');
})

socket.on('message', function(message) {
  console.log('Got a new message');

  $('çomments').append('<li>' + data '</data>');
  $('comment').focus();
})

var sendMessage = function(event) {

  if(event.keyCode != 13)
    return;

  var msg = $('#comment').attr('value');

  if(msg) {

    socket.emit('send_message', msg, function(data){
      console.log(data);
    });

    $('comment').attr('vlue', ' ');
  }
}
