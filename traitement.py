import pynmea2

file = open('gps_data_nmea.txt', encoding='utf-8')

list_GGA = []
list_RMC = []

for line in file.readlines():
    try:
        msg = pynmea2.parse(line)
        if msg.sentence_type == 'GGA':
            list_GGA.append(msg)
        if msg.sentence_type == 'RMC':
            list_RMC.append(msg)
        print(repr(msg))
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue

