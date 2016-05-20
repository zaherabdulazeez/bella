/* Authors: Zaher Abdul Azeez
* The main front end script 
* All interactions are implemented here
* All visualizations are implemented here
*/
 $(function() {
    $('#food').slider()
    $('#health').slider()
    $('#education').slider()
    $('.span2').on('slide', function (ev) {
        var f = parseInt($('#food').val());
        var h = parseInt($('#health').val());
        var e = parseInt($('#education').val());
        reload(f,h,e);
});
});
