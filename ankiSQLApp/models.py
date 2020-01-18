from django.db import models
from django.utils import timezone

class ankidb(models.Model):
    Database_Memorized = models.BooleanField(default=False)
    time_date = models.DateTimeField(default=timezone.now)
    database_loci = models.CharField(max_length=30)
    domain_theme = models.CharField(max_length=30)
    primary_key = models.CharField(max_length=30)
    first_point_to_remember = models.CharField(max_length=300)
    second_point_to_remember = models.CharField(max_length=300)
    third_point_to_remember = models.CharField(max_length=300)
    fourth_point_to_remember = models.CharField(max_length=300)
    fiveth_point_to_remember = models.CharField(max_length=300)
    sixth_point_to_remember = models.CharField(max_length=300)
    seventh_point_to_remember = models.CharField(max_length=300)
    eighth_point_to_remember = models.CharField(max_length=300)

    def __str__(self):
        return "%s %s"%(self.primary_key, self.Database_Memorized)
