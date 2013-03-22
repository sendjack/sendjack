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
            if (isControlGroup) {
                this.initializeShownControlFields();
            } else {
                this.initializeShownTestFields();
            }

            this.$el.find('input, textarea').attr('disabled', 'disabled');
        },

        initializeShownControlFields: function () {
            this.initializeShownFields();

            var fields = this.$el.find('.field');

            fields.has('[name=description]').hide();
            fields.has('[name=more_details]').hide();
        },

        initializeShownTestFields: function () {
            this.initializeShownFields();

            var fields = this.$el.find('.field');
        },

        initializeShownFields: function () {
            var fields = this.$el.find('.field');

            fields.has('[name=customer_title]').hide();
            fields.has('[name=customer_description]').hide();

            fields.has('[name=template_id]').hide();

            fields.has('[name=properties]').hide();
            fields.has('[name=property]').hide();
            fields.has('[name=output_type]').hide();
            fields.has('[name=output_method]').hide();
            fields.has('[name=category_tags]').hide();
            fields.has('[name=industry_tags]').hide();
            fields.has('[name=skill_tags]').hide();
            fields.has('[name=equipment_tags]').hide();
            fields.has('[name=instructions]').hide();
            fields.has('[name=instruction]').hide();
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
