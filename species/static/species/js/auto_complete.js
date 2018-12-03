$(document).ready(function(){
    $("#searching_species").autocomplete({
        source: "/autocomplete/",
        minLength: 3,
        open: function(){
        }
    });
});