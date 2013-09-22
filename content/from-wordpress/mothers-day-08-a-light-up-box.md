Title: Mother's Day '08: A Light-Up Box
Date: 2008-03-02 17:52
Author: admin
Category: AVR, Electronics
Slug: mothers-day-08-a-light-up-box

[![Making PCBs at home, Attempt 2: Done!][]][]

Mother's Day was coming up and I'd just got the hang of making PCBs at
home, along with a new Dremel that could cut and drill them.  
Making some kind of project seemed the obvious answer. I took
inspiration from an Instructable on a similar subject [here][], but
didn't have any fluorescent acrylic so had the LEDs illuminate the board
directly.  
It's also etched with normal ferric chloride, unfortunately.

I'd just picked up some new surface mount button-cell holders, and while
I was tempted to use a 555 to make a quick pulse that drives the LEDs, a
simpler circuit could be made with an ATtiny13, and I just so happened
to have ten of them sitting around. A little breadboarding and I'd got
the general idea working, although PWM still wasn't working - the LEDs
simply flashed on and then off 12 seconds later, with no fading.

I documented most of the manufacture with my camera, so I'll go through
it with pictures. Here goes...

<!--more--> [![Making PCBs at home, Step 1: Design][]][]

First, the circuit had to be designed. I do this in Eagle, since it's
free and runs on Linux. The design has to be single sided (I've only got
single sided boards, for one thing), and I figured the thicker tracks
would make it more resistant to any problems with the toner transfer. It
didn't take too long to come up with an acceptable design that doesn't
have any jumper wires.

[![Making PCBs at home, Step 2: Print][]][]

Next, I tried using photo paper to print and transfer the toner. This
basically failed miserably - the paper got too hot before the toner was
too hot, and the paper bubbled up underneath, ruining it. I tried all
six circuits that I printed and none worked.  
However, the photos showing the manufacture are the same as for
transparencies, so I'll go through them anyway.

[![Making PCBs at home, Step 3: Get the iron on][]][]

The iron's heated up to "Wool" for transparencies

[![Making PCBs at home, Step 4: Clean the PCB][]][]

Boards are scrubbed clean with a scrubber and also rinsed, I didn't
bother with soap later on and it worked fine. Faux-steel brushes would
probably be even better, or perhaps sandpaper. The key thing is to get a
clean copper surface that's slightly scratched up to help the toner
stick.

[![Making PCBs at home, Step 5: Cut out print][]][]

The chosen design is cut out.

[![Making PCBs at home, Step 6: Stick print to PCB][]][]

And stuck down to the board, toner side down.

[![Making PCBs at home, Step 7: Iron it for 3-5 min][]][]

You then put tissue paper over it to stop the iron sticking to the
paper, and heat it for \~5min.

[![Making PCBs at home, Step 9: Nor were the other 6.][]][]

Sadly, every try with photo paper came out pretty badly.

[![Making PCBs at home, Attempt 2: Transparencies][]][]

I got some transparencies printed. These worked a lot better!

[![Making PCBs at home, Attempt 2: Stick it down][]][]

Transparency is stuck toner-side down. You can tell which way this is
because the circuit should look the right way around when the transfer
is stuck down.

[![Making PCBs at home, Attempt 2: All ironed.][]][]

It did take a second try to get the temperature right, but this is much
better!  
There are still one or two small issues - nothing that stops the board
working, but a few tracks lost a little toner. This is easily fixed with
a standard permanent marker.

[![Making PCBs at home, Attempt 2: Cut with a Dremel][]][]

I cut out the PCBs using a cutting disk on the Dremel (in this case the
one-clic cutting disks which I believe are fibreglass-reinforced ones).
This wasn't too easy since the edge of the dremel somewhat restricts how
deep the cut can be into the material, but I was just able to get them
both cut out nicely.  
Then I sanded them down at the edges to make them nice and smooth.

[![Making PCBs at home, Attempt 2: Etched in Ferric Chloride][]][]

I then etched both boards in ferric chloride. This is a fairly poor, but
easily available etchant that doesn't give off nasty fumes. It does
stain everything, so I'm wearing gloves here. I have a plastic tray of
etchant placed in a larger plastic tray of hot water, which heats the
etchant and catches any spills. I constantly swirl the board around in
the etchant, which makes a big difference in etching time.  
In this photo, you can just see the copper starting to be etched away
in the corners.

[![Making PCBs at home, Attempt 2: Fully etched][]][]

The boards are now fully etched, the only copper left is hopefully under
the toner!  
The toner is non conductive and can't be soldered to, so we need to
strip it off the copper tracks.

[![Making PCBs at home, Attempt 2: Acetone dissolves the toner][]][]

I usually let the boards soak in acetone for ten minutes and then scrub
hard to remove the toner. I'm also removing the toner from the
non-etched board so it can be reused.  
In retrospect, I noticed a few things:  
1) There really wasn't any need to remove toner from the top PCB, since
it won't be soldered to and toner may have even made the sign stand out
better. However, the copper does look fairly nice.  
2) Toner could also be used as something of a solder stop, so
potentially I could have only removed it from pads that had to be
soldered too. This may have been risky later on with the copper heating
up, though.  
3) Paint stripper probably would have worked better.

[![Making PCBs at home, Attempt 2: Toner removed and holes drilled with
Dremel][]][]

The PCBs are then drilled: a 3mm hole for the 4-40 thread screws, and
0.8mm holes for everything else. I'm using HSS drill bits in my Dremel
at 33k RPM, the boards are FR2 so there's not so much need for tungsten
carbide drill bits.

[![Making PCBs at home, Attempt 2: All holes drilled][]][]

Both boards are now drilled.

[![Making PCBs at home, Attempt 2: Parts soldered][]][]

Components get soldered on. Soldering the LEDs was a real pain, but
luckily you can't see the solder when the thing is closed up. In the
future, I'd probably use surface mounted LEDs. The battery holder
doesn't seem to fit the batteries very well, so I use two batteries
instead - this is not only a much better contact, but also drives up the
LED's brightnesses.

[![Making PCBs at home, Attempt 2: Stuck together (nb: used two
standoffs in the end)][]][]

I ended up using two stand-offs taped together, instead of just one, to
give the LEDs more space to diffuse. This made a big difference. It also
let me cover the outsides with tape, which makes the whole thing look a
lot more solid.

[![Making PCBs at home, Attempt 2: Done!][]][]

Finally, here it is in all its glory!

The ATtiny13 has a fairly simple program that just turns on the LEDs
through a transistor for 12s when the button is pressed, and goes to
sleep (power-down mode) otherwise. I wanted to have the LEDs fade in and
out using PWM, but I wasn't able to figure out how to do proper PWM with
the IC's counters in time, and software PWM took up too much space when
the code was compiled, for some reason. Having some kind of on/off mode
might have been a neat idea too, although this way the two batteries
should last a lot longer.

I hope you enjoyed reading through the project! I've attached the Eagle
files below if anyone wants to try printing one, although since Mother's
Day has passed I'd suggest changing the message :p

[Eagle Board][]

[Eagle Schematic][]

[][Eagle Board]

  [Making PCBs at home, Attempt 2: Done!]: http://farm3.static.flickr.com/2209/2304333959_021857e71d.jpg
  [![Making PCBs at home, Attempt 2: Done!][]]: http://flickr.com/photos/randomskk/2304333959
    "View this photo on Flickr"
  [here]: http://www.instructables.com/id/UVIL-Backlit-Blacklight-Nightlight-or-SteamPunk-
  [Making PCBs at home, Step 1: Design]: http://farm4.static.flickr.com/3256/2299143684_490e63f3bb.jpg
  [![Making PCBs at home, Step 1: Design][]]: http://flickr.com/photos/randomskk/2299143684
    "View this photo on Flickr"
  [Making PCBs at home, Step 2: Print]: http://farm4.static.flickr.com/3014/2298349919_b49f21266e.jpg
  [![Making PCBs at home, Step 2: Print][]]: http://flickr.com/photos/randomskk/2298349919
    "View this photo on Flickr"
  [Making PCBs at home, Step 3: Get the iron on]: http://farm4.static.flickr.com/3277/2298351685_1d0e9cfd7f.jpg
  [![Making PCBs at home, Step 3: Get the iron on][]]: http://flickr.com/photos/randomskk/2298351685
    "View this photo on Flickr"
  [Making PCBs at home, Step 4: Clean the PCB]: http://farm4.static.flickr.com/3083/2298354343_6249112815.jpg
  [![Making PCBs at home, Step 4: Clean the PCB][]]: http://flickr.com/photos/randomskk/2298354343
    "View this photo on Flickr"
  [Making PCBs at home, Step 5: Cut out print]: http://farm4.static.flickr.com/3238/2298357307_46acd42ff1.jpg
  [![Making PCBs at home, Step 5: Cut out print][]]: http://flickr.com/photos/randomskk/2298357307
    "View this photo on Flickr"
  [Making PCBs at home, Step 6: Stick print to PCB]: http://farm4.static.flickr.com/3287/2299155116_95965583a8.jpg
  [![Making PCBs at home, Step 6: Stick print to PCB][]]: http://flickr.com/photos/randomskk/2299155116
    "View this photo on Flickr"
  [Making PCBs at home, Step 7: Iron it for 3-5 min]: http://farm4.static.flickr.com/3101/2298361473_c7f7795a90.jpg
  [![Making PCBs at home, Step 7: Iron it for 3-5 min][]]: http://flickr.com/photos/randomskk/2298361473
    "View this photo on Flickr"
  [Making PCBs at home, Step 9: Nor were the other 6.]: http://farm4.static.flickr.com/3232/2299161968_f6ee093322.jpg
  [![Making PCBs at home, Step 9: Nor were the other 6.][]]: http://flickr.com/photos/randomskk/2299161968
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Transparencies]: http://farm3.static.flickr.com/2017/2305058162_191fe63821.jpg
  [![Making PCBs at home, Attempt 2: Transparencies][]]: http://flickr.com/photos/randomskk/2305058162
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Stick it down]: http://farm4.static.flickr.com/3191/2304263567_2df3d6c2c6.jpg
  [![Making PCBs at home, Attempt 2: Stick it down][]]: http://flickr.com/photos/randomskk/2304263567
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: All ironed.]: http://farm3.static.flickr.com/2417/2304270631_c45364370a.jpg
  [![Making PCBs at home, Attempt 2: All ironed.][]]: http://flickr.com/photos/randomskk/2304270631
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Cut with a Dremel]: http://farm4.static.flickr.com/3042/2304274529_3026224509.jpg
  [![Making PCBs at home, Attempt 2: Cut with a Dremel][]]: http://flickr.com/photos/randomskk/2304274529
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Etched in Ferric Chloride]: http://farm3.static.flickr.com/2358/2304278037_16a940c344.jpg
  [![Making PCBs at home, Attempt 2: Etched in Ferric Chloride][]]: http://flickr.com/photos/randomskk/2304278037
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Fully etched]: http://farm3.static.flickr.com/2107/2304281841_80cb02ffe7.jpg
  [![Making PCBs at home, Attempt 2: Fully etched][]]: http://flickr.com/photos/randomskk/2304281841
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Acetone dissolves the toner]: http://farm3.static.flickr.com/2089/2304285407_dfea001636.jpg
  [![Making PCBs at home, Attempt 2: Acetone dissolves the toner][]]: http://flickr.com/photos/randomskk/2304285407
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Toner removed and holes drilled with
  Dremel]: http://farm4.static.flickr.com/3092/2304288909_44234a1879.jpg
  [![Making PCBs at home, Attempt 2: Toner removed and holes drilled
  with Dremel][]]: http://flickr.com/photos/randomskk/2304288909
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: All holes drilled]: http://farm4.static.flickr.com/3269/2305091166_c1cb801cca.jpg
  [![Making PCBs at home, Attempt 2: All holes drilled][]]: http://flickr.com/photos/randomskk/2305091166
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Parts soldered]: http://farm3.static.flickr.com/2402/2305097638_dda24bb51e.jpg
  [![Making PCBs at home, Attempt 2: Parts soldered][]]: http://flickr.com/photos/randomskk/2305097638
    "View this photo on Flickr"
  [Making PCBs at home, Attempt 2: Stuck together (nb: used two
  standoffs in the end)]: http://farm3.static.flickr.com/2057/2305122182_773446458f.jpg
  [![Making PCBs at home, Attempt 2: Stuck together (nb: used two
  standoffs in the end)][]]: http://flickr.com/photos/randomskk/2305122182
    "View this photo on Flickr"
  [Eagle Board]: http://negativeacknowledge.com/wp-content/uploads/2008/03/rev02.brd
    "Eagle Board"
  [Eagle Schematic]: http://negativeacknowledge.com/wp-content/uploads/2008/03/rev02.sch
    "Eagle Schematic"
