from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    total_msg_counter = models.IntegerField(default=0)
    success_msg_counter = models.IntegerField(default=0)
    failed_msg_counter = models.IntegerField(default=0)