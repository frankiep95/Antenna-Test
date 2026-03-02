
def testGPS(instruments):
    for instrument in instruments:
        if instrument.is_connected():
            gps.setupGPS(instrument)

def testWiFi(instruments):
    for instrument in instruments:
        if instrument.is_connected():
            k.getWiFiConnections(instrument)