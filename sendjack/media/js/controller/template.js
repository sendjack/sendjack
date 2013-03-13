/**
 * Access the Template Page.
 *
 * @exports controller.template
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',

            //modules
            'model/template',
            'view/page/template'
        ],
        function (
                $,
                Backbone,
                templateModel,
                templateView) {

var TemplateController = Backbone.Marionette.Controller.extend({

    region: null,

    templateModel: null,

    templatePage: null,

    pagesSelector: '#template-page',

    initialize: function () {
        if ($(this.pagesSelector).length) {
            this.region = new Backbone.Marionette.Region({
                el: '.content'
            });

            this.initializeModels();
            this.initializePages();
            this.initializeTransitions();
        }
    },

    initializeModels: function () {
        this.templateModel = templateModel.TaskTemplateModel();
    },

    initializePages: function () {
        this.templatePage = templateView.TemplatePageView({
            templateModel: this.templateModel
        });
    },

    initializeTransitions: function () {

    },

    loadTemplatePage: function (templateID) {
        if (templateID) {
            var id = parseInt(templateID, 10);
            if (this.templateModel.isNew()) {
                this.templateModel.resetID(id);
            }
        }

        this.region.show(this.templatePage);
    }

});


/** Make sure ProcessInstanceController is a singleton. */
var templateController = null;

return {
    TemplateController: function () {
        if (templateController === null) {
            templateController = new TemplateController();
        }

        return templateController;
    }
};


});


