Title: Breadboard ICSP Adapter
Date: 2008-04-04 20:31
Author: Adam Greig
Tags: Uncategorized
Slug: breadboard-icsp-adapter

At the same time I etched the LED Firefly prototypes, I did some
breadboard ICSP adapters. I've been working with ATtiny13s a lot
recently, and they are a pain to program while breadboarding, so these
seemed like just the thing.

![Breadboard ICSP adaptor](http://static.flickr.com/2304/2355712642_8deabaf564_m.jpg)

It has a 6pin ICSP plug on top, and connects to the breadboard's power
rails and the four pins along one side of the ATtiny13. It provides the
AVR with +ve power and three of four required ICSP connections. The
final pin has to be connected to pin one of the AVR, so the whole PCB
reduces ICSP connections down to just one jump wire.

It works really nicely from my quick experiments, which is nice!

![Breadboard ICSP adaptor](http://static.flickr.com/3200/2355716920_6a3f190f9e_m.jpg)

[Flickr](http://www.flickr.com/photos/7320302@N07/2355716920/)
