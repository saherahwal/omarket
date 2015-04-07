$(document).ready(function() {
	
	$("#newCategoryPar").hide();
	
	$("#addCatButton").click( function() {		
		
		var addingNew = $("#addCatIcon").hasClass("fa-plus-square");
		
		if (addingNew) { // adding new
		
			$("#newCategoryPar").show();
			$("#addCatIcon").removeClass("fa-plus-square");
			$("#addCatIcon").addClass("fa-minus-square");
			
		} else { // cancel 
		
			$("#newCategoryPar").hide();
			$("#addCatIcon").addClass("fa-plus-square");
			$("#addCatIcon").removeClass("fa-minus-square");
			
			//
			// need to empty the field
			//
			$("#id_newCategory").val("");
		}
		
	});	
	
	
});