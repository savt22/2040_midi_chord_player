# 2040_midi_chord_player
MIDI chord player with modifier keys

This was inspired by https://blog.4dcu.be/diy/2021/05/20/MIDIpad.html (who also gave some pointers on code) and https://gist.github.com/sandyjmacdonald/804dc737e7cb798d1b4fa34adc87e2d4. I also got some pointers on r/synthdiy. 

I started with absolutely no idea what I'm doing, and I'm sure this shows in the code. Feels like a lot of it is redundant and there would definitely be a better way of doing this... nevertheless, it does what I wanted it to. 

This is designed to work on the Pimoroni Pico RGB Base, and the first step is getting it set-up following this guide (and adding in the bits on the USB Midi example: https://github.com/pimoroni/keybow2040-circuitpython

The base doesn't actually feel idea for this task, as sometimes you have to hit the pads firmly to register a keypress. I've ordered a Keybow 2040 and will see if it works better on that. 
