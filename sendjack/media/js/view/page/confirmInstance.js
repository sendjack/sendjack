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

        setupControlAndTestFields: function (isControlGroup, taskStatus) {
            if (isControlGroup) {
                this.initializeControlFields(taskStatus);
            } else {
                this.initializeTestFields(taskStatus);
            }
        },

        initializeControlFields: function (taskStatus) {
            this.initializeShownControlFields(taskStatus);
            this.initializeDisabledControlFields(taskStatus);
        },

        initializeTestFields: function (taskStatus) {
            this.initializeShownTestFields(taskStatus);
            this.initializeDisabledTestFields(taskStatus);
        },

        initializeShownControlFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('.template-id').hide();

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('.properties').hide();
                this.$el.find('.property').hide();
                this.$el.find('.output-type').hide();
                this.$el.find('.output-method').hide();
                this.$el.find('.category-tags').hide();
                this.$el.find('.industry-tags').hide();
                this.$el.find('.skill-tags').hide();
                this.$el.find('.equipment-tags').hide();
            }

            this.$el.find('.field.title').hide();
            this.$el.find('.instructions').hide();
            this.$el.find('.instruction').hide();
        },

        initializeDisabledControlFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('[name=customer_title]')
                        .attr('disabled', 'disabled');
                this.$el.find('[name=customer_description]')
                        .attr('disabled', 'disabled');

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('[name=notes]').attr('disabled', 'disabled');
                this.$el.find('[name=deadline_ts]')
                        .attr('disabled', 'disabled');

                this.$el.find('[name=price]').attr('disabled', 'disabled');
            }
        },

        initializeShownTestFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('.template-id').hide();

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('.properties').hide();
                this.$el.find('.property').hide();
                this.$el.find('.output-type').hide();
                this.$el.find('.output-method').hide();
                this.$el.find('.category-tags').hide();
                this.$el.find('.industry-tags').hide();
                this.$el.find('.skill-tags').hide();
                this.$el.find('.equipment-tags').hide();
            }

            this.$el.find('.customer-title').hide();
            this.$el.find('.customer-description').hide();
        },

        initializeDisabledTestFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('[name=title]').attr('disabled', 'disabled');
                // TODO: can hidden inputs be disabled?
                //this.$el.find('[name=instructions]').attr('disabled', 'disabled');
                this.$el.find('[name=instruction]').attr('disabled', 'disabled');

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('[name=notes]').attr('disabled', 'disabled');
                this.$el.find('[name=deadline_ts]').attr('disabled', 'disabled');

                this.$el.find('[name=price]').attr('disabled', 'disabled');
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
