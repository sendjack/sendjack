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
    var that = {};

    /**
     * Convert credit card data to Stripe token and save it.
     */
    that.saveCreditCard = function (
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

    /**
     * Return Stripe token.
     */
    that.getTokenFromStripeResponse = function (status, response) {
        var token = null;
        if (response.error) {
            console.log('Stripe response error:', response.error.message);
        } else {
            token = response.id;
        }

        return token;
    };

    return that;
})();

return payment;


});
