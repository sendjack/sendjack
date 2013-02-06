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
        jquery: 'https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min',
        lodash:
            'http://cdnjs.cloudflare.com/ajax/libs/lodash.js/1.0.0-rc.3/lodash.min',
        backbone: 'libs/backbone/backbone',

        jqueryui: 'libs/jquery/jquery-ui'
    },
    shim: {
        'backbone': {
            deps: ['lodash', 'jquery'],
            exports: 'Backbone'
        },

        'jqueryui': {
            deps: ['jquery'],
            exports: 'jqueryui'
        }
    }

});

require([
        'app2'
]);
