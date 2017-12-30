from django.db import models

from operator import itemgetter

from ..models import PoolColumn
from ..members.members import Members
from ..pools.pools import Pools

class Displays(models.Model):
    def DBuildPools(self, sport_id, f):
        p, m, members = Pools(), Members(), {}
        for member in m.getMembers(sport_id):
            d = { 't':0, 'n':member.name, 'd':[] }
            t = m.getMemberTeams(member.id, sport_id)
            for mt in t:
                cols = p.getTeamColumn(mt.id)
                for col in cols:
                    c = col.name
                d['d'].append((c, mt.name, f[mt.name]))
                d['t'] += f[mt.name]
            k = str(d['t'])+'_'+str(member.id)
            members[k] = d
            members[k]['d'] = sorted(members[k]['d'], key=itemgetter(0))
        members = members.items()
        pc = PoolColumn.objects.filter(sport_id=1).order_by('name')
        return { 
	    'pmembers':m.getMembers(sport_id), 
	    'members':sorted(members, key=itemgetter(0), reverse=True), 
	    'pcolumns':pc 
	}
        
        
