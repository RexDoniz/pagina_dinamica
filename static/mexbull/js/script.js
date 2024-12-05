/*jshint jquery:true */

$(document).ready(function($) {
	"use strict";

	/* global google, DevSolutionSkill: false */
	/*jshint -W018 */
	
	/*-------------------------------------------------*/
	/* =  portfolio isotope
	/*-------------------------------------------------*/

	var winDow = $(window);
		// Needed variables
		var $container=$('.iso-call');
		var $filter=$('.filter');

		try{
			$container.imagesLoaded( function(){
				$container.trigger('resize');
				$container.isotope({
					filter:'*',
					layoutMode:'masonry',
					animationOptions:{
						duration:750,
						easing:'linear'
					}
				});

				setTimeout(Resize, 1500);
			});
		} catch(err) {
		}

		winDow.on('resize', function(){
			var selector = $filter.find('a.active').attr('data-filter');

			try {
				$container.isotope({ 
					filter	: selector,
					animationOptions: {
						duration: 750,
						easing	: 'linear',
						queue	: false,
					}
				});
			} catch(err) {
			}
			return false;
		});
		
		// Isotope Filter 
		$filter.find('a').on('click', function(){
			var selector = $(this).attr('data-filter');

			try {
				$container.isotope({ 
					filter	: selector,
					animationOptions: {
						duration: 750,
						easing	: 'linear',
						queue	: false,
					}
				});
			} catch(err) {

			}
			return false;
		});


	var filterItemA	= $('.filter li a');

		filterItemA.on('click', function(){
			var $this = $(this);
			if ( !$this.hasClass('active')) {
				filterItemA.removeClass('active');
				$this.addClass('active');
			}
		});

	/*-------------------------------------------------*/
	/* = datepicker
	/*-------------------------------------------------*/

	try{

		$( "#date" ).datepicker();

	} catch(err) {
	}
	
	/*-------------------------------------------------*/
	/* =  OWL carousell
	/*-------------------------------------------------*/
	try {
		var owlWrap = $('.owl-wrapper');

		if (owlWrap.length > 0) {

			if (jQuery().owlCarousel) {
				owlWrap.each(function(){

					var carousel= $(this).find('.owl-carousel'),
						dataNum = $(this).find('.owl-carousel').attr('data-num'),
						dataNum2,
						dataNum3;

					if ( dataNum == 1 ) {
						dataNum2 = 1;
						dataNum3 = 1;
					} else if ( dataNum == 2 ) {
						dataNum2 = 2;
						dataNum3 = dataNum - 1;
					} else {
						dataNum2 = dataNum - 1;
						dataNum3 = dataNum - 2;
					}

					carousel.owlCarousel({
						autoPlay: 10000,
						navigation : true,
						items : dataNum,
						itemsDesktop : [1199,dataNum2],
						itemsDesktopSmall : [991,dataNum3],
						itemsTablet : [768, dataNum3],
					});

				});
			}
		}

	} catch(err) {

	}
	
	/* ---------------------------------------------------------------------- */
	/*	Contact Map
	/* ---------------------------------------------------------------------- */

	try {
		var fenway = [42.345573,-71.098326]; //Change a map coordinate here!
		var markerPosition = [42.345573,-71.098326]; //Change a map marker here!
		var markerPosition2 = [42.3342802,-71.1324866]; //Change a map marker here!
		var markerPosition3 = [42.3388483,-71.0607322]; //Change a map marker here!
		$('.map')
			.gmap3({
				center: fenway,
				zoom: 13,
				mapTypeId : google.maps.MapTypeId.ROADMAP
			})
			.marker({
				position: markerPosition,
				icon: 'images/marker.png'
			})
			.marker({
				position: markerPosition2,
				icon: 'images/marker.png'
			})
			.marker({
				position: markerPosition3,
				icon: 'images/marker.png'
			});
	} catch(err) {

	}

	/*-------------------------------------------------*/
	/* =  flexslider
	/*-------------------------------------------------*/

	try {

		var SliderPost = $('.flexslider');

		SliderPost.flexslider({
			animation: "slide",
			customDirectionNav: $(".custom-navigation a")
		});
	} catch(err) {

	}

	/*-------------------------------------------------*/
	/* =  shopping cart subtotals, product increase, 
	/* =  decrease, delete item, dropdown remove item from 
	/* =  shopping cart
	/*-------------------------------------------------*/
	
	var totalPrice = $('.total-price');
	var ShippingPrice = $('.shipping-price').text();
	var PriceAfterShipping = $('.total-price-withshipping');

	PriceSum();

	function PriceSum() {

		var sum = 0;

		$('.tot-price').each(function(){
			sum += parseFloat($(this).text());
		});

		totalPrice.text(parseFloat(sum, 10).toFixed(2));

		if ($.isNumeric(ShippingPrice)) {
			PriceAfterShipping.text(parseFloat(parseFloat(sum, 10) + parseFloat(ShippingPrice, 10), 10).toFixed(2));
		} else {
			PriceAfterShipping.text(parseFloat(sum, 10).toFixed(2));
		}
	}


	var btnIncrease = $('button.increase'),
		btnDecrease = $('button.decrease'),
		DeleteButton = $('a.remove-item');

		btnIncrease.on('click', function(){
			var fieldNum = $(this).parent('.quantity-add').find('input[type="text"]');
			var fieldVal = fieldNum.val();
			var nextVal = parseFloat(fieldVal) + 1;
			fieldNum.val(nextVal);
			var itemPrice = $(this).parents('tr').find('span.stat-price').text();
			var totPrice = $(this).parents('tr').find('span.tot-price');
			var newPrice = parseFloat(parseFloat(itemPrice, 10) * parseFloat(fieldNum.val(), 10), 10).toFixed(2);
			totPrice.text(newPrice);

			PriceSum();
		});

		btnDecrease.on('click', function(){
			var fieldNum = $(this).parent('.quantity-add').find('input[type="text"]');
			var fieldVal = fieldNum.val();
			var nextVal = parseFloat(fieldVal) - 1;
			if (fieldVal > 0) {
				fieldNum.val(nextVal);
				var itemPrice = $(this).parents('tr').find('span.stat-price').text();
				var totPrice = $(this).parents('tr').find('span.tot-price');
				var newPrice = parseFloat(parseFloat(itemPrice, 10) * parseFloat(fieldNum.val(), 10), 10).toFixed(2);
				totPrice.text(newPrice);
			} else {
				fieldNum.val(0);
			}

			PriceSum();
		});

		DeleteButton.on('click', function(event) {
			event.preventDefault();

			$(this).closest('tr').remove();

			PriceSum();
		});

	var removeItemShop = $('a.delete-art');

	removeItemShop.on('click', function(event) {
		event.preventDefault();
		$(this).closest('li').remove();
	});

	/*-------------------------------------------------*/
	/* =  count increment
	/*-------------------------------------------------*/

	$('.skills-box').appear(function() {
		DevSolutionSkill.init('circle1'); 
		DevSolutionSkill.init('circle2'); 
		DevSolutionSkill.init('circle3');
	});

	/* ---------------------------------------------------------------------- */
	/*	Contact Form
	/* ---------------------------------------------------------------------- */

	var submitContact = $('#submit_contact'),
		submitReservation = $('#submit_reservation'),
		message = $('#msg');

	submitContact.on('click', function(e){
		e.preventDefault();

		var $this = $(this);
		
		$.ajax({
			type: "POST",
			url: 'contact.php',
			dataType: 'json',
			cache: false,
			data: $('#contact-form').serialize(),
			success: function(data) {

				if(data.info !== 'error'){
					$this.parents('form').find('input[type=text],textarea,select').filter(':visible').val('');
					message.hide().removeClass('alert-success').removeClass('alert-danger').addClass('alert-success').html(data.msg).fadeIn('slow').delay(5000).fadeOut('slow');
				} else {
					message.hide().removeClass('alert-success').removeClass('alert-danger').addClass('alert-danger').html(data.msg).fadeIn('slow').delay(5000).fadeOut('slow');
				}
			}
		});
	});

	submitReservation.on('click', function(e){
		e.preventDefault();

		var $this = $(this);
		
		$.ajax({
			type: "POST",
			url: 'reservation.php',
			dataType: 'json',
			cache: false,
			data: $('#reservation-form').serialize(),
			success: function(data) {

				if(data.info !== 'error'){
					$this.parents('form').find('input[type=text]').filter(':visible').val('');
					message.hide().removeClass('alert-success').removeClass('alert-danger').addClass('alert-success').html(data.msg).fadeIn('slow').delay(5000).fadeOut('slow');
				} else {
					message.hide().removeClass('alert-success').removeClass('alert-danger').addClass('alert-danger').html(data.msg).fadeIn('slow').delay(5000).fadeOut('slow');
				}
			}
		});
	});
	
	/*-------------------------------------------------*/
	/* =  Comming soon section
	/*-------------------------------------------------*/

	$('.comming-soon-section').css('min-height', $(window).height());

	try {

		$('#clock').countdown("2020/05/17", function(event) {
			var $this = $(this);
			switch(event.type) {
				case "seconds":
				case "minutes":
				case "hours":
				case "days":
				case "daysLeft":
					$this.find('span#'+event.type).html(event.value);
					break;
				case "finished":
					$this.hide();
					break;
			}
		});

	} catch(err) {

	}

	/* ---------------------------------------------------------------------- */
	/*	Header animate after scroll
	/* ---------------------------------------------------------------------- */

	(function() {

		var docElem = document.documentElement,
			didScroll = false,
			changeHeaderOn = 10;
			document.querySelector( 'header, a.go-top' );
		function init() {
			window.addEventListener( 'scroll', function() {
				if( !didScroll ) {
					didScroll = true;
					scrollPage();
				}
			}, false );
		}
		
		function scrollPage() {
			var sy = scrollY();
			if ( sy >= changeHeaderOn ) {
				$( 'header' ).addClass('active');
				$( 'a.go-top' ).addClass('active');
			}
			else {
				$( 'header' ).removeClass('active');
				$( 'a.go-top' ).removeClass('active');
			}
			didScroll = false;
		}
		
		function scrollY() {
			return window.pageYOffset || docElem.scrollTop;
		}
		
		init();
		
	})();

});

function Resize() {
	$(window).trigger('resize');
}
