/**
 * Access the CreditCardView.
 *
 * @exports view.creditCard
 *
 * @requires $
 * @requires Lodash
 *
 */
define(
        [
            //libraries
            'jquery',
            'underscore',

            //modules
            'event',
            'view/item/base'

            //jquery ui
        ],
        function ($, _, event, baseView) {


// Get access to the superclass without instantiating an instance.
var ItemView = baseView.getItemViewClass();

var CreditCardView = ItemView.extend({

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
        ItemView.prototype.initialize.call(this);
        this.$submitButton = this.$el.find('.submit-button');
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

            this.model.save();
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
    },

    /** TODO: This isn't currently called. */
    addTypeCheckingValidationRules: function () {
        this.$el.validate({
            rules: {
                card_number: {
                    creditcard: true
                },
                card_expiry_month: {
                    range: [0,12]
                },
                card_expiry_year: {
                    number: true,
                    minlength: 4,
                    maxlength: 4
                },
                cvc: {
                    number: true,
                    maxlength: 5
                }
            }
        });
    }
});

return {
    CreditCardView: function (attributes, options) {
        return new CreditCardView(attributes, options);
    }
};


});
