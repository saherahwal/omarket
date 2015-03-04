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
		
		//
		// Function Defs 
		//
		
		//
		// Fill city options 
		//
		/*
		var getCities = function() {
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
						// remove all options
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
		} */
		
		var getCities = function() {
			var cities = [];
			$.ajax({
					url: "/address/cities/",					
					datatype: "json",
					type: "POST",					
					data: {  
							value: $("#id_countrySignup").val(),
							text : $("#id_countrySignup option:selected").text(),
						  },
				 }).done(function(data) {					
				     cities = data					 
					 $( "#id_citySignup").autocomplete({
						source: cities
					 });
				 });			
		}
		
		var showUSRelated = function(){
			//
			// Show State list if United States is chosen
			//			
			var country_sel = $( "#id_countrySignup option:selected" ).text();
			if (country_sel === "United States"){				
				$("#cityChoice").after(stateChoice);
				$("#stateChoice").after(zipCode)
			}else{				
				$("#stateChoice").detach();
				$("#zipCodePar").detach();
			}
		}
		
		var getPhoneCodes = function(){
			$.ajax({
					url: "/address/phoneCode/",					
					datatype: "json",
					type: "POST",					
					data: {  
							value: $("#id_countrySignup").val(),
							text : $("#id_countrySignup option:selected").text(),
						  },
				 }).done(function(data) {						
						
						//
						// add country code text 
						//
						$("#id_mobileNumberSignup").val("+" + data['phone_code']);
						
				 });
		}		
		
		
		//
		// keep copy of stateChoice dropdown and zipcode field
		// then detach :)
		//	
        var stateChoice = $("#stateChoice");
		var zipCode = $("#zipCodePar");		
		$("#stateChoice").detach();	
		$("#zipCodePar").detach();		
		
		//
		// Show or hide State list
		// get phone code per country chosen
		//
		showUSRelated();	
	    getPhoneCodes();				
		
       
		$( "#id_countrySignup" ).on( 'click', function() {	 
			getCities();
			showUSRelated();
			getPhoneCodes();
		});

			
		$( "#id_countrySignup" ).on( 'change', function() {	  
			getCities();
			showUSRelated();	
			getPhoneCodes();
		});		

});