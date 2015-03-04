$(function() {

    Morris.Line({
        element: 'morris-line-orders',
        data: [{
            period: '2015 W0',
            orders: 2666,
            customers: null,
            subscribers: 2647
        }, {
            period: '2015 W1',
            orders: 2778,
            customers: 2294,
            subscribers: 2441
        }, {
            period: '2015 W2',
            orders: 4912,
            customers: 1969,
            subscribers: 2501
        }, {
            period: '2015 W3',
            orders: 3767,
            customers: 3597,
            subscribers: 5689
        }, {
            period: '2015 W4',
            orders: 6810,
            customers: 1914,
            subscribers: 2293
        }, {
            period: '2015 W5',
            orders: 5670,
            customers: 4293,
            subscribers: 1881
        }, {
            period: '2015 W6',
            orders: 4820,
            customers: 3795,
            subscribers: 1588
        }, {
            period: '2015 W7',
            orders: 15073,
            customers: 5967,
            subscribers: 5175
        }, {
            period: '2015 W8',
            orders: 10687,
            customers: 4460,
            subscribers: 2028
        }, {
            period: '2015 W9',
            orders: 8432,
            customers: 5713,
            subscribers: 1791
        }],
        xkey: 'period',
        ykeys: ['orders', 'customers', 'subscribers'],
        labels: ['orders', 'customers', 'subscribers'],
		lineColors: ['#428bca', '#d9534f', '#f0ad4e'],
        pointSize: 4,
        hideHover: 'auto',
        resize: true
    });
    
	/*
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Download Sales",
            value: 12
        }, {
            label: "In-Store Sales",
            value: 30
        }, {
            label: "Mail-Order Sales",
            value: 20
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '2006',
            a: 100,
            b: 90
        }, {
            y: '2007',
            a: 75,
            b: 65
        }, {
            y: '2008',
            a: 50,
            b: 40
        }, {
            y: '2009',
            a: 75,
            b: 65
        }, {
            y: '2010',
            a: 50,
            b: 40
        }, {
            y: '2011',
            a: 75,
            b: 65
        }, {
            y: '2012',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });
	*/

});
