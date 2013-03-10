/**
 * Provide routers.
 *
 * @exports router
 *
 * @requires $
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'backbone',

            //modules
            'controller/createInstance'
            //'controller/confirmInstance',
            //'controller/approveInstance'

            //jquery ui
        ],
        function (Backbone, createInstance, confirmInstance, approveInstance) {


/** Every router has a single controller. */
var createInstanceController = createInstance.CreateInstanceController();
// var confirmInstanceController = confirmInstance.ConfirmInstanceController();
//var approveInstanceController = approveInstance.ApproveInstanceController();


var CreateInstanceRouter = Backbone.Marionette.AppRouter.extend({

    controller: createInstanceController,

    appRoutes: {
        'tasks/create': 'loadCreateInstancePage',
        'users/create': 'loadCreateCustomerPage',
        'tasks/create/thanks': 'loadCreateInstanceThanksPage'
    }
});


/** var ConfirmInstanceRouter = Backbone.Marionette.AppRouter.extend({

    controller: confirmInstanceController,

    appRoutes: {
        'tasks/:id/confirm': 'loadConfirmInstancePage',
        'users/:id/card': 'loadCardCustomerPage',
        'tasks/:id/confirm/thanks': 'loadConfirmInstanceThanksPage'
    }
});

var ApproveInstanceRouter = Backbone.Marionette.AppRouter.extend({

    controller: approveInstanceController,

    appRoutes: {
        'tasks/:id/approve': '',
        'tasks/:id/approve/thanks': ''
    }
});
 */
/** Make sure the routers are singletons. */
var createInstanceRouter = null;
var confirmInstanceRouter = null;
var approveInstanceRouter = null;

return {
    CreateInstanceRouter: function () {
        if (createInstanceRouter === null) {
            createInstanceRouter= new CreateInstanceRouter();
        }

        return createInstanceRouter;
    }

    /** ConfirmInstanceRouter: function () {
        if (confirmInstanceRouter === null) {
            confirmInstanceRouter = new ConfirmInstanceRouter();
        }

        return confirmInstanceRouter;
    },

    ApproveInstanceRouter: function () {
        if (approveInstanceRouter === null) {
            approveInstanceRouter= new ApproveInstanceRouter();
        }

        return approveInstanceRouter;
    } */
};


});
