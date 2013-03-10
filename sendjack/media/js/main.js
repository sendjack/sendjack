/**
 * Use RequireJS to run Jackalope.
 *
 * For help on using main.js: http://requirejs.org/docs/api.html#jsfiles
 *
 * Plugins:
 * N/A
 *
 * @module main
 * @requires app
 *
 */
require.config({
    paths: {
        // Core libraries
        jquery: 'https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min',
        underscore: 'http://cdnjs.cloudflare.com/ajax/libs/lodash.js/1.0.0-rc.3/lodash.min',
        backbone: 'libs/backbone/backbone',
        stripe: 'libs/stripe/stripe',
        mp: 'libs/mixpanel/mixpanel',

        // Backbone Plugins
        marionette: 'libs/backbone/backbone.marionette',
        'backbone.wreqr': 'libs/backbone/backbone.wreqr',
        'backbone.babysitter': 'libs/backbone/backbone.babysitter',
        modelbinder: 'http://cdnjs.cloudflare.com/ajax/libs/backbone.modelbinder/0.1.3/Backbone.ModelBinder-min',

        // jQuery Plugins
        jqueryui: 'libs/jquery/jquery-ui',
        validation: 'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.11.0/jquery.validate.min'
    },

    shim: {
        backbone: {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },

        jqueryui: {
            deps: ['jquery'],
            exports: 'jqueryui'
        },

        validation: {
            deps: ['jquery'],
            exports: 'validation'
        },

        modelbinder: {
            deps: ['backbone'],
            exports: 'ModelBinder'
        },

        stripe: {
            exports: 'Stripe'
        }
    }

});

require([
        // application
        'app',

        // one time libraries that modify other libraries
        'jquery',
        'jqueryui',
        'validation',
        'backbone',
        'marionette'

], function (app) {
    app.start();
});
