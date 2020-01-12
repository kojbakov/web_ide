function add() {
  var new_chq_no = parseInt($('#total_chq').val()) + 1;
  var new_input = "\
    <div id='new_step_"+new_chq_no+"'>\
      <br>\
      <textarea cols='80' rows='5' placeholder='Step' value='"+new_chq_no+"'></textarea>\
      <textarea cols='80' rows='5' placeholder='Result' value='"+new_chq_no+"'></textarea>\
      <button class='save btn btn-default'>v</button>\
      <button class='save btn btn-default'>^</button>\
      <button id='new_step_"+new_chq_no+"' class='save btn btn-default' onclick='remove(this.id)'>X" + new_chq_no +"</button>\
    </div>"
  //<div id='indent'><button class='save btn btn-default' onclick='remove()'>Remove</button></div>"
  
  $('#new_chq').append(new_input);
  $('#total_chq').val(new_chq_no);
  window.scrollTo(0,document.body.scrollHeight);
}

function remove(clicked_id) {
  var last_chq_no = $('#total_chq').val();
  if (last_chq_no > 0) {
    //console.log(clicked_id)
    //alert(clicked_id);
    $('#'+clicked_id).remove();
    $('#total_chq').val(last_chq_no - 1);
  }
}