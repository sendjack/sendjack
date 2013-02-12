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
                customer.CustomerModel());

        var status = this.$el.find('[name=status]').val();
        this.model.set('status', status);
    }
});

return {
    CustomerView: function () {
        return new CustomerView();
    }
};


});
