/**
 * A model of a credit card, which gets sent to Stripe.
 *
 * @exports model.creditCard
 */
define(
        [
            // libraries
            'underscore',
            'backbone',

            // modules
            'event',
            'util/payment'
        ],
        function (_, Backbone, event, payment) {


var CreditCardModel = Backbone.Model.extend({

    initialize: function () {
        Backbone.Model.prototype.initialize.call(this);

        _.bindAll(this);

    },

    /** Override save() to work with the payment utility. */
    save: function () {
        payment.saveCreditCard(
                this.get('card_number'),
                this.get('card_cvc'),
                this.get('card_expiry_month'),
                this.get('card_expiry_year'),
                this.onSave);
    },

    onSave: function (status, response) {
        var token = payment.getTokenFromStripeResponse(status, response);

        if (token === null) {
            console.log('Stripe response token is null.');
            //FIXME XXX
            //this.$el.find('.payment-errors').text(response.error.message).show();
            //this.$submitButton.removeAttr('disabled');

            //var offset = $('#second-focus').offset().top;
            //$('html, body').animate({scrollTop:offset}, 1000);
        } else {
            this.set('stripe_token', token);
        }
    }
});

return {
    CreditCardModel: function (attributes, options) {
        return new CreditCardModel(attributes, options);
    }
};


});
