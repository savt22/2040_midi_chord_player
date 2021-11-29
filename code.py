#this was originally for the Volca FM - so only 3 voices. 
#Add additional NoteOff/NoteOn if more than 3 note chords required

import time
from keybow2040 import Keybow2040
#from keybow_hardware.pim56x import PIM56X as Hardware # for Keybow 2040
from keybow_hardware.pim551 import PIM551 as Hardware # for Pico RGB Keypad Base

import usb_midi
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

keybow = Keybow2040(Hardware())
keys = keybow.keys

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)
rgb = (0, 0, 0)

#sets keyboard layout, creates slight flicker when holding down button. White and black notes on piano different colours 
while True:
    keybow.update()

    for key in keys:
        if key.pressed:
            key.set_led(*rgb)
        else:
            keybow.set_led(0, 100, 100, 100)
            keybow.set_led(1, 50, 100, 10)
            keybow.set_led(2, 100, 100, 100)
            keybow.set_led(3, 50, 100, 10)
            keybow.set_led(4, 100, 100, 100)
            keybow.set_led(5, 100, 100, 100)
            keybow.set_led(6, 50, 100, 10)
            keybow.set_led(7, 100, 100, 100)
            keybow.set_led(8, 50, 100, 10)
            keybow.set_led(9, 100, 100, 100)
            keybow.set_led(10, 50, 100, 10)
            keybow.set_led(11, 100, 100, 100)
            keybow.set_led(12, 200, 100, 100)
            keybow.set_led(13, 100, 200, 100)
            keybow.set_led(14, 100, 100, 200)
            keybow.set_led(15, 100, 50, 100)


                      #C single note
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send(NoteOn(60, 127))

        @keybow.on_release(C)
        def release_handler(C):

            midi.send(NoteOff(60, 0))
                      
                     #C major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send([NoteOn(60, 127),
                       NoteOn(64, 127),
                       NoteOn(67, 127)])

        @keybow.on_release(C)
        def release_handler(C):

            midi.send([NoteOff(60, 127),
                       NoteOff(64, 127),
                       NoteOff(67, 127)])

                      #C minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send([NoteOn(60, 127),
                       NoteOn(63, 127),
                       NoteOn(67, 127)])

        @keybow.on_release(C)
        def release_handler(C):

            midi.send([NoteOff(60, 127),
                       NoteOff(63, 127),
                       NoteOff(67, 127)])

                      #C maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send([NoteOn(60, 127),
                       NoteOn(64, 127),
                       NoteOn(71, 127)])

        @keybow.on_release(C)
        def release_handler(C):

            midi.send([NoteOff(60, 127),
                       NoteOff(64, 127),
                       NoteOff(71, 127)])

                      #C min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send([NoteOn(60, 127),
                       NoteOn(63, 127),
                       NoteOn(70, 127)])

        @keybow.on_release(C)
        def release_handler(C):

            midi.send([NoteOff(60, 127),
                       NoteOff(63, 127),
                       NoteOff(70, 127)])

                     #C maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send([NoteOn(60, 127),
                       NoteOn(64, 127),
                       NoteOn(74, 127)])

        @keybow.on_release(C)
        def release_handler(C):

            midi.send([NoteOff(60, 127),
                       NoteOff(64, 127),
                       NoteOff(74, 127)])

                     #C min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send([NoteOn(60, 127),
                       NoteOn(63, 127),
                       NoteOn(74, 127)])

        @keybow.on_release(C)
        def release_handler(C):

            midi.send([NoteOff(60, 127),
                       NoteOff(63, 127),
                       NoteOff(74, 127)])

                    #C half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        C = keys[0]
        @keybow.on_press(C)
        def press_handler(C):

            midi.send([NoteOn(60, 127),
                       NoteOn(66, 127),
                       NoteOn(70, 127)])

        @keybow.on_release(C)
        def release_handler(C):

            midi.send([NoteOff(60, 127),
                       NoteOff(66, 127),
                       NoteOff(70, 127)])

                      #Db single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send(NoteOn(61, 127))

        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send(NoteOff(61, 0))
                      
                     #Db major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send([NoteOn(61, 127),
                       NoteOn(65, 127),
                       NoteOn(68, 127)])

        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send([NoteOff(61, 127),
                       NoteOff(65, 127),
                       NoteOff(68, 127)])

                      #Db minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send([NoteOn(61, 127),
                       NoteOn(64, 127),
                       NoteOn(68, 127)])

        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send([NoteOff(61, 127),
                       NoteOff(64, 127),
                       NoteOff(68, 127)])

                      #Db maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send([NoteOn(61, 127),
                       NoteOn(65, 127),
                       NoteOn(72, 127)])
       
        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send([NoteOff(61, 127),
                       NoteOff(65, 127),
                       NoteOff(72, 127)])

                      #min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send([NoteOn(61, 127),
                       NoteOn(64, 127),
                       NoteOn(71, 127)])
       
        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send([NoteOff(61, 127),
                       NoteOff(64, 127),
                       NoteOff(71, 127)])

                     #maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send([NoteOn(61, 127),
                       NoteOn(65, 127),
                       NoteOn(75, 127)])

        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send([NoteOff(61, 127),
                       NoteOff(65, 127),
                       NoteOff(75, 127)])

                     #min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send([NoteOn(61, 127),
                       NoteOn(64, 127),
                       NoteOn(75, 127)])

        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send([NoteOff(61, 127),
                       NoteOff(64, 127),
                       NoteOff(75, 127)])

                    #half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        Db = keys[1]
        @keybow.on_press(Db)
        def press_handler(Db):

            midi.send([NoteOn(61, 127),
                       NoteOn(67, 127),
                       NoteOn(71, 127)])

        @keybow.on_release(Db)
        def release_handler(Db):

            midi.send([NoteOff(61, 127),
                       NoteOff(67, 127),
                       NoteOff(71, 127)])

                      #D single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send(NoteOn(62, 127))

        @keybow.on_release(D)
        def release_handler(D):

            midi.send(NoteOff(62, 0))
                      
                     #D major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send([NoteOn(62, 127),
                       NoteOn(66, 127),
                       NoteOn(69, 127)])

        @keybow.on_release(D)
        def release_handler(D):

            midi.send([NoteOff(62, 127),
                       NoteOff(66, 127),
                       NoteOff(69, 127)])

                      #D minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send([NoteOn(62, 127),
                       NoteOn(65, 127),
                       NoteOn(69, 127)])

        @keybow.on_release(D)
        def release_handler(D):

            midi.send([NoteOff(62, 127),
                       NoteOff(65, 127),
                       NoteOff(69, 127)])

                      #D maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send([NoteOn(62, 127),
                       NoteOn(66, 127),
                       NoteOn(73, 127)])
       
        @keybow.on_release(D)
        def release_handler(D):

            midi.send([NoteOff(62, 127),
                       NoteOff(66, 127),
                       NoteOff(73, 127)])

                      #D min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send([NoteOn(62, 127),
                       NoteOn(65, 127),
                       NoteOn(72, 127)])

        @keybow.on_release(D)
        def release_handler(D):

            midi.send([NoteOff(62, 127),
                       NoteOff(65, 127),
                       NoteOff(72, 127)])

                     #D maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send([NoteOn(62, 127),
                       NoteOn(66, 127),
                       NoteOn(76, 127)])

        @keybow.on_release(D)
        def release_handler(D):

            midi.send([NoteOff(62, 127),
                       NoteOff(66, 127),
                       NoteOff(76, 127)])

                     #D min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send([NoteOn(62, 127),
                       NoteOn(65, 127),
                       NoteOn(76, 127)])

        @keybow.on_release(D)
        def release_handler(D):

            midi.send([NoteOff(62, 127),
                       NoteOff(65, 127),
                       NoteOff(76, 127)])

                    #D half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        D = keys[2]
        @keybow.on_press(D)
        def press_handler(D):

            midi.send([NoteOn(62, 127),
                       NoteOn(68, 127),
                       NoteOn(72, 127)])

        @keybow.on_release(D)
        def release_handler(D):

            midi.send([NoteOff(62, 127),
                       NoteOff(68, 127),
                       NoteOff(72, 127)])

                      #Eb single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Eb = keys[3]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send(NoteOn(63, 127))

        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send(NoteOff(63, 0))
                      
                     #Eb major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Eb = keys[3]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send([NoteOn(63, 127),
                       NoteOn(67, 127),
                       NoteOn(70, 127)])

        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send([NoteOff(63, 127),
                       NoteOff(67, 127),
                       NoteOff(70, 127)])

                      #Eb minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Eb = keys[3]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send([NoteOn(63, 127),
                       NoteOn(66, 127),
                       NoteOn(70, 127)])

        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send([NoteOff(63, 127),
                       NoteOff(66, 127),
                       NoteOff(70, 127)])

                      #Eb maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Eb = keys[3]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send([NoteOn(63, 127),
                       NoteOn(67, 127),
                       NoteOn(74, 127)])
       
        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send([NoteOff(63, 127),
                       NoteOff(67, 127),
                       NoteOff(74, 127)])

                      #Eb min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Eb = keys[3]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send([NoteOn(63, 127),
                       NoteOn(66, 127),
                       NoteOn(73, 127)])

        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send([NoteOff(63, 127),
                       NoteOff(66, 127),
                       NoteOff(73, 127)])

                     #Eb maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Eb = keys[3]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send([NoteOn(63, 127),
                       NoteOn(67, 127),
                       NoteOn(77, 127)])

        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send([NoteOff(63, 127),
                       NoteOff(67, 127),
                       NoteOff(77, 127)])

                     #Eb min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Eb = keys[3]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send([NoteOn(63, 127),
                       NoteOn(66, 127),
                       NoteOn(77, 127)])

        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send([NoteOff(63, 127),
                       NoteOff(66, 127),
                       NoteOff(77, 127)])

                    #Eb half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        D = keys[2]
        @keybow.on_press(Eb)
        def press_handler(Eb):

            midi.send([NoteOn(63, 127),
                       NoteOn(69, 127),
                       NoteOn(73, 127)])

        @keybow.on_release(Eb)
        def release_handler(Eb):

            midi.send([NoteOff(63, 127),
                       NoteOff(69, 127),
                       NoteOff(73, 127)])

                      #E single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send(NoteOn(64, 127))

        @keybow.on_release(E)
        def release_handler(E):

            midi.send(NoteOff(64, 0))
                      
                     #E major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send([NoteOn(64, 127),
                       NoteOn(68, 127),
                       NoteOn(71, 127)])

        @keybow.on_release(E)
        def release_handler(E):

            midi.send([NoteOff(64, 127),
                       NoteOff(68, 127),
                       NoteOff(71, 127)])

                      #E minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send([NoteOn(64, 127),
                       NoteOn(67, 127),
                       NoteOn(71, 127)])

        @keybow.on_release(E)
        def release_handler(E):

            midi.send([NoteOff(64, 127),
                       NoteOff(67, 127),
                       NoteOff(71, 127)])

                      #E maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send([NoteOn(64, 127),
                       NoteOn(68, 127),
                       NoteOn(75, 127)])
       
        @keybow.on_release(E)
        def release_handler(E):

            midi.send([NoteOff(64, 127),
                       NoteOff(68, 127),
                       NoteOff(75, 127)])

                      #E min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send([NoteOn(64, 127),
                       NoteOn(67, 127),
                       NoteOn(74, 127)])

        @keybow.on_release(E)
        def release_handler(E):

            midi.send([NoteOff(64, 127),
                       NoteOff(67, 127),
                       NoteOff(74, 127)])

                     #E maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send([NoteOn(64, 127),
                       NoteOn(68, 127),
                       NoteOn(78, 127)])

        @keybow.on_release(E)
        def release_handler(E):

            midi.send([NoteOff(64, 127),
                       NoteOff(68, 127),
                       NoteOff(78, 127)])

                     #E min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send([NoteOn(64, 127),
                       NoteOn(67, 127),
                       NoteOn(78, 127)])

        @keybow.on_release(E)
        def release_handler(E):

            midi.send([NoteOff(64, 127),
                       NoteOff(67, 127),
                       NoteOff(78, 127)])

                    #E half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        E = keys[4]
        @keybow.on_press(E)
        def press_handler(E):

            midi.send([NoteOn(64, 127),
                       NoteOn(70, 127),
                       NoteOn(74, 127)])

        @keybow.on_release(E)
        def release_handler(E):

            midi.send([NoteOff(64, 127),
                       NoteOff(70, 127),
                       NoteOff(74, 127)])

                      #F single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send(NoteOn(65, 127))

        @keybow.on_release(F)
        def release_handler(F):

            midi.send(NoteOff(65, 0))
                      
                     #F major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send([NoteOn(65, 127),
                       NoteOn(69, 127),
                       NoteOn(72, 127)])

        @keybow.on_release(F)
        def release_handler(F):

            midi.send([NoteOff(65, 127),
                       NoteOff(69, 127),
                       NoteOff(72, 127)])

                      #F minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send([NoteOn(65, 127),
                       NoteOn(68, 127),
                       NoteOn(72, 127)])

        @keybow.on_release(F)
        def release_handler(F):

            midi.send([NoteOff(65, 127),
                       NoteOff(68, 127),
                       NoteOff(72, 127)])

                      #F maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send([NoteOn(65, 127),
                       NoteOn(69, 127),
                       NoteOn(76, 127)])
       
        @keybow.on_release(F)
        def release_handler(F):

            midi.send([NoteOff(65, 127),
                       NoteOff(69, 127),
                       NoteOff(76, 127)])

                      #F min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send([NoteOn(65, 127),
                       NoteOn(68, 127),
                       NoteOn(75, 127)])

        @keybow.on_release(F)
        def release_handler(F):

            midi.send([NoteOff(65, 127),
                       NoteOff(68, 127),
                       NoteOff(75, 127)])

                     #F maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send([NoteOn(65, 127),
                       NoteOn(69, 127),
                       NoteOn(79, 127)])

        @keybow.on_release(F)
        def release_handler(F):

            midi.send([NoteOff(65, 127),
                       NoteOff(69, 127),
                       NoteOff(79, 127)])

                     #F min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send([NoteOn(65, 127),
                       NoteOn(68, 127),
                       NoteOn(79, 127)])

        @keybow.on_release(F)
        def release_handler(F):

            midi.send([NoteOff(65, 127),
                       NoteOff(68, 127),
                       NoteOff(79, 127)])

                    #F half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        F = keys[5]
        @keybow.on_press(F)
        def press_handler(F):

            midi.send([NoteOn(65, 127),
                       NoteOn(71, 127),
                       NoteOn(75, 127)])

        @keybow.on_release(F)
        def release_handler(F):

            midi.send([NoteOff(65, 127),
                       NoteOff(71, 127),
                       NoteOff(75, 127)])

                      #Gb single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send(NoteOn(66, 127))

        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send(NoteOff(66, 0))
                      
                     #Gb major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send([NoteOn(66, 127),
                       NoteOn(70, 127),
                       NoteOn(73, 127)])

        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send([NoteOff(66, 127),
                       NoteOff(70, 127),
                       NoteOff(73, 127)])

                      #Gb minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send([NoteOn(66, 127),
                       NoteOn(69, 127),
                       NoteOn(73, 127)])

        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send([NoteOff(66, 127),
                       NoteOff(69, 127),
                       NoteOff(73, 127)])

                      #Gb maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send([NoteOn(66, 127),
                       NoteOn(70, 127),
                       NoteOn(77, 127)])
       
        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send([NoteOff(66, 127),
                       NoteOff(70, 127),
                       NoteOff(77, 127)])

                      #Gb min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send([NoteOn(66, 127),
                       NoteOn(69, 127),
                       NoteOn(76, 127)])

        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send([NoteOff(66, 127),
                       NoteOff(69, 127),
                       NoteOff(76, 127)])

                     #Gb maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send([NoteOn(66, 127),
                       NoteOn(70, 127),
                       NoteOn(80, 127)])

        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send([NoteOff(66, 127),
                       NoteOff(70, 127),
                       NoteOff(80, 127)])

                     #Gb min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send([NoteOn(66, 127),
                       NoteOn(69, 127),
                       NoteOn(80, 127)])

        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send([NoteOff(66, 127),
                       NoteOff(69, 127),
                       NoteOff(80, 127)])

                    #Gb half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        Gb = keys[6]
        @keybow.on_press(Gb)
        def press_handler(Gb):

            midi.send([NoteOn(66, 127),
                       NoteOn(72, 127),
                       NoteOn(76, 127)])

        @keybow.on_release(Gb)
        def release_handler(Gb):

            midi.send([NoteOff(66, 127),
                       NoteOff(72, 127),
                       NoteOff(76, 127)])

                      #G single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send(NoteOn(67, 127))

        @keybow.on_release(G)
        def release_handler(G):

            midi.send(NoteOff(67, 0))
                      
                     #G major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send([NoteOn(67, 127),
                       NoteOn(71, 127),
                       NoteOn(74, 127)])

        @keybow.on_release(G)
        def release_handler(G):

            midi.send([NoteOff(67, 127),
                       NoteOff(71, 127),
                       NoteOff(74, 127)])

                      #G minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send([NoteOn(67, 127),
                       NoteOn(70, 127),
                       NoteOn(74, 127)])

        @keybow.on_release(G)
        def release_handler(G):

            midi.send([NoteOff(67, 127),
                       NoteOff(70, 127),
                       NoteOff(74, 127)])

                      #G maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send([NoteOn(67, 127),
                       NoteOn(71, 127),
                       NoteOn(78, 127)])
       
        @keybow.on_release(G)
        def release_handler(G):

            midi.send([NoteOff(67, 127),
                       NoteOff(71, 127),
                       NoteOff(78, 127)])

                      #G min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send([NoteOn(67, 127),
                       NoteOn(70, 127),
                       NoteOn(77, 127)])

        @keybow.on_release(G)
        def release_handler(G):

            midi.send([NoteOff(67, 127),
                       NoteOff(70, 127),
                       NoteOff(77, 127)])

                     #G maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send([NoteOn(67, 127),
                       NoteOn(71, 127),
                       NoteOn(81, 127)])

        @keybow.on_release(G)
        def release_handler(G):

            midi.send([NoteOff(67, 127),
                       NoteOff(71, 127),
                       NoteOff(81, 127)])

                     #G min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send([NoteOn(67, 127),
                       NoteOn(70, 127),
                       NoteOn(81, 127)])

        @keybow.on_release(G)
        def release_handler(G):

            midi.send([NoteOff(67, 127),
                       NoteOff(70, 127),
                       NoteOff(81, 127)])

                    #G half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        G = keys[7]
        @keybow.on_press(G)
        def press_handler(G):

            midi.send([NoteOn(67, 127),
                       NoteOn(73, 127),
                       NoteOn(77, 127)])

        @keybow.on_release(G)
        def release_handler(G):

            midi.send([NoteOff(67, 127),
                       NoteOff(73, 127),
                       NoteOff(77, 127)])

                      #Ab single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send(NoteOn(68, 127))

        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send(NoteOff(68, 0))
                      
                     #Ab major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send([NoteOn(68, 127),
                       NoteOn(72, 127),
                       NoteOn(75, 127)])

        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send([NoteOff(68, 127),
                       NoteOff(72, 127),
                       NoteOff(75, 127)])

                      #Ab minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send([NoteOn(68, 127),
                       NoteOn(71, 127),
                       NoteOn(75, 127)])

        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send([NoteOff(68, 127),
                       NoteOff(71, 127),
                       NoteOff(75, 127)])

                      #Ab maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send([NoteOn(68, 127),
                       NoteOn(72, 127),
                       NoteOn(79, 127)])
       
        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send([NoteOff(68, 127),
                       NoteOff(72, 127),
                       NoteOff(79, 127)])

                      #Ab min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send([NoteOn(68, 127),
                       NoteOn(71, 127),
                       NoteOn(78, 127)])

        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send([NoteOff(68, 127),
                       NoteOff(71, 127),
                       NoteOff(78, 127)])

                     #Ab maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send([NoteOn(68, 127),
                       NoteOn(72, 127),
                       NoteOn(82, 127)])

        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send([NoteOff(68, 127),
                       NoteOff(72, 127),
                       NoteOff(82, 127)])

                     #Ab min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send([NoteOn(68, 127),
                       NoteOn(71, 127),
                       NoteOn(82, 127)])

        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send([NoteOff(68, 127),
                       NoteOff(71, 127),
                       NoteOff(82, 127)])

                    #Ab half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        Ab = keys[8]
        @keybow.on_press(Ab)
        def press_handler(Ab):

            midi.send([NoteOn(68, 127),
                       NoteOn(74, 127),
                       NoteOn(78, 127)])

        @keybow.on_release(Ab)
        def release_handler(Ab):

            midi.send([NoteOff(68, 127),
                       NoteOff(74, 127),
                       NoteOff(78, 127)])


                      #A single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send(NoteOn(69, 127))

        @keybow.on_release(A)
        def release_handler(A):

            midi.send(NoteOff(69, 0))
                      
                     #A major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send([NoteOn(69, 127),
                       NoteOn(73, 127),
                       NoteOn(76, 127)])

        @keybow.on_release(A)
        def release_handler(A):

            midi.send([NoteOff(69, 127),
                       NoteOff(73, 127),
                       NoteOff(76, 127)])

                      #A minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send([NoteOn(69, 127),
                       NoteOn(72, 127),
                       NoteOn(76, 127)])

        @keybow.on_release(A)
        def release_handler(A):

            midi.send([NoteOff(69, 127),
                       NoteOff(72, 127),
                       NoteOff(76, 127)])

                      #A maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send([NoteOn(69, 127),
                       NoteOn(73, 127),
                       NoteOn(80, 127)])

        @keybow.on_release(A)
        def release_handler(A):

            midi.send([NoteOff(69, 127),
                       NoteOff(73, 127),
                       NoteOff(80, 127)])

                      #A min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send([NoteOn(69, 127),
                       NoteOn(72, 127),
                       NoteOn(79, 127)])

        @keybow.on_release(A)
        def release_handler(A):

            midi.send([NoteOff(69, 127),
                       NoteOff(72, 127),
                       NoteOff(79, 127)])

                     #A maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send([NoteOn(69, 127),
                       NoteOn(73, 127),
                       NoteOn(83, 127)])

        @keybow.on_release(A)
        def release_handler(A):

            midi.send([NoteOff(69, 127),
                       NoteOff(73, 127),
                       NoteOff(83, 127)])

                     #A min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send([NoteOn(69, 127),
                       NoteOn(72, 127),
                       NoteOn(83, 127)])

        @keybow.on_release(A)
        def release_handler(A):

            midi.send([NoteOff(69, 127),
                       NoteOff(72, 127),
                       NoteOff(83, 127)])

                    #A half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        A = keys[9]
        @keybow.on_press(A)
        def press_handler(A):

            midi.send([NoteOn(69, 127),
                       NoteOn(75, 127),
                       NoteOn(79, 127)])

        @keybow.on_release(A)
        def release_handler(A):

            midi.send([NoteOff(69, 127),
                       NoteOff(75, 127),
                       NoteOff(79, 127)])

                      #Bb single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send(NoteOn(70, 127))

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send(NoteOff(70, 0))
                      
                     #Bb major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send([NoteOn(70, 127),
                       NoteOn(74, 127),
                       NoteOn(77, 127)])

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send([NoteOff(70, 127),
                       NoteOff(74, 127),
                       NoteOff(77, 127)])

                      #Bb minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send([NoteOn(70, 127),
                       NoteOn(73, 127),
                       NoteOn(77, 127)])

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send([NoteOff(70, 127),
                       NoteOff(73, 127),
                       NoteOff(77, 127)])

                      #Bb maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send([NoteOn(70, 127),
                       NoteOn(74, 127),
                       NoteOn(81, 127)])

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send([NoteOff(70, 127),
                       NoteOff(74, 127),
                       NoteOff(81, 127)])

                      #Bb min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send([NoteOn(70, 127),
                       NoteOn(73, 127),
                       NoteOn(80, 127)])

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send([NoteOff(70, 127),
                       NoteOff(73, 127),
                       NoteOff(80, 127)])

                     #Bb maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send([NoteOn(70, 127),
                       NoteOn(74, 127),
                       NoteOn(84, 127)])

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send([NoteOff(70, 127),
                       NoteOff(74, 127),
                       NoteOff(84, 127)])

                     #B min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send([NoteOn(70, 127),
                       NoteOn(73, 127),
                       NoteOn(84, 127)])

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send([NoteOff(70, 127),
                       NoteOff(73, 127),
                       NoteOff(84, 127)])


                    #BB half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        Bb = keys[10]
        @keybow.on_press(Bb)
        def press_handler(Bb):

            midi.send([NoteOn(70, 127),
                       NoteOn(76, 127),
                       NoteOn(80, 127)])

        @keybow.on_release(Bb)
        def release_handler(Bb):

            midi.send([NoteOff(70, 127),
                       NoteOff(76, 127),
                       NoteOff(80, 127)])

                      #B single notes
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send(NoteOn(71, 127))

        @keybow.on_release(B)
        def release_handler(B):

            midi.send(NoteOff(71, 0))
                      
                     #B major chord
    if keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send([NoteOn(71, 127),
                       NoteOn(75, 127),
                       NoteOn(78, 127)])

        @keybow.on_release(B)
        def release_handler(B):

            midi.send([NoteOff(71, 127),
                       NoteOff(75, 127),
                       NoteOff(78, 127)])

                      #B minor chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and not keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send([NoteOn(71, 127),
                       NoteOn(74, 127),
                       NoteOn(78, 127)])

        @keybow.on_release(B)
        def release_handler(B):

            midi.send([NoteOff(71, 127),
                       NoteOff(74, 127),
                       NoteOff(78, 127)])

                      #B maj7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send([NoteOn(71, 127),
                       NoteOn(75, 127),
                       NoteOn(82, 127)])

        @keybow.on_release(B)
        def release_handler(B):

            midi.send([NoteOff(71, 127),
                       NoteOff(75, 127),
                       NoteOff(82, 127)])

                      #Bb min7 chord
    if not keys[15].pressed and not keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send([NoteOn(71, 127),
                       NoteOn(74, 127),
                       NoteOn(81, 127)])

        @keybow.on_release(B)
        def release_handler(B):

            midi.send([NoteOff(71, 127),
                       NoteOff(74, 127),
                       NoteOff(81, 127)])

                     #B maj9 chord
    if keys[15].pressed and not keys[14].pressed \
    and keys[13].pressed and not keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send([NoteOn(71, 127),
                       NoteOn(75, 127),
                       NoteOn(85, 127)])

        @keybow.on_release(B)
        def release_handler(B):

            midi.send([NoteOff(71, 127),
                       NoteOff(75, 127),
                       NoteOff(85, 127)])

                     #B min9 chord
    if not keys[15].pressed and keys[14].pressed \
    and not keys[13].pressed and keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send([NoteOn(71, 127),
                       NoteOn(74, 127),
                       NoteOn(85, 127)])

        @keybow.on_release(B)
        def release_handler(B):

            midi.send([NoteOff(71, 127),
                       NoteOff(74, 127),
                       NoteOff(85, 127)])

                    #B half diminished chord
    if keys[15].pressed and keys[14].pressed \
    and keys[13].pressed and keys[12].pressed:
        B = keys[11]
        @keybow.on_press(B)
        def press_handler(B):

            midi.send([NoteOn(71, 127),
                       NoteOn(77, 127),
                       NoteOn(81, 127)])

        @keybow.on_release(B)
        def release_handler(B):

            midi.send([NoteOff(71, 127),
                       NoteOff(77, 127),
                       NoteOff(81, 127)])
