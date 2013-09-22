Title: Nixie Tubes: Lit up at last!
Date: 2008-09-24 22:30
Author: admin
Category: Electronics, HomeMadePCBs
Slug: nixie-tubes-lit-up-at-last

[![Nixies At Last][]][]

I know I got them months and months ago, but I've only just had time to
actually do anything besides work. While I do have a big project coming
up (but not really at the point where I can write about it), I did
finally make the PCB for the nixie power supply I designed a while back.

While I did realise I'd forgotten to put in a 56k resistor when I
designed the circuit, I was able to add this in with a through-the-hole
resistor I had lying around that was just the right size.

I powered up the circuit with a 9V battery and held my breath as the
voltage reading on the multimeter jumped to 246! A quick turn of the pot
on the back and the voltage hit 170V, ideal for the nixies.

I connected one up and lo and behold, it lit up! The glow really is
ethereal - cameras cannot capture this, you have to see it in person.
That didn't stop me from trying, though!

The next step is to make a PCB to control all 12 nixies (probably with
three of the power supply modules) and maybe link it into an RTC (though
that is a bit boring - I might try doing something else, like GPS
position?).

[![Nixies At Last][1]][]

[Schematic][] - [Board][] (the board isn't great, with some pretty fine
tracks that run pretty close to each other, but it does have the 56k
resistor I forgot in my version) (both files under [CC-BY-SA-NC][]).

  [Nixies At Last]: http://static.flickr.com/3060/2886242440_ddc348a7fb_m.jpg
  [![Nixies At Last][]]: http://www.flickr.com/photos/7320302@N07/2886242440/
    "Nixies At Last"
  [1]: http://static.flickr.com/3107/2885405091_445ab05536_m.jpg
  [![Nixies At Last][1]]: http://www.flickr.com/photos/7320302@N07/2885405091/
    "Nixies At Last"
  [Schematic]: http://randomskk.net/projects/nixie_psu/psu.sch
    "PSU Schematic"
  [Board]: http://randomskk.net/projects/nixie_psu/psu.brd "PSU Board"
  [CC-BY-SA-NC]: http://creativecommons.org/licenses/by-nc-sa/3.0/
