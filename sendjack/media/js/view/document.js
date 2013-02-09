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

            //jquery ui
            'jqueryui'
        ],
        function ($, Backbone, template) {


var DocumentView = Backbone.View.extend({

    initialize: function () {
        this.setElement('#karma');

        var datepicker = $('.datepicker').datepicker();

        if ($('#template').length !== 0) {
            var templateView = template.TemplateView();
        }
    },

    render: function () {
        this.$el.show();
        return this;
    }
});

return {
    DocumentView: function () {
        return new DocumentView();
    }
};


});
