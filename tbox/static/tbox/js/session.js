// define options for connected users
var subscribe_options = { 
	insertMode: 'append',
	subscribeToAudio:true, 
	subscribeToVideo:true,
	width: "100%",
	height: 200,
};

var publish_options = { 
	publishVideo: true,
	width: "100%",
	height: 200,
};

$(document).ready(function(){

	// initialise session
	var session = OT.initSession(api_key, session_id)
	session.on({
		// subscribe to all currently available streams
		streamCreated: function(event) { 
			session.subscribe(event.stream, 'subVid', subscribe_options); 
		},
		
		connectionCreated: function (event) {
			console.log("connection created");
		},
		
		connectionDestroyed: function (event) {
			console.log("connection destroyed");
		},
		
		sessionDisconnected: function sessionDisconnectHandler(event) {
			// The event is defined by the SessionDisconnectEvent class
			console.log("Disconnected from the session.");
			$( ".myVidBox" ).append( "<div id='myVid'></div>" );
			if (event.reason == "networkDisconnected") {
				alert("Your network connection terminated.")
			}
		}
	});
	
	if (user_function == "Pub" || user_function == "Mod") {
		//event listener for incoming chat
		session.on('signal:chat', function(event) {
			msg = document.createElement('p');
			msg.innerHTML += event.data;
			msg.className = event.from.connectionId === session.connection.connectionId ? 'mine' : 'theirs';
			document.querySelector('#chat-history').appendChild(msg);
			//msg.scrollIntoView();
			var myDiv = $("#chat-history");
			myDiv.animate({ scrollTop: myDiv.prop("scrollHeight") - myDiv.height() }, 1);
		});
		
		//event listener for outgoing chat
		document.querySelector('#form-chattext').addEventListener('submit', function(event) {
				event.preventDefault();

				session.signal({
					type: 'chat',
					data: username + ": " + msgTxt.value
				}, function(error) {
					if (!error) {
						msgTxt.value = '';
					}
				});
		});
	}
	
	$("#start-video").click(function(){
	
	
		session.connect(token, function(error) {
			if (error) {
				console.log(error.message);
			} 
			else {
				publisher = OT.initPublisher('myVid', publish_options);
				session.publish(publisher, function(error) {
					if (error) {
						console.log(error);
					} else {
						console.log('Publishing a stream.');
						$("#main-content").removeClass("hidden");
						$("#disconnect").removeAttr('disabled');
						$("#start-subscribe").attr('disabled', 'disabled');
						$("#start-voice").attr('disabled', 'disabled');
						$("#start-video").attr('disabled', 'disabled');	
					}
				});
		
			}
		});
	});
	
	$("#start-voice").click(function(){
		
		session.connect(token, function(error) {
			if (error) {
				console.log(error.message);
			} 
			else {
				publish_options.publishVideo = false;
				publisher = OT.initPublisher('myVid', publish_options);
				session.publish(publisher, function(error) {
					if (error) {
						console.log(error);
					} else {
						console.log('Publishing a stream (voice-only).');
						$("#main-content").removeClass("hidden");
						$("#disconnect").removeAttr('disabled');
						$("#start-subscribe").attr('disabled', 'disabled');
						$("#start-voice").attr('disabled', 'disabled');
						$("#start-video").attr('disabled', 'disabled');	
					}
				});
		
			}
		});
	});
	
	$("#start-subscribe").click(function(){
		
		session.connect(token, function(error) {
			if (error) {
				console.log(error.message);
			} 
			else {
				console.log("Subscribe only");
				$("#main-content").removeClass("hidden");
				$("#disconnect").removeAttr('disabled');
				$("#start-subscribe").attr('disabled', 'disabled');
				$("#start-voice").attr('disabled', 'disabled');
				$("#start-video").attr('disabled', 'disabled');		
			}
		});
	});
	
	//disconnect
	$("#disconnect").click(function(){
		session.disconnect();
		$(this).attr('disabled', 'disabled');
		$("#start-voice").removeAttr('disabled');
		$("#start-subscribe").removeAttr('disabled');
		$("#start-video").removeAttr('disabled');
		$("#main-content").addClass("hidden");
	});
	
});
