/**
 * Access the CreditCardView.
 *
 * @exports payment
 *
 * @requires $
 * @requires Lodash
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'jquery',
            'lodash',
            'backbone',

            //modules
            'event',
            'util/payment'

            //jquery ui
        ],
        function ($, _, Backbone, event, payment) {


var CreditCardView = Backbone.View.extend({

    required_fields: [
        "first_name",
        "last_name",
        "email",
        "card_number",
        "card_expiry_month",
        "card_expiry_year",
        "card_cvc"
    ],

    initialize: function () {
        this.$submitButton = this.$el.find('.submit-button');
        this.customerModel = this.options.customerModel;
        _.bindAll(this);

    },

    events: function () {
        var _events = {};

        _events['click .submit-button'] = 'save';

        return _events;
    },
        
    save: function () {
        if (this.validate()) {
            this.$submitButton.attr('disabled', 'disabled');

            payment.saveCreditCard(
                    this.$el.find('[name=card_number]').val(),
                    this.$el.find('[name=card_cvc]').val(),
                    this.$el.find('[name=card_expiry_month]').val(),
                    this.$el.find('[name=card_expiry_year]').val(),
                    this.onSaveResponse);
        }
    },

    onSaveResponse: function (status, response) {
        var token = payment.getTokenFromStripeResponse(status, response);

        if (token === null) {
            //FIXME XXX
            //this.$el.find('.payment-errors').text(response.error.message).show();
            this.$submitButton.removeAttr('disabled');

            //var offset = $('#second-focus').offset().top;
            //$('html, body').animate({scrollTop:offset}, 1000);
        } else {
            this.customerModel.set('stripe_token', token);
            this.trigger(event.SAVE);
        }
    },

    validate: function () {
        var validated = true;
        for (var i = 0; i < this.required_fields.length; i += 1) {
            if ($('[name=' + this.required_fields[i] + ']').val() === "") {
                validated = false;
            }
        }

        return validated;
    }

});

return {
    CreditCardView: function (attributes, options) {
        return new CreditCardView(attributes, options);
    }
};


});
