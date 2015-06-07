$(document).ready(function(){
		
		//
		// CSRF token protection 
		//
		var csrftoken = $.cookie('csrftoken');
				
		function csrfSafeMethod(method) {
			// these HTTP methods do not require CSRF protection
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		
		//
		// WARNING: every subsequent Ajax will use this
		// easy add of csrf token
		//
		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});		
		
		var subscribeBusiness = function (data) {			
			$.ajax({
					url: "/registration/subscribe/",					
					datatype: "json",
					type: "POST",					
					data: data,
				 }).done(function(data) {					
				     // capture the response
					 window.location = '/business/add';
				 });		
		}
		    
   
		$( "#veryBasicBusiness" ).on( 'click', function() {	 
			var data = { subChoice : 'veryBasic' };
			subscribeBusiness( data );
		});
				
		$( "#basicBusiness" ).on( 'click', function() {	 
			var data = { subChoice : 'basic' };
			subscribeBusiness( data );
		});
		
		$( "#proBusiness" ).on( 'click', function() {	 
			var data = { subChoice : 'pro' };
			subscribeBusiness( data );
		});
		
		$( "#premBusiness" ).on( 'click', function() {	 
			var data = { subChoice : 'prem' };
			subscribeBusiness( data );
		});
		
		$( "#freeCustomer" ).on( 'click', function() {	 
			var data = { subChoice : 'free' };
			subscribeBusiness( data );
		});			
		
});