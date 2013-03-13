/**
 * The entire Jackalope client side application.
 *
 * DEPENDENCIES:
 * 1. RequireJS: http://requirejs.org
 * 2. Backbone: http://backbonejs.org
 * 3. Marionette: http://marionettejs.org
 *
 * CONVENTIONS:
 * 1. Douglas Crockford: http://javascript.crockford.com/code.html
 * 2. JSDocs
 * 3. $NAME: jQuery variable
 *
 * @exports app
 * @requires $
 */
define([], function () {

// Delay application until jQuery and Backbone plugins have been loaded
return {
    start: function () {require(
        [
            // libraries
            'jquery',
            'backbone',

            // modules
            'util/track',
            'router'
        ], function ($, Backbone, track, router) {
                        

            /**
             * Initialize Object with superpowers per Crockford's recommendation.
             * 1. Object.create: http://javascript.crockford.com/prototypal.html
             */
            var initializeObject = (function () {
                if (typeof Object.create !== 'function') {
                    Object.create = function (o) {
                        function F() {}
                        F.prototype = o;
                        return new F();
                    };
                }
            })();


            /** Initialize Environment. */
            var initializeEnvironment = (function () {

                // Make sure AJAX requests are not cached.
                $.ajaxSetup({cache: false});

                // Turn off template loading for Marionette.
                Backbone.Marionette.Renderer.render = function (template, data) {
                    return template;
                };
            })();


            var sendjack = new Backbone.Marionette.Application();


            /** Add all the routers to the application. */
            sendjack.addInitializer(function (options) {
                var createInstanceRouter = router.CreateInstanceRouter();
                var confirmInstanceRouter = router.ConfirmInstanceRouter();
                //var approveInstanceRouter = router.ApproveInstanceRouter();

                Backbone.history.start({pushState: true});
            });

            $(document).ready(function () {sendjack.start();});
        });
    }
};


});
