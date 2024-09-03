# Imports go at the top
from microbit import *
import radio, music, time

radio.config(group=23)

speaker_on = False
speaker_buf = 0

set_volume(70)

def msg_rec():
    for i in range(0,3):
        display.set_pixel(4,0,9)
        time.sleep(.1)
        display.set_pixel(4,0,0)
        time.sleep(.1)
    
msg_text = ""

# Code in a 'while True:' loop repeats forever
while True:
    msg = radio.receive()
    
    # Radio ON
    if speaker_on == True and speaker_buf < 1:
        speaker.on
        music.play(music.BA_DING)
        speaker_buf += 1
        display.set_pixel(0,0,9)

    # Radio OFF
    if speaker_on == False and speaker_buf == 1:
        speaker.off
        speaker_buf = 0
        display.set_pixel(0,0,0)
    

    # Radio Toggle
    if button_b.was_pressed():
        speaker_on = not speaker_on

    # Read Message
    if pin_logo.is_touched():
        display.scroll(msg_text)

    # Write Message
    if button_a.was_pressed():
        radio.send(input('>>>   '))
        
    # New Message
    if msg:
        msg_rec()
        msg_text = msg
        print('<<<   ' + msg_text)
        music.play(music.BA_DING)
