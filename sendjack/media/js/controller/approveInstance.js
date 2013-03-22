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
            'view/page/approveInstanceThanks'
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
                approveInstanceThanksView) {


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
    },

    initializeTransitions: function () {
        // when instnace view is saved then navigate
        this.instanceModel.once(event.SAVE, function () {
            var id = this.instanceModel.id;
            var path = '/tasks/' + id + '/approve/thanks';
            Backbone.history.navigate(path, {trigger: true});
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
