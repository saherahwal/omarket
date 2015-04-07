function format ( d ) {
    return 'Full name: '+d.first_name+' '+d.last_name+'<br>'+
        'Salary: '+d.salary+'<br>'+
        'The child row can contain any data you wish, including links, images, inner tables etc.';
}

var test;

$(document).ready(function() {
	
	// Array to track the ids of the details displayed rows
    var detailRows = [];
	
	//
	// orders data table
	//
	/*
	var dt = $('#ordersTable').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": "scripts/ids-objects.php",
        "columns": [
            {
                "class":          "details-control",
                "orderable":      false,
                "data":           null,
                "defaultContent": ""
            },
            { "data": "first_name" },
            { "data": "last_name" },
            { "data": "position" },
            { "data": "office" }
        ],
        "order": [[1, 'asc']]
    } ); */
 
	var dt = $('#ordersTable').DataTable();	
	
    $('#ordersTable tbody').on( 'click', 'tr td:first-child', function () {
        var tr = $(this).closest('tr');
		var icon = $(this).closest('td').children('i');
        var row = dt.row( tr );
        var idx = $.inArray( tr.attr('id'), detailRows );		
		
		test = icon;
		
        if ( row.child.isShown() ) {
            tr.removeClass( 'details' );	
			
			// icon hide and show
			icon.removeClass( 'fa-minus-square' );			
			icon.addClass( 'fa-plus-square' );	
			
            row.child.hide();
 
            // Remove from the 'open' array
            detailRows.splice( idx, 1 );
        }
        else {
            tr.addClass( 'details' );
			
			// icon hide and show
			icon.removeClass( 'fa-plus-square' );			
			icon.addClass( 'fa-minus-square' );		
			
			// add row
            row.child( format( row.data() ) ).show();
 
            // Add to the 'open' array
            if ( idx === -1 ) {
                detailRows.push( tr.attr('id') );
            }
        }
    } );
});