/**
 * Provide a base app region.
 *
 * @exports view.region
 *
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'backbone'

            //modules
        ],
        function (Backbone) {


var AppRegion = Backbone.Marionette.Region.extend({

    // show, open, and close reference these examples for transitions:
    // github.com/marionettejs/backbone.marionette/blob/master/src/marionette.region.js
    // github.com/marionettejs/backbone.marionette/issues/320#issuecomment-9746319
    show: function (view) {
        this.ensureEl();
        view.render();

        var that = this;
        this.close(function () {
            if (that.currentView && that.currentView !== view) {
                return ;
            }
            that.currentView = view;

            that.open(view, function() {
                Backbone.Marionette.triggerMethod.call(view, "show");
                Backbone.Marionette.triggerMethod.call(that, "show", view);
            });
        });

    },

    /**
     * Open the new view and allow for animation.
     */
    open: function (view, callback) {
        var that = this;
        this.$el.html(view.$el.hide());
        view.show(function (){
            callback.call(that);
        });
    },

    /**
     * Close the region and allow for the view to animate it's hide.
     */
    close: function (callback) {
        var view = this.currentView;
        delete this.currentView;

        if (!view) {
            if (callback) {
                callback.call(this);
                return;
            }
        }

        var that = this;
        view.hide(function () {
            // make sure that the view is closed and onClose is called
            if (view.close) {
                view.close();
            }
            Backbone.Marionette.triggerMethod.call(that, "close");

            // finish the show request through callback after the animation
            if (callback) {
                callback.call(that);
            }
        });
    }
});

return {
    AppRegion: function (options) {
        return new AppRegion(options);
    }
};


});
