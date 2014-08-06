# Auth: mlr
# Date: 2013-04-26

import miss
from datetime import date
from lxml import html


class Site(miss.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.court_id = self.__module__

        # If it's the beginning of January, we need to make sure that we aren't
        # missing any late-coming cases from the previous year.
        today = date.today()
        self.url = 'http://courts.ms.gov/scripts/websiteX_cgi.exe/GetOpinion?Year=%s&Court=Supreme+Court&Submit=Submit' % today.year - 1
        beginning_of_year = (date(today.year, 1, 1) <= today <= date(today.year, 1, 15))
        if not beginning_of_year:
            # This simply aborts the crawler.
            self.status = 200
            self.html = html.fromstring('<html></html>')
