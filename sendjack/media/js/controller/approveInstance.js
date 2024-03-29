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
            'model/customer',
            'model/instance',
            'view/region',
            'view/page/approveInstance',
            'view/page/approveInstanceThanks',
            'view/page/rejectInstanceThanks'
        ],
        function (
                $,
                Backbone,
                event,
                track,
                customerModel,
                instanceModel,
                region,
                approveInstanceView,
                approveInstanceThanksView,
                rejectInstanceThanksView) {


var ApproveInstanceController = Backbone.Marionette.Controller.extend({

    region: null,

    customerModel: null,
    instanceModel: null,

    approveInstancePage: null,
    approveInstanceThanksPage: null,

    pagesSelector: '#approve-instance-page, #approve-instance-thanks-page',

    initialize: function () {
        if ($(this.pagesSelector).length) {
            this.region = region.AppRegion({
                el: '#page-container'
            });

            this.initializeModels();
            this.initializePages();
            this.initializeTransitions();
        }
    },

    initializeModels: function () {
        this.instanceModel = instanceModel.TaskInstanceModel();
        this.customerModel = customerModel.CustomerModel();

        this.instanceModel.on('change:customer_id', function (model, value) {
            this.customerModel.resetID(value);
        }, this);

        // once the customer is pulled from server show the correct fields.
        this.customerModel.once(
                'change:control_group',
                function (model, value) {
                    this.approveInstancePage.approveInstanceObjectView.
                            setupControlAndTestFields(value);
                },
                this);
    },

    initializePages: function () {
        this.approveInstancePage = approveInstanceView.ApproveInstancePageView({
            instanceModel: this.instanceModel
        });
        this.approveInstanceThanksPage = approveInstanceThanksView
                .ApproveInstanceThanksPageView();
        this.rejectInstanceThanksPage = rejectInstanceThanksView
                .RejectInstanceThanksPageView();
    },

    initializeTransitions: function () {
        this.instanceModel.once(event.SAVE, function (model, options) {
            var status = model.get('status');
            if (status === 'approved') {
                this.onApprovedInstance(model, options);
            } else if (status === 'rejected') {
                this.onRejectedInstance(model, options);
            }
        }, this);
    },

    loadApproveInstancePage: function (instanceID) {
        var id = parseInt(instanceID, 10);
        if (this.instanceModel.isNew()) {
            this.instanceModel.resetID(id);
        }

        this.region.show(this.approveInstancePage);
    },

    loadApproveInstanceThanksPage: function (instanceID) {
        var id = parseInt(instanceID, 10);
        if (this.instanceModel.isNew()) {
            this.instanceModel.resetID(id);
        }

        this.region.show(this.approveInstanceThanksPage);
    },

    loadRejectInstanceThanksPage: function (instanceID) {
        var id = parseInt(instanceID, 10);
        if (this.instanceModel.isNew()) {
            this.instanceModel.resetID(id);
        }

        this.region.show(this.rejectInstanceThanksPage);
    },

    onApprovedInstance: function (model, options) {
        var id = model.id;

        track.approveTask(id, model.get('price'));

        var path = '/tasks/' + id + '/approve/thanks';
        Backbone.history.navigate(path, {trigger: true});
    },

    onRejectedInstance: function (model, options) {
        var id = model.id;
        
        track.rejectTask(id, model.get('price'));

        var path = '/tasks/' + id + '/reject/thanks';
        Backbone.history.navigate(path, {trigger: true});
   }
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
