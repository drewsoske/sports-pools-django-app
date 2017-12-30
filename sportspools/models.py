from django.db import models

# Create your models here.
SPORT_IDS = (
        (1, 'NHL'),
        (2, 'NBA'),
        (3, 'MLB'),
    )

# Member Model
class Member(models.Model):
    global SPORT_IDS

    sport_id = models.PositiveSmallIntegerField(
        max_length=2,
        choices=SPORT_IDS,
        default=1
    )
    email = models.CharField(
        max_length=200,
        null=True
    )
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name

    def sport_name(self):
        sport = filter(lambda x: self.sport_id in x, SPORT_IDS)
        return sport[0][1]

    def team_names(self, id):
        out = ''
        pcts = Team.objects.raw("SELECT t.id, t.name, p.column_id_id as column_id FROM sportspools_team t JOIN sportspools_memberteam mt ON t.id = mt.team_id_id AND mt.member_id_id = %s JOIN sportspools_poolcolumnteam p ON t.id = p.team_id_id AND p.column_id_id = %s",[self.id, id])
        for pct in pcts:
            if id == pct.column_id:
                out = pct.name + ', ' + out
        return out 

    def a(self):
        if self.team_names(1):
            return self.team_names(1)
        else:
            return self.team_names(6)
    
    def b(self):
        if self.team_names(2):
            return self.team_names(2)
        else:
            return self.team_names(7)
    
    def c(self):
        if self.team_names(3):
            return self.team_names(3)
        else:
            return self.team_names(8)
    
    def d(self):
        if self.team_names(4):
            return self.team_names(4)
        else:
            return self.team_names(9)
    
    def e(self):
        if self.team_names(5):
            return self.team_names(5)
        else:
            return self.team_names(10)


# Team Model
class Team(models.Model):
    global SPORT_IDS

    sport_id = models.PositiveSmallIntegerField(
        max_length=2,
        choices=SPORT_IDS,
        default=1,
    )
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def sport_name(self):
        sport = filter(lambda x: self.sport_id in x, SPORT_IDS)
        return sport[0][1]


# Member Team Model
class MemberTeam(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)


# Pool Column Model
class PoolColumn(models.Model):
    global SPORT_IDS

    sport_id = models.PositiveSmallIntegerField(
        max_length=2,
        choices=SPORT_IDS,
        default=1,
    )
    name = models.CharField(max_length=5)


# Pool Column Team Model
class PoolColumnTeam(models.Model):
    global SPORT_IDS

    sport_id = models.PositiveSmallIntegerField(
        max_length=2,
        choices=SPORT_IDS,
        default=1,
    )
    column_id = models.ForeignKey(PoolColumn, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)

