/**
 * Provide a router for async page changes.
 *
 * @exports router
 *
 * @requires $
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'jquery',
            'lodash',
            'backbone',

            //modules
            'controller/createInstance'
            //jquery ui
        ],
        function ($, _, Backbone, createInstanceController) {


var AppRouter = Backbone.Router.extend({

    /** Initialize all non-page specific functionality. */
    initialize: function () {
        var datepicker = $('.datepicker').datepicker({minDate: '0'});
        
        // cancel form submissions
        $('form button[type=submit]').click(function (event) {
            event.preventDefault();
        });
    },

    routes: {
        'tasks/create': 'loadInstanceCreate',
        'users/create': 'loadCustomerCreate',
        'tasks/create/thanks': 'loadInstanceCreateThanks'

    },

    loadInstanceCreate: function () {
        var controller = createInstanceController.CreateInstanceSeriesView(this);
        controller.loadInstanceCreatePage();
    },

    loadCustomerCreate: function () {
        var controller = createInstanceController.CreateInstanceSeriesView(this);
        controller.loadCustomerCreatePage();
    },

    loadInstanceCreateThanks: function () {
        var controller = createInstanceController.CreateInstanceSeriesView(this);
        controller.loadInstanceCreateThanksPage();
    }

});

/** Make sure router is a singleton. */
var appRouter = null;

return {
    AppRouter: function () {
        if (appRouter === null) {
            appRouter = new AppRouter();
            
            var options = {
                pushState: true
            };

            Backbone.history.start(options);
        }

        return appRouter;
    }

};

});
