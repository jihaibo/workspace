from django.db import models
import datetime
#from django.contrib import admin
# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('dtae published')
	def __unicode__(self):
		return self.question
	def was_published_recntly(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
		
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.choice_text
#admin.site.register(Poll,Choice)