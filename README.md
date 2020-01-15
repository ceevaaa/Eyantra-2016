# [E-Yantra Robotics Competition 2016-17 from IIT-Bombay](https://www.e-yantra.org/)  
e-Yantra Robotics Competition (eYRC) is a unique annual competition for undergraduate students in science and engineering colleges. Selected teams are given a robotic kit complete with accessories and video tutorials to help them learn basic concepts in embedded systems and microcontroller programming. Our team was
1. [Ruturaj Shitole](https://github.com/rutu777)
2. [Anurag Pandey](https://github.com/asfd221)
3. [Shiva Pundir](https://github.com/ceevaaa)  

<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/Images/team%234227.jpg" width="400" >  

## [Rules](https://www.youtube.com/watch?v=CTPEDkKTA4E)  
The theme we got was Cross-a-Crater in which our bot's aim was to cross a crater from the given two choice of routes. Each route had potholes which had to be filled with the available cones given, but there were certain rules to be followed while filling the holes also. We also built a mechanical hand using metal-strips and Servo motors and programmed the servos to move in a specific sequence of rotation to pick up/drop the craters. We used Zigbee for communicating with our base bot which was Fire Bird V ATMEGA2560 on top of which the hand was built.  
<p float="left">
<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/Images/arena_complete.jpg" width="400" >
<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/Images/arena_vertical.jpg" width="400" >  
</p>  

The green part being the crater.  
The blue circles being the potholes.  
The small green cubes being the rocks which had to be avoided.  
The numbered cones with numbers on the top being the filling material.  
The black line is to be followed to reach specific points.  

## Build
The Hand was built using 3 [servo motors](https://www.robomart.com/servo-motors), attached to the [metal strips](https://rarecomponents.com/store/flat-rigid-metal-plates) with some springs which in turn was mounted on the FirebirdV.

<p float="left">
<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/Images/hand_detached.jpg" height="300" width="400" >  
<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/Images/firebird_on_fire.jpg" width="400" >
</p>  

## [Fire Bird V ATMEGA2560](http://www.nex-robotics.com/products/fire-bird-v-robots/fire-bird-v-atmega2560-robotic-research-platform.html)  
FIRE BIRD V will help you get acquainted with the world of robotics and embedded systems. Thanks to its innovative architecture and adoption of the ‘Open Source Philosophy’ in its software and hardware design, you will be able to create and contribute too, complex applications that run on this platform, helping you acquire expertise as you spend more time with them. Fire Bird V is designed by NEX Robotics and Embedded Real Time Systems lab, CSE IIT Bombay.  
A [2.4GHz ZigBee module](https://www.mouser.in/ProductDetail/DIGI/XB3-24Z8US-J?qs=sGAEpiMZZMtJacPDJcUJY8XgHoGMqQj39ZA2gobLK2F4M0waznlAtA%3D%3D) provide secure and multi-channel wireless communication up to a range of one kilometer line of sight.  

<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/Images/firebirdV.jpg" width="300" >  

## Pickup/Drop

<p float="left">
<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/pickup.gif" width="300" >  
<img src="https://github.com/ceevaaa/Eyantra-2016/blob/master/pushups.gif" width="300" >  
</p>

## Summary
Finally, after completion of everything we were still not able to completely cross the crater, as the bot diverged to the white part leaving the black line a number of times and hence creating a problem with the whole sequence of operations. It was a mistake from our side not to completely take care of the aberrant cases.
