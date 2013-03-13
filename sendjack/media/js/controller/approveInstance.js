/**
 * Access the Approve Instance Series.
 *
 * @exports controller.approveInstance
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


var ApproveInstanceController = Backbone.Marionette.Controller.extend({

});


/** Make sure ApproveInstanceController is a singleton. */
var approveInstanceController = null;

return {
    ApproveInstanceController: function () {
        if (approveInstanceController === null) {
            approveInstanceController = new ApproveInstanceController();
        }

        return approveInstanceController;
    }
};


});

