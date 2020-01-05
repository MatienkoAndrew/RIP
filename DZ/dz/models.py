from django.db import models
from django.conf import settings
from django.utils import timezone
#from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Service(models.Model):
	worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	author = models.CharField(max_length=100, default='')
	title = models.CharField(max_length=200)
	text = models.TextField()
	price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to='image', null=True, blank=True)

	def	publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
