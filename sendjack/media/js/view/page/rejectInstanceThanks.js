/**
 * Provide the Reject Instance Thanks Page.
 *
 * @exports view.page.rejectInstanceThanks
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/page/base'
        ],
        function ($, pageView) {


var PageView = pageView.getPageViewClass();

var RejectInstanceThanksPageView = PageView.extend({

    el: '#reject-instance-thanks-page'

});


return {
    RejectInstanceThanksPageView: function (attributes, options) {
        return new RejectInstanceThanksPageView(attributes, options);
    }
};


});
