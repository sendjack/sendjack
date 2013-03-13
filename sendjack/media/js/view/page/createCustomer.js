/**
 * Provide the Create Customer Page.
 *
 * @exports view.page.createCustomer
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/page/base',
            'view/item/customer'
            //jquery ui
        ],
        function ($, pageView, customerView) {


var PageView = pageView.getPageViewClass();

var CreateCustomerPageView = PageView.extend({

    el: '#create-customer-page',

    _initializeChildViews: function () {
        var createCustomerObjectView = CreateCustomerObjectView({
            model: this.options.customerModel
        });
    }
});


var CustomerView = customerView.getCustomerViewClass();
function CreateCustomerObjectView(attributes, options) {
    var CreateCustomerObjectViewClass = CustomerView.extend({

        initialize: function () {
            CustomerView.prototype.initialize.call(this);

            this.model.on('change:stripe_token', this.onAttributeChange, this);
        },

        addRequiredValidationRules: function () {
            this.$el.validate({
                rules: {
                    first_name: 'required',
                    last_name: 'required',
                    email: 'required'
                }
            });
        },

        onAttributeChange: function (model, value, options) {
            console.log('THIS SHOULD NEVER EVER BE CALLED.');
            this.save();
        }
    });

    return new CreateCustomerObjectViewClass(attributes, options);
}

return {
    CreateCustomerPageView: function (attributes, options) {
        return new CreateCustomerPageView(attributes, options);
    }
};


});
