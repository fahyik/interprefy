from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from opentok import OpenTok, MediaModes, Roles
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import json, urllib2

from .models import *

# Create your views here.

#backend methods
def create_session(request):
	
	tbox = TokBox.objects.get(pk=1)
	opentok = OpenTok(tbox.api_key, tbox.api_secret)
	session = opentok.create_session(media_mode=MediaModes.routed)
	session_id = session.session_id
	return HttpResponse(session_id)

@login_required	
def gen_token(request, session_pk=None):
	# make curl to create session
# 	requrl = request.build_absolute_uri(reverse("tbox:create_session"))
# 	req = urllib2.Request(requrl)
# 	res = urllib2.urlopen(req)
# 	session_id = res.read()
	# GET has to pass the session_pk or passed from room view
	if request.method == "GET" or session_pk:
		res = {}
		if request.GET or session_pk:
			if request.GET:
				session = Session.objects.get(pk=request.GET["session_pk"])
			else:
				session = Session.objects.get(pk=session_pk)
				
			session_id = session.session_id
			print "token request for session and session id:"
			print session, session_id
			tbox = TokBox.objects.get(pk=1)
			opentok = OpenTok(tbox.api_key, tbox.api_secret)
			
			#set token parameters: role and data
			print "request by user:"
			print request.user.username
			userprofile = UserProfile.objects.get(username=request.user.username)
			params = { "role": None,
				"data": "name="+request.user.username }
			
			if userprofile.function == "Mod":
				params["role"] = Roles.moderator
			elif userprofile.function == "Pub":
				params["role"] = Roles.publisher
			elif userprofile.function == "Sub":
				params["role"] = Roles.subscriber
				
			token = opentok.generate_token(session_id, **params)
			print token
			res["token"] = token
			res["success"] = {"status": True, "error": None,}
			if request.GET:
				return HttpResponse(json.dumps(res))
			else:
				return json.dumps(res)
		else:
			res["success"] = {"status": False, "error": "no GET data",}
			return HttpResponse(json.dumps(res))
			
	elif request.method == "POST":
		# need to update session table with connection count
		# need to update connection table with connection id and data
		# will be done through ajax post/tokbox js on room view
		pass

#frontend methods
def home(request):
	return render(request, "tbox/home.html", {})

@login_required
def call_center(request):
	session_list = Session.objects.all()
	for each in session_list:
		each.lang = each.get_language_display()
	
	return render(request, "tbox/callcenter.html", {"session_list": session_list})

@login_required
def room(request, session_name):
	tbox = TokBox.objects.get(pk=1)
	session = Session.objects.get(name_id=session_name)
	#generate token, pass into context
	token = json.loads(gen_token(request, session.pk))["token"]
	
	context = { "session": session,
		"token": token,
		"api_key": tbox.api_key,
	}
	
	if request.user.is_authenticated():
		context["userprofile"] = UserProfile.objects.get(username=request.user.username)
	
	return render(request, "tbox/room.html", context)
	