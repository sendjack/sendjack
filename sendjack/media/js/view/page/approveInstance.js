/**
 * Provide the Approve Instance Page.
 *
 * @exports view.page.approveInstance
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

var ApproveInstancePageView = PageView.extend({

    el: '#approve-instance-page',
    approveInstanceObjectView: null,

    _initializeChildViews: function () {
        this.approveInstanceObjectView = ApproveInstanceObjectView({
            model: this.options.instanceModel
        });
    }
});


var TaskInstanceView = instanceView.getTaskInstanceViewClass();
function ApproveInstanceObjectView(attributes, options) {
    var ApproveInstanceObjectViewClass = TaskInstanceView.extend({

        setupControlAndTestFields: function (isControlGroup) {
            var fields = this.$el.find('.field');

            if (isControlGroup) {
                fields.has('[name=description]').hide();
                fields.has('[name=more_details]').hide();
            }

            this.$el.find('input, textarea').attr('disabled', 'disabled');
        },

        save: function (attributes, options) {
            var approved_status_attribute = {status: 'approved'};
            TaskInstanceView.prototype.save.call(
                    this,
                    $.extend(approved_status_attribute, attributes),
                    options);
        }
    });

    return new ApproveInstanceObjectViewClass(attributes, options);
}


return {
    ApproveInstancePageView: function (attributes, options) {
        return new ApproveInstancePageView(attributes, options);
    }
};


});
