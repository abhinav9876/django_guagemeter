$(function(){
  $('#test').speedometer();

  $('.changeSpeedometer').click(function(){
    $('#test').speedometer({ percentage: $('.speedometer').val() || 0 });
  });

});

$(function(){
  $('#test1').speedometer();

  $('.changeSpeedometer1').click(function(){
    $('#test1').speedometer({ percentage: $('.speedometer1').val() || 0 });
  });

});
