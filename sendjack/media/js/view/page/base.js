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
            'backbone'

            //modules
            //jquery ui
        ],
        function ($, Backbone) {


var PageView = Backbone.Marionette.CompositeView.extend({

    initialize: function () {
        // This bypasses Marionette's templates.
        this.template = this.el.html;

        // Setup page DOM
        var datepicker = this.$('.datepicker').datepicker({minDate: '0'});
        
        // cancel form submissions
        this.$('form button[type=submit]').click(function (event) {
            event.preventDefault();
        });
    }
});

return {
    getPageViewClass: function () {
        return PageView;
    }
};


});
