function update_species(id, childs_length){
    $.post('',
           { 'id': id.toString(),
             'childs': childs_length},
           function(data) {
             $("#table" + id.toString()).replaceWith(data);
           });
};