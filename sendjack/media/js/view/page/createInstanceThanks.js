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
        function ($, page) {


var PageView = page.getPageViewClass();

var CreateInstanceThanksPageView = PageView.extend({

    el: '#instance-create-page'

});


return {
    CreateInstanceThanksPageView: function (attributes, options) {
        return new CreateInstanceThanksPageView(attributes, options);
    }
};


});
