/**
 * Access the Confirm Instance Series.
 *
 * @exports controller.confirmInstance
 *
 * @requires $
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',

            //modules
            'event',
            'util/track',
            'view/item/customer',
            'view/item/instance'

            //jquery ui
        ],
        function ($, Backbone, event, track, customer, instance) {


var ConfirmInstanceController = Backbone.Marionette.Controller.extend({

});


/** Make sure ConfirmInstanceController is a singleton. */
var confirmInstanceController = null;

return {
    ConfirmInstanceController: function () {
        if (confirmInstanceController === null) {
            confirmInstanceController = new ConfirmInstanceController();
        }

        return confirmInstanceController;
    }
};


});
