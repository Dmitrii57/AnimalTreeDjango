$(document).ready(function(){
    $("#searching_species").autocomplete({
        source: "/autocomplete/",
        minLength: 3,
        open: function(){
        }
      });
});

function search(root_id, species){
    $.post('/search/',
           { 'name': species},
           function(data) {
             $("#table1").replaceWith(data);
           });
};