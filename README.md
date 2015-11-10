# PebbleSesame
A remote control door unlocked from a Pebble Smart Watch

Youtube Video: https://youtu.be/uxB4fb8dUpM

So, whether you've done it, you do it often, or you'll do it in the future; Imagine yourself working on your programming assignment and you are just so concentrated. All your ideas are coming to your head when suddenly, your doorbell rings. Oh no, that means you have to get up, run to your door, at 'worst' case allow the person inside, run back to your room and hope that all your thought intact by the time you get to your chair. If not programming, then picture your favorite hobby being unfavorably interrupted. 

We've all been there; Pebble Sesame is here to help!

Pebble Sesame:
Once your doorbell is pushed, a webcam located in a safe place near your door takes a picture. The picture is then sent to the owner of the Pebble watch. The owner is then able to unlock and lock the door appropriately from their Pebble watch.

![alt tag](http://i.imgur.com/wh1R9xb.jpg)

How it Works

Raspberry Pi to Pebble Watch:
The button pushed calls fswebcam, which then takes a jpeg image and stores it in the current directory. The image is then converted, compressed, and resized to a png 144x168 gray scaled image to be displayed on the pebble watch. Once it’s converted, it is then uploaded to imgur and the URL of the image is stored in a text file in the current working directory. The URL and the watch notification signal are then sent to an AWS(Amazon Web Service) server that is the center of communication for the entire project. A python script on the server is called that downloads the image from imgur. The pebble watch is listening for a notification and once it hears it, the user is able to see the image taken. Also, it displays text for the user on the screen as part of the notification. 

Pebble Watch to Raspberry Pi:
Once the user receives the notification, Up button on the pebble sends a command to unlock the door, and Down button locks it. The signal sent from the pebble is '1' for unlock and '0' for lock. The signal is sent and stored in the AWS server. The Raspberry Pi is constantly listening for a change in state and once it hears it using UART(universal asynchronous receiver/transmitter), it sends the state data to an Arduino UNO. The arduino then interprets it and controls the servo motor(lock and unlock demo) appropriately.
