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
            'view/base',
            'model/customer'

            //jquery ui
        ],
        function ($, base, customer) {


// Get access to the superclass without instantiating an instance.
var ObjectView = base.getObjectViewClass();

var CustomerView = ObjectView.extend({

    initialize: function () {
        ObjectView.prototype.initialize.call(
                this,
                '#customer',
                'customer',
                customer.CustomerModel({id: this.options.model_id}));

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
                },
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
    CustomerView: function (attributes, options) {
        return new CustomerView(attributes, options);
    },

    getCustomerViewClass: function () {
        return CustomerView;
    }
};


});
