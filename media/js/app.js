
/**
 * STRIPE
 **/

var PUBLISHABLE_DEV_KEY = "pk_gd3qjiAUdlUvLbjLqJsS5ApMRSQqO";
var PUBLISHABLE_PROD_KEY = "";

// this identifies your website in the createToken call below
Stripe.setPublishableKey(PUBLISHABLE_DEV_KEY);

$(document).ready(function() {
  $("#payment-form").submit(function(event) {
    // disable the submit button to prevent repeated clicks
    $('.submit-button').attr("disabled", "disabled");

    Stripe.createToken({
        number: $('.card-number').val(),
        cvc: $('.card-cvc').val(),
        exp_month: $('.card-expiry-month').val(),
        exp_year: $('.card-expiry-year').val()
    }, stripeResponseHandler);

    // prevent the form from submitting with the default action
    return false;
  });
});

function stripeResponseHandler(status, response) {
    var $signUpForm = $('form[name="signup"]');
    console.log($signUpForm);
    console.log(status);
    console.log(response);
    console.log(response.id);

    // add token to form
    $signUpForm.find('[name="token"]').val(response.id);

    // submit form
    $signUpForm.submit();
}
