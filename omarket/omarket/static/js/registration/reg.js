$(document).ready(function(){
		
		// get countries list
		$.ajax({
			  type: "POST",
			  url: "/address/countries",
			  data: { name: "John", location: "Boston" }
			}).done(function( msg ) {
				// fill up the countries list
			});
});