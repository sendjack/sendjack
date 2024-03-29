/**
 * Stripe wrapper module.
 *
 * @exports payment
 *
 * @requires $
 * @requires Stripe
 **/

var jackalope = jackalope || {};
jackalope.payment = function ($, Stripe) {

    // Get Stripe key from meta data.
    var apiKey = $('meta[name=stripe-key]').attr('content');

    // Sign up form required fields
    var required_fields = [
        "first-name",
        "last-name",
        "email",
        "card-number",
        "card-expiry-month",
        "card-expiry-year",
        "card-cvc"
    ];

    // this identifies your website in the createToken call below
    Stripe.setPublishableKey(apiKey);

    this.setupPaymentForm = (function () {
        $("#payment-form").submit(function(event) {
            // disable the submit button to prevent repeated clicks
            $('.submit-button').attr("disabled", "disabled");

            // only submit a verified form
            if (verifyForm()) {
                Stripe.createToken({
                    number: $('.card-number').val(),
                    cvc: $('.card-cvc').val(),
                    exp_month: $('.card-expiry-month').val(),
                    exp_year: $('.card-expiry-year').val()
                }, stripeResponseHandler);
            }

            // prevent the form from submitting with the default action
            return false;
        });
    })();
            

    function stripeResponseHandler(status, response) {
        if (response.error) {
            // show the errors on the form
            console.log("errors");
            $(".payment-errors").text(response.error.message).show();
            $(".submit-button").removeAttr("disabled");

            var offset = $('#second-focus').offset().top;
            $('html, body').animate({scrollTop:offset}, 1000);
        } else {
            var $form = $("#payment-form");
            // token contains id, last4, and card type
            var token = response.id;
            // insert the token into the form so it gets submitted to the server
            $form.find('[name="token"]').val(token);
            // and submit
            $form.get(0).submit();
        }
    }

    // TODO: create a formUtil module with validation.
    function verifyForm() {
        var verified = true;
        for (var i = 0; i < required_fields.length; i += 1) {
            if ($('.' + required_fields[i]).val() === "") {
                verified = false;
            }
        }

        return verified;
    }
};
