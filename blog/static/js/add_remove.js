
function add() {
  var new_chq_no = parseInt($('#total_chq').val()) + 1;
  var new_input = "\
    <div id='id_step_"+new_chq_no+"'>\
      <br>\
      <tr><th><label for='id_step_'"+new_chq_no+">Step:</label></th><td><textarea name='step_'"+new_chq_no+" cols='10' rows='1' required id='id_step'>Step text</textarea></td></tr>\
      <tr><th><label for='id_result_'"+new_chq_no+">Result:</label></th><td><textarea name='result_'"+new_chq_no+" cols='10' rows='1' required id='id_result'>Result text</textarea></td></tr>\
      <button class='save btn btn-default'>v</button>\
      <button class='save btn btn-default'>^</button>\
      <button id='id_step_"+new_chq_no+"' class='save btn btn-default' onclick='remove(this.id)'>X" + new_chq_no +"</button>\
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



//<textarea cols='80' rows='5' placeholder='Step' value='"+new_chq_no+"'></textarea>