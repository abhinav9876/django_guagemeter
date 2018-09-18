function testadd(id){
  var server = prompt("Enter server ip addr: ", "192.1.1.5");

  var last_tested = '2_aug_1018';
  var avg_speed = '4.8';
  var ping_RTT = '6';
  var upload_speed = '3.7';
  var download_speed = '4.3';
  var download = 'false_link';
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML ="hello"+ this.responseText;
    //  prompt("enter name","ame");
    }
  };

  xhttp.open("GET","add_test_entry/"+server+";"+last_tested+";"+avg_speed+";"+ping_RTT+";"+upload_speed
        +";"+download_speed+";"+download+"/", true);
  xhttp.send();

//  $.post( "{% url 'add_test_entry' %}",
// {
//   csrfmiddlewaretoken: '{{ csrf_token}}' ,
//score : score, //pass the score here
//win: win  // pass the win value here
//},
//function(data) {
//     if(data.status == 1){
  //         success! Do something

  //   }
    // else{
         // error! Do something
     //}
 //});
}
