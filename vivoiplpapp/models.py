from django.db import models



class Ipltask(models.Model):
    index=models.BigIntegerField(primary_key=True)
    Season = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=10)
    date = models.DateField(default = True)
    team1 = models.CharField(max_length=20)
    team2 = models.CharField(max_length=20)
    toss_winner = models.CharField(max_length=20)
    toss_decision = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    dl_applied = models.CharField(max_length=20)
    winner = models.CharField(max_length=20)
    win_by_runs = models.CharField(max_length=20)
    win_by_wickets = models.CharField(max_length=20)
    player_of_match = models.CharField(max_length=20)
    venue = models.CharField(max_length=20)
    umpire1 = models.CharField(max_length=20)
    umpire2 = models.CharField(max_length=20)
    umpire3 = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
