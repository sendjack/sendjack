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
            'view/page/base'
            //jquery ui
        ],
        function ($, page) {


var PageView = page.getPageViewClass();

var CreateCustomerPageView = PageView.extend({

    el: '#customer-create-page'

});


return {
    CreateCustomerPageView: function (attributes, options) {
        return new CreateCustomerPageView(attributes, options);
    }
};


});
