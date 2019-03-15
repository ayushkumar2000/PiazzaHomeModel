from django.db import models
from django.core.urlresolvers import reverse 
# Create your models here.
class thread(models.Model):
    value=models.CharField(max_length=5000)
    subject=models.CharField(max_length=5000)
    author=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    filetype=models.CharField(max_length=100)

    def __str__ (self):
        return self.value+'-'+self.author
    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'thread_id': self.pk})

class comment(models.Model):
    Thread=models.ForeignKey(thread,on_delete=models.CASCADE)
    filetype=models.CharField(max_length=100)
    comment=models.CharField(max_length=1000)

    def __str__ (self):
        return str(self.Thread) + '-' + self.comment
         