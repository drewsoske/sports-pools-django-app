from django.db import models

import re
import requests
import simplejson as json
import string
import sys
import unicodedata

class Feeds(models.Model):
    key = 'register for a key with me'
    authkey = None

    def FAuth(self, sport_id):
        # url
        url = "http://apsapi.drewsoske.com/api/auth"
        if self.authkey is None:
            r = requests.post(url, data={'key': self.key})
            self.authkey = r.text
        return self.authkey

    def FGetAPI(self, sport_id, url, test=False, build='json'):
        # url
        nbaurl = "http://apsapi.drewsoske.com/nba/build/%s/all" % (build,)
        nhlurl = "http://apsapi.drewsoske.com/nhl/build/%s/all" % (build,)

        url = nbaurl if sport_id == 2 else nhlurl
        token = self.FAuth(sport_id)
        r = requests.get(url, stream=True, data={'key': self.key, 'token': token[1:-2]})
	d = json.loads(r.text)
        if test == True:
            return r.status_code
        return json.loads(r.text)
