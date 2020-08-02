# https://rhodesmill.org/skyfield/positions.html

from skyfield.api import EarthSatellite, Topos, load
from datetime import datetime
from datetime import timedelta
from pytz import timezone

# updates these values
western = timezone('US/Pacific')
san_francisco = Topos('37.7749 N', '122.4194 W')

ts = load.timescale()
t = ts.now()
current = western.localize(datetime.now())

# load the satellite dataset from Celestrak
# line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
# line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
starlink_url = "https://celestrak.com/NORAD/elements/starlink.txt"
starlinks = load.tle_file(starlink_url)
print ("Loaded", len(starlinks), "satellites")

# loop through satellites to find times when visible
for satellite in starlinks:

    # find events when satellite rises or sets in the next 2 hours
    t0 = ts.utc(current) 
    t1 = ts.utc(current + timedelta(hours=2))
    t, events = satellite.find_events(san_francisco, t0, t1, altitude_degrees=30.0)
    
    # see if satellite visible to a ground observer over the next 2 hours
    eph = load('de421.bsp')
    earth, venus = eph['earth'], eph['venus']
    two_hours = ts.utc(current, range(0, 120, 20))
    sunlit = satellite.at(two_hours).is_sunlit(eph)
    blocked = (earth + satellite).at(two_hours).observe(venus).apparent().is_behind_earth()

    for ti, event in zip(t, events):
        if (blocked) or (not sunlit):
            break
        # name = ('rise above 30°', 'culminate', 'set below 30°')[event]
        # print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)
        print('{}  {}'.format(
            ti.utc_strftime('%Y-%m-%d %H:%M'),
            satellite.name,
        ))