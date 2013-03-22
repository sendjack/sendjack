/**
 * Provide the Search Page.
 *
 * @exports view.page.search
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',

            //modules
            'view/page/base',
            'view/item/instance'
        ],
        function ($, Backbone, pageView, instanceView) {


var PageView = pageView.getPageViewClass();

var SearchPageView = PageView.extend({

    el: '#search-page',

    _initializeChildViews: function () {
        var searchObjectView = SearchObjectView({
            model: this.options.instanceModel
        });
    },

    show: function (callback) {
        this.$el.fadeIn({
            duration: 'fast',
            complete: callback
        });
    },

    hide: function (callback) {
        var that = this;
        this.$el.fadeOut({
            duration: 'slow',
            complete: function () {
                setTimeout(callback, 1000);
            }
        });
    }
});


var TaskInstanceView = instanceView.getTaskInstanceViewClass();
function SearchObjectView(attributes, options) {
    var SearchObjectViewClass = TaskInstanceView.extend({

        getRequiredValidationRules: function () {
            return {
                rules: {
                    customer_title: {
                        required: true
                    }
                }
            };
        },

        onSubmit: function (event) {
            if (this.isValid()) {
                Backbone.history.navigate('/tasks/create', {trigger: true});
            } else {
                console.log('this form is not valid');
            }
        }
    });

    return new SearchObjectViewClass(attributes, options);
}


return {
    SearchPageView: function (attributes, options) {
        return new SearchPageView(attributes, options);
    }
};


});
