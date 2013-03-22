/**
 * Provide the Process Instance Page.
 *
 * @exports view.page.processInstance
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/page/base',
            'view/item/instance'
        ],
        function ($, pageView, instanceView) {


var PageView = pageView.getPageViewClass();

var ProcessInstancePageView = PageView.extend({

    el: '#process-instance-page',
    processInstanceObjectView: null,

    _initializeChildViews: function () {
        this.processInstanceObjectView = instanceView.TaskInstanceView({
            model: this.options.instanceModel
        });
    }
});


return {
    ProcessInstancePageView: function (attributes, options) {
        return new ProcessInstancePageView(attributes, options);
    }
};


});
