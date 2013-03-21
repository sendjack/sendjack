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

    show: function (callback) {
        // non-displayed page should be hidden and shown to get page height
        this.$el.css('visibility', 'hidden');
        this.$el.show();

        // slide page up
        var negativePageHeight = parseInt(-(this.$el.height()), 10) + 'px';
        this.$el.css('top', negativePageHeight);

        // make it visible (though occluded)
        this.$el.css('visibility', 'visible');

        // slide page down
        this.$el.animate({top: '0px'}, {
            duration: 1000,
            complete: callback
        });
    },

    /** Define a hide transition. */
    hide: function (callback) {
        var pageHeight = this.$el.height();
        var pageHeightStr = parseInt(-pageHeight, 10) + 'px';

        this.$el.animate({top: pageHeightStr}, {
            duration: 'fast',
            complete: callback
        });


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
