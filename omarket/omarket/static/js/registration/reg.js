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
				
		$( "#id_countrySignup" ).on( 'change', function() {		  
		  $.ajax({
					url: "/address/cities/",					
					datatype: "json",
					type: "POST",					
					data: {  
							value: $("#id_countrySignup").val(),
							text : $( "#id_countrySignup option:selected" ).text(),
						  },
				 }).done(function(data) {						
						//
						//remove all options
						//
						$("#id_citySignup").find('option').remove();
						
						//
						// add new options
						//
						for(var key in data) {							
							var option = new Option(data[key], key);
							$("#id_citySignup").append($(option));
						}						
						
						
				 });
		});

		
});