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

    // Stripe keys
    // TODO: Pull from a constants file
    var PUBLISHABLE_DEV_KEY = "pk_gd3qjiAUdlUvLbjLqJsS5ApMRSQqO";
    var PUBLISHABLE_PROD_KEY = "pk_W32hVKbXvAXcpskodZueIxA3QyGJ3";
    var api_key = PUBLISHABLE_DEV_KEY;

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
    Stripe.setPublishableKey(api_key);

    this.setupPaymentForm = (function () {
        $("#payment-form").submit(function(event) {
            // disable the submit button to prevent repeated clicks
            $('.submit-button').attr("disabled", "disabled");

            console.log($('.card-number').val());

            Stripe.createToken({
                number: $('.card-number').val(),
                cvc: $('.card-cvc').val(),
                exp_month: $('.card-expiry-month').val(),
                exp_year: $('.card-expiry-year').val()
            }, stripeResponseHandler);

            // prevent the form from submitting with the default action
            return false;
        });

        $('input').keyup(function () {
            if (verifyForm()) {
                $('.submit-button').removeAttr("disabled");
            } else {
                $('.submit-button').attr("disabled", "disabled");
            }
        });
    })();
            

    function stripeResponseHandler(status, response) {
        if (response.error) {
            // show the errors on the form
            console.log("errors");
            $(".payment-errors").text(response.error.message);
            $(".submit-button").removeAttr("disabled");
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
