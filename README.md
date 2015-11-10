# PebbleSesame
A remote control door unlocked from a Pebble Smart Watch

A button is pushed that simulates a doorbell. A webcam then takes a picture. The picture is sent and recieved on the pebble watch. The owner is then able to lock and unlock the door from their Pebble watch.

![alt tag](http://i.imgur.com/wh1R9xb.jpg)

How it Works:
The button pushed calls fswebcam which then takes a jpeg image and stores it in the current directory. The image is then converted, compressed, and resized to a png 144x168 grayscaled image to be displayed on the pebble watch. Once its done being converted, it is then uploaded to imgur and the url of the image is then stored in a text file in the current working directory. The url and the watch notfication signal is then sent to an AWS(Amazon Web Service) server that is the center of communication for the entire project. A python script on the server is called that downloads the image from imgur. The pebble watch is listening for a notification and once it hears it, the user is able to see the image taken. Also, it displays text for the user on the screen as part of the notification. The user is then able to unlock the door from the pebble watch and lock it when appropriate.
