from django.shortcuts import render
from django.http import HttpResponse

from displays.displays import Displays
from feeds.feeds import Feeds
from members.members import Members
from pools.pools import Pools

# Create your views here.
# home 
def index(request):
    return render(request, 'sportspools/poolsIndex.html', {'Sports Pools By Drew': 2017})

#nhl
def nhl(request):
    sport_id = 1
    url = "nhl"
    f, d = Feeds(), Displays()
    api = f.FGetAPI(sport_id, url, False)
    context = {
	'feed': api,
	'page_name': 'NHL 2017-2018',
	'sport_id': sport_id,
    }
    print(context)
    return render(request, 'sportspools/poolsAPI.html', context)

# nba
def nba(request):
    sport_id = 2
    url = "nba"
    f, d = Feeds(), Displays()
    api = f.FGetAPI(sport_id, url, False)
    context = {
        'feed': api,
        'page_name': 'NBA 2017-2018',
        'sport_id': sport_id,
    }
    print(context)
    return render(request, 'sportspools/poolsAPI.html', context)
