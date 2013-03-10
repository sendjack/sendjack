/**
 * The entire Jackalope client side application.
 *
 * DEPENDENCIES:
 * 1. RequireJS: http://requirejs.org
 * 2. Backbone: http://backbonejs.org
 *
 * CONVENTIONS:
 * 1. Douglas Crockford: http://javascript.crockford.com/code.html
 * 2. JSDocs
 * 3. $NAME: jQuery variable
 *
 * @exports app
 * @requires $
 */
require(
        [
            // libraries
            'jquery',

            // modules
            'util/track',
            'router',

            // one-time instantiators
            'jqueryui',
            'validation'
        ],
        function ($, track, router) {

console.log($);
console.log(track);
console.log(router);

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


/**
 * Initialize Environment.
 */
var initializeEnvironment = (function () {
    // Make sure AJAX requests are not cached.
    $.ajaxSetup({cache: false});

})();


/**
 * Initialize Application.
 */
var initializeApp = (function () {
    $(document).ready(function () {
        var appRouter = router.AppRouter();
    });
})();


});
