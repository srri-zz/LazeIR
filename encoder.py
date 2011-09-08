#By Steven Richards <sbrichards@mit.edu>
#Simple Tone Generator for Laser Rigging, demo only
import audiere
from sys import exit
print '\n\n\n\n'
tone = int(raw_input("Enter a frequency between 1-20000Hz (as a number): "))
device = audiere.open_device()
freq = device.create_tone(tone)
freq.play()
print '\n\n\n'
raw_input("Hit enter to stop")
freq.stop()
exit()

