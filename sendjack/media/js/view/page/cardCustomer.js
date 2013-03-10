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
            'view/item/customer'
        ],
        function ($, pageView, customerView) {


var PageView = pageView.getPageViewClass();

var CardCustomerPageView = PageView.extend({

    el: '#customer-card-page',

    _initializeChildViews: function () {
        var cardCustomerObjectView = CardCustomerObjectView({
            model: this.options.customerModel
        });

        var creditCardView = payment.CreditCardView({
            el: '#credit-card-grid',
            model: this.options.creditCardModel
        });

        // once we get a token we should save the customer
        this.options.creditCardModel.once(
                event.SAVE,
                cardCustomerObjectView.save,
                this);

    }

});


var CustomerView = customerView.getCustomerViewClass();
function CardCustomerObjectView(attributes, options) {
    var CardCustomerObjectViewClass = CustomerView.extend({
        
        addRequiredValidationRules: function () {
            this.$el.validate({
                rules: {
                    first_name: 'required',
                    last_name: 'required',
                    email: 'required',
                    card_number: 'required',
                    card_expiry_month: 'required',
                    card_expiry_year: 'required',
                    cvc: 'required'
                }
            });
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
