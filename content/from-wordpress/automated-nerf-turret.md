Title: Automated NERF turret
Date: 2010-06-18 16:35
Author: Adam Greig
Tags: Arduino, Electronics
Slug: automated-nerf-turret

![Automatic NERF EBF-25 Turret](https://farm5.static.flickr.com/4019/4711476211_5334eb34fe.jpg)

So, exams are finally over and I've had time to get playing with
something again. Some friends bought me a NERF Vulcan for my birthday
(cheers!) and of course I had to mod it up. The gun itself is now
running off a 3-cell lipo pack, which about doubles the rate of fire,
and has three ammo belts chained together to give 74 rounds in one
continuous burst of fire.

![Automatic NERF EBF-25 Turret](https://farm5.static.flickr.com/4011/4712116676_347aac154d.jpg)

I then hooked up an Arduino and servo motor to a series of cabletied
pencils, which can pull the trigger on command. The Arduino and a USB
webcam then connect to a laptop which is running motion and a small
python script which interfaces to the Arduino and plays sound clips from
Portal turrets when motion is detected/no longer detected.

![Automatic NERF EBF-25 Turret](https://farm2.static.flickr.com/1275/4711478303_9c9dd1bc7b.jpg)

The whole thing works very nicely, shooting down anyone who walks into
my room with a rapid burst of darts, and terrifying them with the portal
turret sounds.

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="480" height="385" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><param name="src" value="http://www.youtube-nocookie.com/v/wrWUhVeEcHk&amp;hl=en_GB&amp;fs=1&amp;rel=0"></param><param name="allowfullscreen" value="true"></param><embed type="application/x-shockwave-flash" width="480" height="385" src="http://www.youtube-nocookie.com/v/wrWUhVeEcHk&amp;hl=en_GB&amp;fs=1&amp;rel=0" allowscriptaccess="always" allowfullscreen="true"></embed></object>

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="480" height="385" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><param name="src" value="http://www.youtube-nocookie.com/v/-FBXKrU1Jec&amp;hl=en_GB&amp;fs=1&amp;rel=0"></param><param name="allowfullscreen" value="true"></param><embed type="application/x-shockwave-flash" width="480" height="385" src="http://www.youtube-nocookie.com/v/-FBXKrU1Jec&amp;hl=en_GB&amp;fs=1&amp;rel=0" allowscriptaccess="always" allowfullscreen="true"></embed></object>

Check out
[flickr](http://www.flickr.com/photos/randomskk/sets/72157624178093055/) for
more photos!

I modified Principia Lab's servo code from
[here](http://principialabs.com/arduino-serial-servo-control/) and
[motion](http://www.lavrsen.dk/twiki/bin/view/Motion/WebHome) and
Portal turret sounds from Valve's
[Portal](http://orange.half-life2.com/portal.html) and the code below for
controlling motion and the arduino and playing the sound files:

<p>
<script src="http://gist.github.com/443851.js"></script>
</p>
