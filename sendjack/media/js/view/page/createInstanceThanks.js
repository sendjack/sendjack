/**
 * Provide the Create Instance Thanks Page.
 *
 * @exports view.page.createInstanceThanks
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

var CreateInstanceThanksPageView = PageView.extend({

    el: '#instance-create-thanks-page'

});


return {
    CreateInstanceThanksPageView: function (attributes, options) {
        return new CreateInstanceThanksPageView(attributes, options);
    }
};


});
