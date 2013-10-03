""" pip install pippi """

from pippi import dsp

def make_cycles(length):
    """ Well begun, half done """
    num_harmonics = dsp.randint(1, 6)
    val_harmonics = [1, 2, 3, dsp.randint(4, 7), dsp.randint(5, 9)]

    # Each collection of partials
    min_length = dsp.stf(10)
    max_length = dsp.stf(18)

    root = 40.0 # hz

    # Deviate
    root = root + dsp.rand()

    elapsed = 0
    cycles = []

    # Count off
    while elapsed < length:
        cycle_length = dsp.randint(min_length, max_length)

        harmonics = [ 
                dsp.tone(
                length=cycle_length, 
                freq=root * dsp.randchoose(val_harmonics), 
                amp=dsp.rand(0.1, 0.4),
                wavetype='impulse'
                ) 
            for h in range(num_harmonics) ]

        harmonics = [ dsp.pan(harmonic, dsp.rand()) for harmonic in harmonics ]
        harmonics = [ dsp.env(harmonic, 'gauss') for harmonic in harmonics ]

        cycles += [ dsp.mix(harmonics) ]
        elapsed += cycle_length

    return ''.join(cycles)

cycles = [ make_cycles(dsp.stf(60 * 2)) for i in range(4) ]

out = dsp.mix(cycles)
out = dsp.pine(out, dsp.stf(60 * 8), 80.0 * 2)

cycles = [ make_cycles(dsp.stf(60 * 8)) for i in range(4) ]
cycles = dsp.mix(cycles)

out = dsp.mix([ out, cycles ])

dsp.write(out, 'newly')
