from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TokBox(models.Model):
	api_key = models.CharField(max_length=8)
	api_secret = models.CharField(max_length=40)
	
class Session(models.Model):
	TYPE_CHOICES = (
		("A", "Admin Room"),
		("B", "Broadcast Room"),
	)
	
	LANG_CHOICES = (
		("--", "Admin Room"),
		("AR", "Arabic"),
		("DA", "Danish"),
		("DE", "German"),
		("EL", "Greek"),
		("EN", "English"),
		("ES", "Spanish"),
		("FA", "Persian"),
		("FR", "French"),
		("HI", "Hindi"),
		("IT", "Italian"),
		("PT", "Portuguese"),
		("RU", "Russian"),
		("SV", "Swedish"),
		("ZH", "Chinese"),	
	)
	
	# name should be similar for same conference
	name = models.CharField(max_length=50)
	# name id identifies the type of room and language, i.e.: admin_nameofroom_LN
	name_id = models.CharField(max_length=50, null=True, editable=False)
	# no. of connections
	conn_count = models.IntegerField(default=0)
	session_id = models.CharField(max_length=72, unique=True)
	type = models.CharField(max_length=1, choices=TYPE_CHOICES)
	language = models.CharField(max_length=2, choices=LANG_CHOICES) # two capital letters, -- for admin
	
	def __unicode__(self):
		return self.name_id

	def save(self, *args, **kwargs):
		if self.type == "A":
			self.name_id = "admin_" + self.name
		elif self.type == "B":
			self.name_id = "bcast_" + self.name
			
		self.name_id = self.name_id + "_" + self.language
		super(Session, self).save(*args, **kwargs)

class Connection(models.Model):
	session = models.ForeignKey(Session)
	user = models.ForeignKey(User)
	
	conn_id = models.CharField(max_length=255)
	conn_user = models.CharField(max_length=50)
		
	def save(self, *args, **kwargs):
		self.conn_user = self.user.username
		super(Connection, self).save(*args, **kwargs)

class UserProfile(models.Model):
	FUNCTION_CHOICES = (
		("Pub", "Publisher"),
		("Sub", "Subscriber"),
		("Mod", "Moderator"),
	)
	
	user = models.OneToOneField(User)
	
	username = models.CharField(max_length=50, editable=False)
	function = models.CharField(max_length=3, choices=FUNCTION_CHOICES)
	
	def save(self, *args, **kwargs):
		self.username = self.user.username
		super(UserProfile, self).save(*args, **kwargs)