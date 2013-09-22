Title: STM32 Prototyping Boards
Date: 2009-09-14 22:19
Author: Adam Greig
Tags: ARM, Electronics
Slug: stm32-prototyping-boards

I used an STM32 for the first time in [Robot2][], and soon discovered
how cool they were. Each one is packed full of neat peripherals, runs
really really fast and can do all sorts of cool stuff that simpler µCs
like an ATmega simply can't pull off. With this in mind, I asked ST for
two samples of their STM32F103CBT6, a 48pin LQFP package. They sent the
samples (thanks, ST!) and I got to making up a PCB to put them on.

[flickr pid="3921208392" size="medium"]

I decided I wanted something with a lot of interface peripherals, so
broke out USART1, 2 and 3, I²C1 and 2 (also USART3) and SPI1 and 2.
Additionally a USB plug is connected to the USB peripheral, and JTAG is
available. The 6pin header for USART1 is compatible with the FTDI
cables/breakouts which makes interfacing with an FTDI cable for
programming (the bootloader listens on USART1) or with an xbee on one of
SparkFun's breakouts is very easy.

[flickr pid="3920427009" size="medium"]

So far I've used one of these boards for Robot3 (an upcoming post) and
plan to use the second to start prototypes with my quadcopter UAV.
They're pretty useful, uploading code to them is quick and easy with the
bootloader, and having that many peripherals available and capable of
running at pretty high speeds makes these boards handy to have around.

[flickr pid="3920430553" size="medium"]

Eagle files and a PNG [here][].

  [Robot2]: http://negativeacknowledge.com/2009/05/robot2-an-arm-based-colour-tracking-robot/
  [here]: https://randomskk.net/projects/stm32_dev_board
