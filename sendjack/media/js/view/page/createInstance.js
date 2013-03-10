/**
 * Provide the Create Instance Page.
 *
 * @exports view.page.createInstance
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

var CreateInstancePageView = PageView.extend({

    el: '#instance-create-page'

});


return {
    CreateInstancePageView: function (attributes, options) {
        return new CreateInstancePageView(attributes, options);
    }
};


});
