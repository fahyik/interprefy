from django.contrib import admin
from .models import *
# Register your models here.

class SessionAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "language", "type", "name_id", "session_id", "conn_count")
	list_filter = ["name"]

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("username", "function")

admin.site.register(TokBox)
admin.site.register(Session, SessionAdmin)
admin.site.register(Connection)
admin.site.register(UserProfile, UserProfileAdmin)