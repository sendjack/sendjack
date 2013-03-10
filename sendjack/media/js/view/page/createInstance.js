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
            'view/page/base',
            'view/item/instance'
            //jquery ui
        ],
        function ($, pageView, instanceView) {


var PageView = pageView.getPageViewClass();

var CreateInstancePageView = PageView.extend({

    el: '#instance-create-page',

    _initializeChildViews: function () {

        var createInstanceObjectView = CreateInstanceObjectView({
            model: this.options.instanceModel
        });
    }
});


var TaskInstanceView = instanceView.getTaskInstanceViewClass();
function CreateInstanceObjectView(attributes, options) {
    var CreateInstanceObjectViewClass = TaskInstanceView.extend({

        addRequiredValidationRules: function () {
            this.$el.validate({
                rules: {
                    customer_title: 'required',
                    customer_description: 'required',
                    deadline_ts: 'required'
                }
            });
        }
    });

    return new CreateInstanceObjectViewClass(attributes, options);
}


return {
    CreateInstancePageView: function (attributes, options) {
        console.log(attributes);
        return new CreateInstancePageView(attributes, options);
    }
};


});
