/**
 * Sign up application.
 *
 * @exports app
 *
 * @requires $
 * @requires Stripe
 **/

var jackalope = jackalope || {};
jackalope.app = (function () {

    // remove imported libraries from global
    jQuery.noConflict();
    var stripeNoConflict = Stripe;
    delete Stripe;

    this.init = (function ($) {
        $(document).ready(function() {
            jackalope.payment($, stripeNoConflict);
        });
    }(jQuery));

}());
