$(document).ready(function() {
    function myMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var mapOptions = {
            center: uluru,
            zoom: 10,
            mapTypeId: google.maps.MapTypeId.HYBRID
        }
        var marker = new google.maps.Marker({
            position: uluru,
            map: map
        });
        var map = new google.maps.Map(document.getElementById("map"), mapOptions);
    }
});