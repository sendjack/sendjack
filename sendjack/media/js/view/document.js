/**
 * Access the DocumentView.
 *
 * @exports DocumentView
 * @requires $
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',

            //modules
            'view/template',
            'view/signUpSeries',
            'view/taskInstancePostPage',

            //jquery plugins
            'jqueryui',
            'validation'
        ],
        function ($, Backbone, template, signUpSeries, taskInstancePostPage) {


var DocumentView = Backbone.View.extend({

    initialize: function () {


        if ($('#template').length !== 0) {
            var taskTemplateView = template.TaskTemplateView();
        }

        if ($('.alt-content').length !== 0) {
            var signUpSeriesView = signUpSeries.SignUpSeries();
        }

        if ($('.task-instance-post-page').length !== 0) {
            var taskPostPage = taskInstancePostPage.TaskInstancePostPage();
        }

    }
});

/** Make sure DocumentView is a singleton. */
var documentView = null;

return {
    DocumentView: function () {
        if (documentView === null) {
            documentView = new DocumentView();
        }

        return documentView;
    }
};


});
