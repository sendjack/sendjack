/**
 * Provide a base class for page views.
 *
 * @exports view.page.base
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',

            //modules
            'util/track'
            //jquery ui
        ],
        function ($, Backbone, track) {


var PageView = Backbone.Marionette.CompositeView.extend({

    initialize: function () {

        // This bypasses Marionette's templates.
        this.template = this.el.html;

        // Setup page DOM
        var datepicker = this.$('.date-picker').datepicker({minDate: '0'});
        
        // cancel form submissions
        this.$('form button[type=submit]').click(function (event) {
            event.preventDefault();
        });

        // subclasses load child views here
        this._initializeChildViews();

        // Child View will need to see DOM first.
        // Detach and and set to block for easy attachment.
        this.$el.detach().css('display', 'block');
    },

    /** Loads the Child Views from the DOM before the el is detached. */
    _initializeChildViews: function () {
    },

    /** Called by Marionette when the View is shown. */
    onShow: function () {
        track.viewPage(window.location.pathname);
    }
});

return {
    getPageViewClass: function () {
        return PageView;
    }
};


});
