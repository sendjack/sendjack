/**
 * Provide the Approve Instance Thanks Page.
 *
 * @exports view.page.approveInstanceThanks
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

var ApproveInstanceThanksPageView = PageView.extend({

    el: '#approve-instance-thanks-page'

});


return {
    ApproveInstanceThanksPageView: function (attributes, options) {
        return new ApproveInstanceThanksPageView(attributes, options);
    }
};


});
