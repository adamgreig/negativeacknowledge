Title: 20 LEDs, 5 pins: Charlieplexing!
Date: 2008-05-08 21:53
Author: Adam Greig
Tags: AVR, Electronics
Slug: 20-leds-5-pins-charlieplexing

![almost works!](http://static.flickr.com/2414/2435299668_3eb69d7bf5.jpg)

I recently ordered 100 blue LEDs from eBay for a measly £1 (plus p&amp;p of
something like £3). To my surprise, they are both bright and all
functioning!

However, I hadn't really thought through what to do with them.

This was when I found a link to the [charlieplexing instructable][]
again, and decided to whip it together on a piece of protoboard. This
turned out to be an absolute nightmare of wiring things up, hidden
shorts, melting wire, all that fun stuff. In the end, I got *most* of
the LEDs working fine, and a few are a bit screwed up. They can each be
individually controlled using just five pins on the little ATtiny13 in
the middle there, and it even has five input buttons (one per pin)!

This is a pretty neat use of tiny amounts of IO pins.

Unfortunately the back of the thing looks like this:

![finished - there are two shorts somewhere. where? no idea](http://static.flickr.com/2114/2432745328_d7e6117b05.jpg)

and I never quite got the courage to get the last few working.

I plan to instead make a PCB for them! Of course, the wiring there will
no doubt be equally nightmaric, but at least the manufacturing should be
easy.

[Flickr](http://www.flickr.com/photos/7320302@N07/2432745328/)
