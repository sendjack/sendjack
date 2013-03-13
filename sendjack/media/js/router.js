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
            'controller/createInstance',
            'controller/processInstance',
            'controller/confirmInstance'
            //'controller/approveInstance'

            //jquery ui
        ],
        function (
                Backbone,
                createInstance,
                processInstance,
                confirmInstance,
                approveInstance) {


/** Every router has a single controller. */
var createInstanceController = createInstance.CreateInstanceController();
var processInstanceController = processInstance.ProcessInstanceController();
var confirmInstanceController = confirmInstance.ConfirmInstanceController();
//var approveInstanceController = approveInstance.ApproveInstanceController();


var CreateInstanceRouter = Backbone.Marionette.AppRouter.extend({

    controller: createInstanceController,

    appRoutes: {
        'tasks/create': 'loadCreateInstancePage',
        'users/create': 'loadCreateCustomerPage',
        'tasks/create/thanks': 'loadCreateInstanceThanksPage'
    }
});


var ProcessInstanceRouter = Backbone.Marionette.AppRouter.extend({

    controller: processInstanceController,

    appRoutes: {
        'tasks/:id/process': 'loadProcessInstancePage'
    }
});


var ConfirmInstanceRouter = Backbone.Marionette.AppRouter.extend({

    controller: confirmInstanceController,

    appRoutes: {
        'tasks/:id/confirm': 'loadConfirmInstancePage',
        'users/:id/card': 'loadCardCustomerPage',
        'tasks/:id/confirm/thanks': 'loadConfirmInstanceThanksPage'
    }
});

/** var ApproveInstanceRouter = Backbone.Marionette.AppRouter.extend({

    controller: approveInstanceController,

    appRoutes: {
        'tasks/:id/approve': '',
        'tasks/:id/approve/thanks': ''
    }
});
 */
/** Make sure the routers are singletons. */
var createInstanceRouter = null;
var processInstanceRouter = null;
var confirmInstanceRouter = null;
var approveInstanceRouter = null;

return {
    CreateInstanceRouter: function () {
        if (createInstanceRouter === null) {
            createInstanceRouter= new CreateInstanceRouter();
        }

        return createInstanceRouter;
    },

    ProcessInstanceRouter: function () {
        if (processInstanceRouter === null) {
            processInstanceRouter= new ProcessInstanceRouter();
        }

        return processInstanceRouter;
    },

   ConfirmInstanceRouter: function () {
        if (confirmInstanceRouter === null) {
            confirmInstanceRouter = new ConfirmInstanceRouter();
        }

        return confirmInstanceRouter;
    }

    /**ApproveInstanceRouter: function () {
        if (approveInstanceRouter === null) {
            approveInstanceRouter= new ApproveInstanceRouter();
        }

        return approveInstanceRouter;
    } */
};


});