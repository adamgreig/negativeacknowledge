Title: Final Lightbar Controller
Date: 2008-06-11 16:52
Author: Adam Greig
Tags: AVR, Electronics, Robotics
Slug: final-lightbar-controller

I've finished the lightbar controller!

![Lightbar Visualiser](https://static.flickr.com/3041/2570139325_288bd6e6ef.jpg)

This device analyses the music it picks up via the electret microphone,
then flashes the LEDs in time to the music. It's encased in the box
SparkFun sent me the microphones in, since the box was just begging to
be used as a case for something! I'm sure that was intentionally
designed.

![Lightbar Visualiser](https://static.flickr.com/3106/2570965162_1b8a6009d1.jpg)

Getting a bit more technical:

The microphone picks up the noise and sends this to the LM386 amp, which
amplifies it about 200x before it's read by the ATtiny13's ADC at 8-bit
resolution. The ATtiny13 then keeps a running average of the noise
level, and flashes the LEDs if the current volume exceeds the average by
a scalar amount.

![Lightbar Visualiser](https://static.flickr.com/3262/2570962450_c3d00cc974.jpg)

As a result, the LEDs flash on when the music hits a peak, and are off
otherwise - no matter what volume.  
The brightness of the LEDs is also somewhat correlated to the loudness
of the peak, since a louder peak will generally keep the LEDs on for
longer.

Check out the video of it in action:

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="425" height="344" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="src" value="https://www.youtube.com/v/6ihIaNN9UBY&amp;hl=en"></param><embed type="application/x-shockwave-flash" width="425" height="344" src="https://www.youtube.com/v/6ihIaNN9UBY&amp;hl=en"></embed></object>

Download the schematic, PCB layout, code:  
[https://randomskk.net/projects/lightstrip/][] (all files released
under Creative Commons BY-SA-NC 3.0).[  
][https://randomskk.net/projects/lightstrip/]

  [https://randomskk.net/projects/lightstrip/]: https://randomskk.net/projects/lightstrip/
