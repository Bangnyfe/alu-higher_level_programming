#!/usr/bin/node
$(document).ready(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
  });
});
