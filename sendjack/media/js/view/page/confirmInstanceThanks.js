/**
 * Provide the Confirm Instance Thanks Page.
 *
 * @exports view.page.confirmInstanceThanks
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
        function ($, pageView) {


var PageView = pageView.getPageViewClass();

var ConfirmInstanceThanksPageView = PageView.extend({

    el: '#confirm-instance-thanks-page'

});


return {
    ConfirmInstanceThanksPageView: function (attributes, options) {
        return new ConfirmInstanceThanksPageView(attributes, options);
    }
};


});

