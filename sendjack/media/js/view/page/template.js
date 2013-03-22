/**
 * Provide the Template Page.
 *
 * @exports view.page.template
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/page/base',
            'view/item/template'
        ],
        function ($, pageView, templateView) {


var PageView = pageView.getPageViewClass();

var TemplatePageView = PageView.extend({

    el: '#template-page',

    templateObjectView: null,

    _initializeChildViews: function () {
        this.templateObjectView = templateView.TaskTemplateView({
            model: this.options.templateModel
        });
    }
});


return {
    TemplatePageView: function (attributes, options) {
        return new TemplatePageView(attributes, options);
    }
};


});

