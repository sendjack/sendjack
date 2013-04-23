/**
 * Access the CustomerView
 *
 * @exports view.customer
 *
 * @requires $
 * @requires view.base
 * @requires model.customer
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/item/base'

            //jquery ui
        ],
        function ($, baseView) {


// Get access to the superclass without instantiating an instance.
var ObjectView = baseView.getObjectViewClass();

var CustomerView = ObjectView.extend({

    el: '.customer-view',

    initialize: function () {
        ObjectView.prototype.initialize.call(this);

        if (this.model.isNew()) {
            var isControlGroup = Math.floor(Math.random() * 2);
            if (isControlGroup) {
                this.model.set('control_group', true);
            } else {
                this.model.set('control_group', false);
            }
        }
    },

    getTypeCheckingValidationRules: function () {
        return {
            rules: {
                email: {
                    email: true
                }
            }
        };
    },

    editBindings: function (bindings) {

        // We send this to Stripe but don't want it on our servers.
        delete bindings.card_number;
        delete bindings.card_expiry_month;
        delete bindings.card_expiry_year;
        delete bindings.card_cvc;

        return bindings;
    }

});

return {
    CustomerView: function (attributes, options) {
        return new CustomerView(attributes, options);
    },

    getCustomerViewClass: function () {
        return CustomerView;
    }
};


});
