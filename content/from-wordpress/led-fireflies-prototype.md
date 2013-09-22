Title: LED Fireflies: Prototype
Date: 2008-04-04 20:28
Author: Adam Greig
Tags: Electronics
Slug: led-fireflies-prototype

![it works!](http://static.flickr.com/3231/2348220444_285de14291.jpg)

I've got the second prototype made for my LED Firefly idea. This one
uses all through-the-hole components, compared to the entirely surface
mounted first prototype.  
I did this for a few reasons:

-   I have far more through-the-hole RGB LEDs than surface mounted, and
    they're brighter to boot
-   I also have more ATtiny13s in through-the-hole packages
-   The chips are easier to change out
-   It's easier for others to assemble!

However, the new prototype isn't without problems. It seems the
photocopier merely flipped my image instead of mirroring it, so the
ATtiny13 has to be inserted backwards. This means I can't really program
it more than once, and bending the pins more than once breaks them.
Oops! The other components are more lenient about which way they go in.

![assembled](http://static.flickr.com/2115/2347389493_5d769ab97c.jpg)

Second, I actually made it without ordering any 12mm batteries, so I
can't power them via battery. I did solder a 2\*AA battery box to one,
which is nice but takes up a fair bit of space. I'd like to work out the
best way to power these things.

I tried silkscreening the PCBs this time, but this wasn't too
successful. It seems the toner sticks to copper a \_lot\_ better than to
plain FR2. Additionally the silkscreen was not flipped right either, so
I had to either put it on the copper side or have it backwards on the
top! I went for a bit of both:

![Silkscreen?](http://static.flickr.com/2121/2348215940_7210c43ac2.jpg)

However, the basics do work right now - although my code still doesn't
do light detection, which I need to work on - and it looks really good
when encapsulated in some foam.

I think the next step will be to finish off the code and then get these
things produced properly for some nice PCBs.

[Flickr](http://www.flickr.com/photos/7320302@N07/2348220444/)
