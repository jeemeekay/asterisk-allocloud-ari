#!/usr/bin/python2

import ari
import logging
import time

logging.basicConfig()
client = ari.connect('http://localhost:8088/', 'allocloud', 'Pa$$w0rd')

def on_dtmf(channel, event):
    digit = event['digit']
    if digit == '#':
        channel.play(media='sound:goodbye')
        channel.continueInDialplan()
    elif digit == '*':
        channel.play(media='sound:asterisk-friend')
    else:
        channel.play(media='sound:digits/%s' % digit)


def on_start(channel_obj, event):    
    channel = channel_obj.get('channel')
    channel.answer()
    for digit in event['channel']['dialplan']['exten']:
        time.sleep(1.5)
        print "playing: ",digit
        channel.play(media='number:'+digit)
    
    time.sleep(2)
    channel.hangup()


client.on_channel_event('StasisStart', on_start)
client.run(apps="hello")
