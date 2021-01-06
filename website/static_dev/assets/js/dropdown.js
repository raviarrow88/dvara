$(document).ready(function(){


var get_subs = function(){
  var cat_id = $('#id_category').val()

  $.ajax({
    url: '/get_subs/?id='+cat_id,
    success:function(data){
      console.log(data)
      var len = data['sub_cats'].length
      $('#id_sub_category').empty()
      for(var i=0;i<len;i++){

                $('#id_sub_category').append("<option value="+data['sub_cats'][i][0]+">"+data['sub_cats'][i][1]+"</option>")
      }

    },
    type:'GET',
  });
}


$('#id_category').click(get_subs)

})
