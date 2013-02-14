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
    }
});

return {
    CustomerView: function (attributes, options) {
        return new CustomerView(attributes, options);
    }
};


});
