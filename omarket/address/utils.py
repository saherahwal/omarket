from address.models import Country, City

ADDRESS_MAX_LENGTH = 500
MAX_CITYNAME_LENGTH=93
MAX_ZIPCODE_LENGTH=5

#
# US States hardcoded
#
#TODO: consider making this a hashtable instead of list
STATES_US_CHOICES = [(1, 'AL'), (2, 'AK'), (3, 'AZ'), (4, 'AR'), (5, 'CA'),
                     (6, 'CO'), (7, 'CT'), (8, 'DE'), (9, 'FL'), (10, 'GA'),
                     (11, 'HI'), (12, 'ID'), (13, 'IL'), (14, 'IN'), (15, 'IA'),
                     (16, 'KS'), (17, 'KY'), (18, 'LA'), (19, 'ME'), (20, 'MD'),
                     (21, 'MA'), (22, 'MI'), (23, 'MN'), (24, 'MS'), (25, 'MO'),
                     (26, 'MT'), (27, 'NE'), (28, 'NV'), (29, 'NH'), (30, 'NJ'),
                     (31, 'NM'), (32, 'NY'), (33, 'NC'), (34, 'ND'), (35, 'OH'),
                     (36, 'OK'), (37, 'OR'), (38, 'PA'), (39, 'RI'), (40, 'SC'),
                     (41, 'SD'), (42, 'TN'), (43, 'TX'), (44, 'UT'), (45, 'VT'),
                     (46, 'VA'), (47, 'WA'), (48, 'WV'), (49, 'WI'), (50, 'WY')]  


#
# Helper Functions
#
def getCountryCodeCountryTuples():
    """
        return a list of 2-tuples of country-id and country_name
    """
    countryQuerySet = Country.objects.all().order_by('country_name')
    listRes = []
    for q in countryQuerySet:
        tupRes = ( q.id, q.country_name)
        listRes.append( tupRes)
    return listRes

def getStateFromId(idNum):
    try:
        for s in STATES_US_CHOICES:
            if( s[0] == int(idNum) ):
                print "state returned", s[1]
                return s[1]
    except:
        print 'idNum=', idNum
        # DO return default
        # most likely country with no States (non-US)
        return ''
