Title: NIXIEs and Accelerometers
Date: 2009-02-16 02:50
Author: Adam Greig
Tags: Arduino, Electronics
Slug: nixies-and-accelerometers

![Four Nixies](http://farm4.static.flickr.com/3424/3258599547_bc1cab87ca.jpg)

It's been a while since I've posted anything, so I'll drop a quick
update. Hopefully by the end of the coming week I'll have finished on my
current great big time-consuming project and will be able to write that
up.

I've been playing with a few things besides that project, though. The
first is stress testing my small and somewhat dodgy [NIXIE PSU](http://negativeacknowledge.com/2008/09/nixie-tubes-lit-up-at-last/), which
amazingly has managed to drive eight tubes:

![8 nixies: getting dangerous](http://farm4.static.flickr.com/3567/3279522143_79c282a60d.jpg)

I plan to finish off designing a
somewhat more powerful power supply so I don't worry about it exploding
in my face every time I try using it. A better way to control it than a
plain RTC would be nice too - I'm thinking of using a GPS module.

(p.s. yea, I accidentally set the 8 on instead of the 9 and didn't
realise -- oops!)

The other thing I've recently been playing with is an accelerometer I
got for Christmas. It's the [LIS302DL](http://www.sparkfun.com/commerce/product_info.php?products_id=8658) from Sparkfun, a super cheap
3-axis accelerometer that can output on SPI or I²C, has interrupts for
freefall and things like the user tapping it or double tapping it, and
adjustable sensitivity - 2g or 8g. All that for $20 on a breakout board
is pretty incredible!

I hooked it up to an Arduino and after some messing around, was able to
get it to read the acceleration data from the sensor over I²C, and then
send it to the PC with a timestamp over serial (itself over USB). Then I
whipped up a quick Python script to plot the data and decided I'd test
something that's now been thoroughly battered into me: in simple
harmonic motion, the acceleration on a particle is proportional to its
displacement, which can be shown to mean it is a sine wave. I figured
that's as good a way as any to test the sensor, and so I took the
Arduino and swung it as a pendulum from its USB cable.  
I then had Python generate the magnitude of the acceleration - the
single value showing the resultant acceleration on all three axis. This
was plotted against the millisecond value from the arduino and hey
presto - a (nearly) perfect sine wave!

![Simple Harmonic Motion](|filename|/images/from-wordpress/shm.png)
![Simple Harmonic Motion Zoomed In](|filename|/images/from-wordpress/shm2.png)

Not bad! The accelerometer itself:

![Arduino + LIS302DL Accelerometer](http://farm4.static.flickr.com/3291/3283553082_7159ddbc4e.jpg)

(p.s. be sure to view the full sized image for tons of lovely macro
sharpness)

For bonus points: Given that the Arduino was on the Earth's surface, and
that the millisecond data is accurate, how long was the USB cable the
Arduino was swinging from?
