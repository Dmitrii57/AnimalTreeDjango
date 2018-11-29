function search(root_id, species){
    $.post('/search/',
           { 'name': species},
           function(data) {
             $("#table1").replaceWith(data);
           });
};