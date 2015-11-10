simply.title('Welcome')

setInterval(requestPhp, 1000);

function requestPhp(){
 ajax({ url: 'http://ec2-52-33-128-37.us-west-2.compute.amazonaws.com/currentState.txt' }, function(data){
  if(data == 1){
   simply.title('Unlock Door?');
  }
  else{
   simply.title('Waiting..');
  }
});
}

simply.on('singleClick', function(e) {
  if (e.button === 'up') {
    simply.title("Access Granted");
    ajax({ url: 'http://ec2-52-33-128-37.us-west-2.compute.amazonaws.com/changeDoorState.php?state=1' }, function(data){
    
    });
  }
  else if (e.button === 'down') {
    simply.title("Door Lock");
    ajax({ url: 'http://ec2-52-33-128-37.us-west-2.compute.amazonaws.com/changeDoorState.php?state=0' }, function(data){

    });

  }
});
