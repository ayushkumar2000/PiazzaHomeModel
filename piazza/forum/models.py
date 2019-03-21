from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime, timezone
# Create your models here.
class thread(models.Model):
    value=models.TextField(max_length=5000)
    subject=models.CharField(max_length=5000)
    author=models.CharField(max_length=100)
    created = models.DateTimeField()
    filetype=models.CharField(max_length=100)
    author_type = models.IntegerField()
    def __str__ (self):
        return self.value+'-'+self.author
    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'thread_id': self.pk})
    def timesec(self):
        now = datetime.now(timezone.utc)
        return((now-self.created).seconds)
    def timedays(self):
        now = datetime.now(timezone.utc)
        return((now-self.created).days)
    def timeminutes(self):
        now = datetime.now(timezone.utc)
        return(int(((((now-self.created).seconds%3600)))/60))
    def timehour(self):
        now = datetime.now(timezone.utc)
        return(int(((now-self.created).seconds/3600)))
class comment(models.Model):
    Thread=models.ForeignKey(thread,on_delete=models.CASCADE)
    filetype=models.CharField(max_length=100)
    comment=models.TextField(max_length=1000)
    
    author=models.CharField(max_length=100)
    author_type = models.IntegerField()
    def __str__ (self):
        return str(self.Thread) + '-' + self.comment
         