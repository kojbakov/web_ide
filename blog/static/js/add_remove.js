
function add() {
  var new_chq_no = parseInt($('#total_chq').val()) + 1;
  var new_input = "\
  <tr>\
  <td><textarea name='step_new' cols='10' rows='1' required id='id_step'></textarea></td>\
  <td><textarea name='result_new' cols='10' rows='1' required id='id_result_new'></textarea></td>\
  </tr>"
  $('#new_chq').append(new_input);
  $('#total_chq').val(new_chq_no);
  window.scrollTo(0,document.body.scrollHeight);
}

function remove(clicked_id) {
  var last_chq_no = $('#total_chq').val();
  if (last_chq_no > 0) {
    $('#'+clicked_id).remove();
    $('#total_chq').val(last_chq_no - 1);
  }
}

function addRow(tableID) {

    var table = document.getElementById(tableID);
    try{
      var rowCount = table.rows.length;
      if (rowCount == 1){
        console.log(rowCount)
        $(table).show();
      }

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var cell1 = row.insertCell(0);
    var element1 = document.createElement("input");
    element1.type = "checkbox";
    element1.name="chkbox[]";
    cell1.appendChild(element1);

    var cell2 = row.insertCell(1);
    var element2 = document.createElement("textarea");
    element2.type = "textarea";
    element2.name = "step_new";
    element2.cols = "10";
    element2.rows = "1";
    element2.value = "Step text"
    cell2.appendChild(element2);

    var cell3 = row.insertCell(2);
    var element3 = document.createElement("textarea");
    element3.type = "textarea";
    element3.name = "result_new";
    element3.cols = "10";
    element3.rows = "1";
    element3.value = "Result text"

    cell3.appendChild(element3);


      }catch(e) {
          alert(e);
      }


}

function deleteRow(tableID) {
    try {
    var table = document.getElementById(tableID);
    var rowCount = table.rows.length;

    for(var i=0; i<rowCount; i++) {
        var row = table.rows[i];
        var chkbox = row.cells[0].childNodes[0];
        if(null != chkbox && true == chkbox.checked) {
            table.deleteRow(i);
            rowCount--;
            i--;
        }
    }
    var rowCount = table.rows.length;
      if (rowCount == 1){
        $(table).hide();
      }
    }catch(e) {
        alert(e);
    }
}

function hideEmptySteps(tableID){
    try {
    var table = document.getElementById(tableID);
    var rowCount = table.rows.length;
      if (rowCount == 1){
        $(table).hide();
      }
    }catch(e) {
        alert(e);
    }

}