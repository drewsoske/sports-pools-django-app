from django.db import models

from ..models import Member
from ..models import MemberTeam

class Members(models.Model):
    def getMembers(self, sport_id):
        pool_members = Member.objects.filter(sport_id=sport_id).order_by('name')
        return pool_members

    def getMemberTeams(self, member_id, sport_id):
        #pool_member_teams = MemberTeam.objects.values('team_id_id').filter(member_id=member_id)
        pool_member_teams = MemberTeam.objects.raw("SELECT t.name, t.id FROM sportspools_memberteam AS m JOIN sportspools_team AS t ON m.team_id_id = t.id AND t.sport_id = %s WHERE m.member_id_id = %s",[sport_id, member_id])
        return pool_member_teams

    def getMemberTeamColumn(self, member_id, sport_id, column_id):
	pool_member_teams = MemberTeam.objects.raw("SELECT t.name, t.id FROM sportspools_memberteam AS m JOIN sportspools_team AS t ON m.team_id_id = t.id AND t.sport_id = %s AND t.name = %s WHERE m.member_id_id = %s",[sport_id, column_id, member_id])
	return pool_member_teams
