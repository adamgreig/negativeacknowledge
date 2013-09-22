Title: Robot3
Date: 2009-09-14 23:06
Author: admin
Category: ARM, Electronics, Robotics
Slug: robot3

I found an old RC car - the kind of thing you get for £5 from Argos -
lying in my cupboard, mostly untouched since I got it as a birthday
present. Still, it has wheels and motors, what more could you ask for?

[flickr pid="3921235172" size="medium"]

[flickr pid="3920452383" size="medium"]

[flickr pid="3920461549" size="medium"]

I proceeded to rip out all its electronics and battery contacts and
cover etc, leaving just the underchasis and two motors. I then put my
own little 900mAh lipo in the battery compartment along with a small
motor driver board (two h-bridges), with all the wires running through
the old contact holes. An [STM32 dev board][] went on top and connects
to a Sharp IR rangefinder and xbee radio.

[flickr pid="3920454819" size="medium"]

[flickr pid="3921243428" size="medium"]

All I had it do to start with was drive forwards, then when the ADC
detected the voltage from the Sharp sensor went over the limit that
indicated an obstacle was ahead, an interrupt fired which caused the car
to reverse back and to the left slightly. This was enough to avoid most
collisions so the car could pretty much drive about as it wanted. Later
I added remote control from a computer over the xbee, with the same
interrupt code for collisions. I was planning to put a GPS and some
other sensors on the car, but shortly after making it I ordered all the
parts for my upcoming quadcopter, which is going to take the limelight
for now.

<object width="425" height="344"><param name="movie" value="http://www.youtube.com/v/itKJRsRtrY8&amp;hl=en&amp;fs=1&amp;"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/itKJRsRtrY8&amp;hl=en&amp;fs=1&amp;" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344"></embed></object>

  [STM32 dev board]: http://negativeacknowledge.com/2009/09/stm32-prototyping-boards/
