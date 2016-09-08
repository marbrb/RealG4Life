var socket = io.connect('localhost', {port: 8085});

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
