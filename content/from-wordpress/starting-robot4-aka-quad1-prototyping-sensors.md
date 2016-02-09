Title: Starting Robot4 aka Quad1: Prototyping Sensors
Date: 2009-09-26 16:56
Author: Adam Greig
Tags: Electronics, Robotics
Slug: starting-robot4-aka-quad1-prototyping-sensors

As briefly mentioned in my last post, my next project is an autonomous
quadcopter. That is, a four-rotored flying robot.

<a href="http://www.flickr.com/photos/randomskk/3946272514/" title="Robot4 aka Quad1 - First Prototyping"><img src="https://farm3.staticflickr.com/2439/3946272514_9be22a9a23.jpg" alt="Robot4 aka Quad1 - First Prototyping" /></a>

After a couple of weeks of waiting around, I've got all the parts I've
ordered so far: a basic aluminium chasis from MikroKopter, four
1040Kv/14A brushless motors, four propellers, some 3000mAh 3S lipo
batteries, and a whole suite of sensors on breakouts from SparkFun,
including an accelerometer, gyroscopes, barometer, magnetometer and GPS.
I've also got spares of a few parts and a second set of accelerometers
and gyroscopes to compare with.

<a href="http://www.flickr.com/photos/randomskk/3946282126/" title="Robot4 aka Quad1 - First Prototyping"><img src="https://farm4.staticflickr.com/3487/3946282126_0b8e46bb4a.jpg" alt="Robot4 aka Quad1 - First Prototyping" /></a>

I also bought four normal brushless motor controllers, which take a PWM
input and control the motor. They're fine for prototyping with, but I
plan to make my own motor controllers that will take throttle values at
a much higher rate over I²C, as well as being capable of reporting
information (voltage, current, rpm) back to the main controller.
However, I've not bought the parts for the motor controllers yet, so for
now I'm using the pre-made ones.

To start with, I'm writing code to read all the sensors and check their
results. This also means I can plug the sensor values into a simulation
on my computer to test filters and control code, rather than having to
run it on the quad every time I need to change a parameter. All the code
is on GitHub: http://github.com/randomskk/Robot4 and so far I've written
code for the accelerometer (SCA3000) and the barometer (SCP1000). The
accelerometer values are read into memory the whole time over DMA, while
the barometer is polled when required as its update rate is about 2Hz so
there's no point wasting a DMA channel. The next thing to do will be the
gyroscopes.

I'll post updates here as the robot progresses...
