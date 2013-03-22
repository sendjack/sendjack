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
        ],
        function ($, pageView, instanceView) {


var PageView = pageView.getPageViewClass();

var CreateInstancePageView = PageView.extend({

    el: '#create-instance-page',

    _initializeChildViews: function () {

        var createInstanceObjectView = CreateInstanceObjectView({
            model: this.options.instanceModel
        });
    }
});


var TaskInstanceView = instanceView.getTaskInstanceViewClass();
function CreateInstanceObjectView(attributes, options) {
    var CreateInstanceObjectViewClass = TaskInstanceView.extend({

        getRequiredValidationRules: function () {
            return {
                rules: {
                    customer_title: {
                        required: true
                    },
                    customer_description: {
                        required: true
                    },
                    deadline_ts: {
                        required: true
                    }
                }
            };
        }
    });

    return new CreateInstanceObjectViewClass(attributes, options);
}


return {
    CreateInstancePageView: function (attributes, options) {
        return new CreateInstancePageView(attributes, options);
    }
};


});
