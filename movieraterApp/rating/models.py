from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Vote(models.Model):
    user = models.ForeignKey(User)
    #movie = models.ForeignKey('Movie')
    name = models.CharField(max_length=200)
    rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Vote %d to %s by %s' % (self.rate, self.name, self.user)
		
		
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    average = models.FloatField(default=0)
    votes = models.ForeignKey(Vote, title = title)
	

    def calculate_rating(self):
        print(self.title)
        #print(self.votes)
        #votes = Vote.objects.filter(name = self.title)
        print(self.votes)
        #total_sum = 0
        #for vote in votes:
        #    total_sum += vote.rate
        #self.average = total_sum / len(votes)
        #self.average
        #self.save()
        #return self.average
		
    def __str__(self):
        return self.title
     
    #nr_votes = models.IntegerField(default=0)
    #votes_sum = models.IntegerField(default=0)    
    # author = models.ForeignKey(User)
    # image_url = models.URLField(null=True, blank=True)
    # trailer = models.CharField(max_length=200)
		
