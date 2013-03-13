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

    el: '#customer',

    initialize: function () {
        ObjectView.prototype.initialize.call(this);

        // FIXME XXX: Check to make sure the model is correct.
        //
        var $status = this.$el.find('[name=status]');
        if ($status.length !== 0) {
            this.model.set('status', $status.val());
        }

        if (this.model.isNew()) {
            var isControlGroup = Math.floor(Math.random() * 2);
            if (isControlGroup) {
                this.model.set('control_group', true);
            } else {
                this.model.set('control_group', false);
            }
        }
    },

    addTypeCheckingValidationRules: function () {
        this.$el.validate({
            rules: {
                email: {
                    email: true
                }
            }
        });
    },

    editBindings: function (bindings) {

        // We send this to Stripe but don't want it on our servers.
        delete bindings.card_cvc;
        delete bindings.card_expiry_month;
        delete bindings.card_expiry_year;
        delete bindings.card_number;

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
