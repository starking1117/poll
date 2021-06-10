from django.db import models

# Create your models here.
class Poll(models.Model):
    subject = models.CharField('投票主題',max_length=100)
    date_created = models.DateField(auto_now_add=True)
    desc = models.TextField('說明')

    def __str__(self):
        return "{}: {}".format(self.id, self.subject)

class Option(models.Model):
    poll_id = models.IntegerField()
    title = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "{}: {} {}".format(self.id, self.poll_id, self.title)
