/**
 * Pay with Stripe.
 *
 * @exports payment
 *
 * @requires $
 * @requires stripe
 *
 */
define(
        [
            // libraries
            'jquery',
            'stripe'

            // modules
            // jquery ui
        ],
        function ($, Stripe) {


// Get Stripe key from meta data.
var apiKey = $('meta[name=stripe-key]').attr('content');

// this identifies your website in the createToken call below
Stripe.setPublishableKey(apiKey);

/**
 * Save Credit Card with Stripe.
 */
var payment = (function () {

    this.saveCreditCard = function (
            number,
            cvc,
            expMonth,
            expYear,
            responseFunction) {

        Stripe.createToken(
                {
                    number: number,
                    cvc: cvc,
                    exp_month: expMonth,
                    exp_year: expYear
                },
                responseFunction);
    };

    this.getTokenFromStripeResponse = function (status, response) {
        var token = null;
        if (response.error) {
            console.log('Stripe response error:', response.error.message);
        } else {
            token = response.id;
        }

        return token;
    };

    return this;
})();

return payment;


});
