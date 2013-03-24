/**
 * Provide the Confirm Instance Page.
 *
 * @exports view.page.confirmInstance
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/page/base',
            'view/item/instance'
            //jquery ui
        ],
        function ($, pageView, instanceView) {


var PageView = pageView.getPageViewClass();

var ConfirmInstancePageView = PageView.extend({

    el: '#confirm-instance-page',
    confirmInstanceObjectView: null,

    _initializeChildViews: function () {
        this.confirmInstanceObjectView = ConfirmInstanceObjectView({
            model: this.options.instanceModel
        });
    }
});


var TaskInstanceView = instanceView.getTaskInstanceViewClass();
function ConfirmInstanceObjectView(attributes, options) {
    var ConfirmInstanceObjectViewClass = TaskInstanceView.extend({

        setupControlAndTestFields: function (isControlGroup) {
            var fields = this.$el.find('.field');

            if (isControlGroup) {
                fields.has('[name=description]').hide();
                fields.has('[name=more_details]').hide();
            }
        }
    });

    return new ConfirmInstanceObjectViewClass(attributes, options);
}


return {
    ConfirmInstancePageView: function (attributes, options) {
        return new ConfirmInstancePageView(attributes, options);
    }
};


});
