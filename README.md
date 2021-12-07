# 2040_midi_chord_player
MIDI chord player with modifier keys

This was inspired by https://blog.4dcu.be/diy/2021/05/20/MIDIpad.html (who also gave some helpful pointers on code) and https://gist.github.com/sandyjmacdonald/804dc737e7cb798d1b4fa34adc87e2d4. I also got some pointers on r/synthdiy. 

I started with absolutely no idea what I'm doing, and I'm sure this shows in the code. Feels like a lot of it is redundant and there would definitely be a better way of doing this... nevertheless, it does what I wanted it to. 

This is designed to work on the Pimoroni Pico RGB Base. It also works on the Keybow 2040. 

The first step is getting it set-up following this guide: https://github.com/pimoroni/keybow2040-circuitpython

You need to flash your board with CircuitPython 7, then you need to add the file keybow.py and the folder keybow_hardware from the above link to the CIRCUITPY's lib folder, along with adafruit_dotstar.mpy from here: https://github.com/adafruit/Adafruit_CircuitPython_DotStar/releases and adafruit_midi folder from here: https://github.com/adafruit/Adafruit_CircuitPython_MIDI

Then replace code.py on CIRCUITPY with the code.py file from this library. 

The base is programmed chromatically from C3-B3, starting in the bottom left and working through the first three columns top to bottom. The white notes are lit pink, and the black notes are lit green. 

The final column are the modifier keys which control which chord is played. If no modifier is pressed, each keyboard keypad will send a single note.

Mod1: maj triad (this was written to use with a 3 voice synth, so all chord variations have 3 notes only - that can easily be changed in the code.)

Mod2: min triad

Mod 3: maj7 triad (no fifth)

Mod4: min7

The following key combinations were removed. For some reason, including multiple key combo modifiers works without issue on Windows, but it causes a range of issues on Mac, including stopping it mounting. The Keybow 2040 also didn't like it. Would like to add this back in, and it's being worked on. 

Mod1 + mod3: maj add9 

Mod2 + mod4: min add9

All 4 mods: half dim

There are loads of modifier key combos left which can be programmed how you like. 

[![IMAGE ALT TEXT](http://img.youtube.com/vi/sJZyv5DZECY/0.jpg)](https://www.youtube.com/watch?v=sJZyv5DZECY "RGB Pico Keypad MIDI Keyboard and Chord Player
")
