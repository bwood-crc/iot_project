import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SM-S928W0266', 'brendan721')

# GET

import urequests
r = urequests.get("http://www.google.ca")
print(r.content)
r.close()

