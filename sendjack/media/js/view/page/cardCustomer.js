/**
 * Provide the Card Customer Page.
 *
 * @exports view.page.cardCustomer
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/page/base',
            'view/item/customer',
            'view/item/creditCard'
        ],
        function ($, pageView, customerView, creditCardView) {


var PageView = pageView.getPageViewClass();

var CardCustomerPageView = PageView.extend({

    el: '#card-customer-page',
    cardCustomerObjectView: null,
    creditCardView: null,

    _initializeChildViews: function () {
        this.cardCustomerObjectView = CardCustomerObjectView({
            model: this.options.customerModel
        });

        this.creditCardView = creditCardView.CreditCardView({
            el: '.card-customer-grid',
            model: this.options.creditCardModel
        });

    },

    /** Set certain events for onShow. */
    onShow: function () {

        // Only when the user changes the token should we save the customer.
        this.options.customerModel.on(
                'change:stripe_token',
                function (model, value) {
                    if (value) {
                        this.cardCustomerObjectView.save();
                    }
                },
                this);
    }
});


var CustomerView = customerView.getCustomerViewClass();
function CardCustomerObjectView(attributes, options) {
    var CardCustomerObjectViewClass = CustomerView.extend({
        
        getRequiredValidationRules: function () {
            return {
                rules: {
                    first_name: {
                        required: true
                    },
                    last_name: {
                        required: true
                    },
                    email: {
                        required: true
                    },
                    card_number: {
                        required: true
                    },
                    card_expiry_month: {
                        required: true
                    },
                    card_expiry_year: {
                        required: true
                    },
                    cvc: {
                        required: true
                    }
                }
            };
        },

        onSubmit: function () {
            // do not save customer as we're waiting on the credit card.
        }
    });

    return new CardCustomerObjectViewClass(attributes, options);
}

return {
    CardCustomerPageView: function (attributes, options) {
        return new CardCustomerPageView(attributes, options);
    }
};


});
