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

            //jquery ui
            'jqueryui'
        ],
        function ($, Backbone, template, signUpSeries, taskInstancePostPage) {


var DocumentView = Backbone.View.extend({

    initialize: function () {
        //this.setElement('#karma');

        var datepicker = $('.datepicker').datepicker({minDate: '0'});

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

return {
    DocumentView: function () {
        return new DocumentView();
    }
};


});
