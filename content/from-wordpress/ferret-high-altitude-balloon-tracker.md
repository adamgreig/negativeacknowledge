Title: Ferret: High Altitude Balloon Tracker
Date: 2010-03-17 21:38
Author: Adam Greig
Tags: Arduino, Electronics, HAB
Slug: ferret-high-altitude-balloon-tracker

<a href="http://www.flickr.com/photos/randomskk/4414040518/" title="Ferret 1 insides"><img src="http://farm3.staticflickr.com/2725/4414040518_16f001f3ae.jpg" alt="Ferret 1 insides" /></a>

I'm part of [CU Spaceflight][], and since we have clearance to launch
high altitude balloons from a few nearby locations we often do launches
for other people. A lot of the time these launches have a radio
transmitter on board, so that people around the country can [pick up its
GPS position and help keep track][] of the balloon's location. We were
helping with a launch a few weeks back which didn't have a radio
transmitter, but instead planned to rely on a GSM based system to text
the GPS coordinates back. [Jon Sowman][] and I decided to whip up a
small radio tracker based on some work that had previously been done by
Iain Waugh at CUSF. Six hours later, we'd completed Ferret 1!

<a href="http://www.flickr.com/photos/randomskk/4414039650/" title="Ferret 1 before boxing"><img src="http://farm3.staticflickr.com/2749/4414039650_e30c16dcf1.jpg" alt="Ferret 1 before boxing" /></a>

It consists of an Arduino with some stripboard stuck on top. The strips
on the stripboard were cut down the middle with a dremel, then we
soldered some pin headers on to mate with the power and lower digital
pins on the arduino. We didn't need any of the higher digital pins, so
the alignment issue wasn't a problem. We then stuck an EM-406a GPS unit
and a [Radiometrix NTX2][] on top along with a few required resistors
and capacitors. The radio requires an antenna, which we constructed out
of some mini coax soldered to the stripboard, a small square of copper
clad board with a hole drilled through and five 17cm long bits of single
core wire. Four of the wires were soldered onto the corners of the
copper clad board sticking outwards, while the fifth was soldered to the
centre conductor of the coax. This results in a quarter-wave antenna
with a ground plane, which is great because almost all the radiation
goes downwards in a fairly nice pattern.

Antenna done, we hacked up Iain's code and flashed that onto the arduino
and gave the whole system a quick test with a radio lying around the
lab:

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="400" height="225" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="data" value="http://www.flickr.com/apps/video/stewart.swf?v=71377"></param><param name="flashvars" value="intl_lang=en-us&amp;photo_secret=08fe2449a9&amp;photo_id=4414453230&amp;flickr_show_info_box=true&amp;hd_default=false"></param><param name="bgcolor" value="#000000"></param><param name="allowFullScreen" value="true"></param><param name="src" value="http://www.flickr.com/apps/video/stewart.swf?v=71377"></param><param name="allowfullscreen" value="true"></param><embed type="application/x-shockwave-flash" width="400" height="225" src="http://www.flickr.com/apps/video/stewart.swf?v=71377" allowfullscreen="true" bgcolor="#000000" flashvars="intl_lang=en-us&amp;photo_secret=08fe2449a9&amp;photo_id=4414453230&amp;flickr_show_info_box=true&amp;hd_default=false" data="http://www.flickr.com/apps/video/stewart.swf?v=71377"></embed></object>

This was successful, so we put the whole thing in a box, taped it down
and were ready to go!

<a href="http://www.flickr.com/photos/randomskk/4413279333/" title="Ferret 1 almost ready to fly"><img src="http://farm5.staticflickr.com/4011/4413279333_40b8397eb8.jpg" alt="Ferret 1 almost ready to fly" /></a>

We duct taped it to the main payload and launched it the next morning.

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="480" height="360" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true"></param><param name="allowScriptAccess" value="always"></param><param name="src" value="http://www.dailymotion.com/swf/video/xchspy"></param><param name="allowfullscreen" value="true"></param><embed type="application/x-shockwave-flash" width="480" height="360" src="http://www.dailymotion.com/swf/video/xchspy" allowscriptaccess="always" allowfullscreen="true"></embed></object>  
**[UKHAS Church Hill Site Project Orion][]**  
*Uploaded by [kannasnakka][]. - [More video blogs and vloggers.][]*

The first launch attempt didn't go so well, with too little helium
resulting in us almost taking out some football players. Luckily we were
able to grab the balloon and refill, getting a successful second launch.
The video above is from Scott James, whose flight we were piggybacking
on. He had an actual video and still camera onboard.

Sadly, shortly after crossing the meridian the GPS lost lock and for a
while we didn't get any new data. Eventually, the data picked up again
-- but with a suddenly discovered bug in the code! We were transmitting
the decimal part of the degrees as as unsigned integer when in reality
they were signed, leading to some pretty significantly incorrect
results. Luckily we were able to figure out how to determine the actual
position from the data it was transmitting (thanks, SpeedEvil on
\#highaltitude on irc.freenode.net!) and the balloon was successfully
recovered.

Ferret is on its way back to us in the post now and hopefully will live
to fly another day!

P.S. we got [hackaday][]'d too!

  [CU Spaceflight]: http://www.srcf.ucam.org/~cuspaceflight/
  [pick up its GPS position and help keep track]: http://ukhas.org.uk/guides:tracking_guide
  [Jon Sowman]: http://www.hexoc.com/wb/pages/ferret.php
  [Radiometrix NTX2]: http://www.radiometrix.co.uk/products/ntx2nrx2.htm
  [UKHAS Church Hill Site Project Orion]: http://www.dailymotion.com/video/xchspy_ukhas-church-hill-site-project-orio_webcam
  [kannasnakka]: http://www.dailymotion.com/kannasnakka
  [More video blogs and vloggers.]: http://www.dailymotion.com/gb/channel/webcam
  [hackaday]: http://hackaday.com/2010/03/17/arduino-balloon-tracking/
