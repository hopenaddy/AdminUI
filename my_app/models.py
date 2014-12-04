from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User, related_name="profile")
	ava = models.CharField(max_length="30")
	token = models.CharField(max_length="30")
	class Meta:
		verbose_name = 'Profiles'
		verbose_name_plural = 'Profile'	
	def __unicode__(self):
		return self.user.get_full_name()

class Msg(models.Model):
	profile = models.ForeignKey(Profile, related_name="msg")
	total_msg_counter = models.IntegerField(default=0)
	success_msg_counter = models.IntegerField(default=0)
	failed_msg_counter = models.IntegerField(default=0)
	class Meta:
		verbose_name = 'Messages'
		verbose_name_plural = 'Message'	




