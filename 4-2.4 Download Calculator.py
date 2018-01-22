# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def convert_seconds(input):
    hours = int(input) / 60 / 60
    minutes = int(input) / 60 - (hours * 60)
    seconds = input - (minutes * 60) - (hours * 60 * 60)
    if hours != 1:
        hours = str(hours) + " hours, "
    else:
        hours = str(hours) + " hour, "
    if minutes != 1:
        minutes = str(minutes) + " minutes, "
    else:
        minutes = str(minutes) + " minute, "
    if seconds != 1:
        seconds = str(seconds) + " seconds"
    else:
        seconds = str(seconds) + " second"
    return hours + minutes + seconds

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]

def download_time(fs,fsu,bw,bwu):
    bits_mult = [['kb', 2.0 ** 10],['kB', 2.0 ** 10 * 8],
                 ['Mb', 2.0 ** 20],['MB', 2.0 ** 20 * 8],
                 ['Gb', 2.0 ** 30],['GB', 2.0 ** 30 * 8],
                 ['Tb', 2.0 ** 40],['TB', 2.0 ** 40 * 8]]
    fsu_mult = lookup(bits_mult, fsu)
#    print 'File Size Multiplier: ' + str(fsu_mult)
    bwu_mult = lookup(bits_mult, bwu)
#    print 'Bandwidth Multiplier: ' + str(bwu_mult)
    fs_bits = fs * fsu_mult
#    print 'File Size (Bits): ' + str(fs_bits)
    bw_bits = bw * bwu_mult
#    print 'Bandwidth (Bits): ' + str(bw_bits)
    time = fs_bits / bw_bits * 1.0
#    print 'Download Time: ' + str(time) + ' seconds'
    return convert_seconds(time)


#print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

#print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

#print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

#print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

#print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

#print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>> 0 hours, 37 minutes, 32.8 seconds

print download_time(1,'kB',3,'MB')
#>>> 0 hours, 0 minutes, 0.000325520833333 seconds
