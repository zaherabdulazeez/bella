/* Authors: Zaher Abdul Azeez
* Map related scripts are implemented here
*/

function initMap(){
	var map = new google.maps.Map(document.getElementById('map'),
		{
			center:{lat:19.132637,lng:72.913157},
			zoom:15
		}
		);
}