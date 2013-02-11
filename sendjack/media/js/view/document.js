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
            'view/customer',
            'view/instance',
            'view/template',

            //jquery ui
            'jqueryui'
        ],
        function ($, Backbone, customer, instance, template) {


var DocumentView = Backbone.View.extend({

    initialize: function () {
        //this.setElement('#karma');

        var datepicker = $('.datepicker').datepicker();

        if ($('#template').length !== 0) {
            var taskTemplateView = template.TaskTemplateView();
        }

        if ($('#instance').length !== 0) {
            var taskInstanceView = instance.TaskInstanceView();
        }

        if ($('#customer').length !== 0) {
            var customerView = customer.CustomerView();
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
