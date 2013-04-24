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
        jquery: 'libs/jquery/jquery',
        underscore: 'libs/lodash/lodash',
        backbone: 'libs/backbone/backbone',
        stripe: 'libs/stripe/stripe',
        mp: 'libs/mixpanel/mixpanel',

        // Backbone Plugins
        marionette: 'libs/backbone/backbone.marionette',
        'backbone.wreqr': 'libs/backbone/backbone.wreqr',
        'backbone.babysitter': 'libs/backbone/backbone.babysitter',
        modelbinder: 'libs/backbone/backbone.modelbinder',

        // jQuery Plugins
        jqueryui: 'libs/jquery/jquery.ui',
        validation: 'libs/jquery/jquery.validate'
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
