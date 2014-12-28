from django.contrib.auth.models import User
from  django.db.models.signals  import  post_save, pre_save 
from  django.dispatch  import  receiver 
from my_app.models import Msg

@receiver (pre_save, sender = User)
def pre_create(sender, **kwargs):
	kwargs["instance"].is_new = bool(not kwargs["instance"].id)

@receiver (post_save, sender = User)
def create(sender, **kwargs):
	if kwargs["instance"].is_new:
		msg = Msg(user=kwargs["instance"])
		msg.save()