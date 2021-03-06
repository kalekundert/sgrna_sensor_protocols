"""\
Below are the excitation and emission maxima for the 
fluorescent proteins used in this assay:

Fluorophore  Excitation  Emission  Reference
──────────────────────────────────────────────────
sfGFP               485       510  Pédelacq (2006)
mRFP                557       592  Campbell (2002)

Below are the laser settings I use on the Lim Lab BD 
LSRII:

Channel  Laser  Filter  Voltage  Threshold
───────────────────────────────────────────
FSC        488              400
SSC        488  488/10      250
GFP        488  530/30      600       5000
RFP        561  610/10      500        500

Below are the loader settings I use for the 96-well 
high-throughput samplers that the Lim and El-Samad 
Labs' BD LSRIIs are equipped with.  I organize my 
plates such that the odd columns contain just PBS 
("wash wells") and the even columns contain the cells 
I want to measure ("sample wells").  This is the only 
way I have found to keep the contamination between 
wells to negligible levels, and I start with a wash 
well in case the user before me didn't clean the 
machine.  I use different loader settings for the two 
types of wells:

Loader Setting     Wash wells  Sample wells
───────────────────────────────────────────
Flow rate          3.0 µL/sec    0.5 µL/sec
Sample volume           30 µL         60 µL
Mixing volume          100 µL        100 µL
Mixing speed       180 µL/sec    180 µL/sec
Num mixes                   2             2
Wash volume            800 µL        800 µL 

For wash wells, I use the highest flow rate possible 
to quickly flush the sample chamber.  For sample 
wells, I use the lowest flow rate possible because my 
cultures are usually pretty saturated, and I want to 
be as accurate as possible.  I use a relatively high 
sample volume because I want to be sure of recording 
10,000 events, even for cultures that didn't grow 
well for some reason (while still leaving enough to 
repeat a plate if necessary).  The two 100 μL mixes 
at 180 μL/sec are enough that I don't need to mix the 
cells when diluting them into PBS.  I use the highest 
possible wash volume, but it doesn't help anything as 
far as I can tell (that why I need wash wells).
"""



# vim: tw=53

