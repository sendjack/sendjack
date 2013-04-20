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

        // slide section up
        var $section = this.$el.find('.main-section');
        var negativeSectionHeight = parseInt(-($section.outerHeight()), 10) + 'px';
        $section.css('top', negativeSectionHeight);

        // make it visible (though occluded)
        this.$el.css('visibility', 'visible');

        // slide section down
        $section.animate({top: '0px'}, {
            duration: 1000,
            complete: callback
        });
    },

    /** Define a hide transition. */
    hide: function (callback) {
        var $section = this.$el.find('.main-section');
        var sectionHeight = $section.outerHeight();
        var sectionHeightStr = parseInt(-sectionHeight, 10) + 'px';

        // hide page
        $section.animate({top: sectionHeightStr}, {
            duration: 'slow',
            complete: function () {
                // after hide scroll to top
                $('html, body').animate({scrollTop: 0}, {
                    duration: 'slow'
                });

                // putting this callback in the scrollTop animate function
                // causes the upcoming form to switch to synchronous
                // submitting.
                callback();
            }
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
