/**
 * Access the Confirm Instance Series.
 *
 * @exports controller.confirmInstance
 *
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
            'model/creditCard',
            'view/page/confirmInstance',
            'view/page/cardCustomer',
            'view/page/confirmInstanceThanks'

            //jquery ui
        ],
        function (
                $,
                Backbone,
                event,
                track,
                customerModel,
                instanceModel,
                creditCardModel,
                confirmInstanceView,
                cardCustomerView,
                confirmInstanceThanksView) {


var ConfirmInstanceController = Backbone.Marionette.Controller.extend({

    region: null,

    customerModel: null,
    instanceModel: null,

    confirmInstancePage: null,
    cardCustomerPage: null,
    confirmInstanceThanksPage: null,

    pagesSelector: '#confirm-instance-page, #card-customer-page, #confirm-instance-thanks-page',

    initialize: function () {
        if ($(this.pagesSelector).length) {
            this.region = new Backbone.Marionette.Region({
                el: '.content'
            });

            this.initializeModels();
            this.initializePages();
            this.initializeTransitions();
        }
    },

    initializeModels: function () {
        // get ID from Router
        this.instanceModel = instanceModel.TaskInstanceModel();
        this.customerModel = customerModel.CustomerModel();
        this.creditCardModel = creditCardModel.CreditCardModel();

        this.instanceModel.on('change:customer_id', function (model, value) {
            this.customerModel.resetID(value);
        }, this);

        // FIXME XXX: This should be in the internal task update controller
        this.instanceModel.on('change:price', function (model) {
            if (!model.previous('price')) {
                model.set('status', 'processed');
            }
        });

        // once the customer is pulled from server show the correct fields.
        this.customerModel.once(
                'change:control_group',
                function (model, value) {
                    var taskStatus = this.instanceModel.get('status');
                    this.confirmInstancePage.confirmInstanceObjectView.
                            setupControlAndTestFields(value, taskStatus);
                },
                this);

        // when the credit card is saved then update the customer
        this.creditCardModel.on('change:stripe_token', function (model, value) {
            this.customerModel.set('stripe_token', value);
        }, this);

    },

    initializePages: function () {
        this.confirmInstancePage = confirmInstanceView.ConfirmInstancePageView({
            instanceModel: this.instanceModel
        });
        this.cardCustomerPage = cardCustomerView.CardCustomerPageView({
            customerModel: this.customerModel,
            creditCardModel: this.creditCardModel
        });
        this.confirmInstanceThanksPage = confirmInstanceThanksView
                .ConfirmInstanceThanksPageView();
    },

    initializeTransitions: function () {
        // when customer view is saved then update task view
        this.customerModel.once(event.SAVE, this.onCardedCustomer, this);

        // when task instance view is saved then render next page
        this.instanceModel.once(event.SAVE, function () {
            var id = this.customerModel.id;
            var path = '/users/' + id + '/card';
            Backbone.history.navigate(path, {trigger:true});
        }, this);

    },

    loadConfirmInstancePage: function (instanceID) {
        var id = parseInt(instanceID, 10);
        if (this.instanceModel.isNew()) {
            this.instanceModel.resetID(id);
        }

        this.region.show(this.confirmInstancePage);
    },

    loadCardCustomerPage: function (customerID) {
        var id = parseInt(customerID, 10 );
        if (this.customerModel.isNew()) {
            this.customerModel.resetID(id);
        }

        this.region.show(this.cardCustomerPage);
    },

    loadConfirmInstanceThanksPage: function (instanceID) {
        var id = parseInt(instanceID, 10);
        if (this.instanceModel.isNew()) {
            this.instanceModel.resetID(id);
        }

        this.region.show(this.confirmInstanceThanksPage);
    },

    onCardedCustomer: function (model, options) {
        track.addCreditCard(this.instanceModel.get('price'));

        this.instanceModel.set('status', 'confirmed');
        this.instanceModel.once(event.SAVE, this.onConfirmedTask, this);
        this.instanceModel.save();
    },

    onConfirmedTask: function (model, options) {
        track.postTask(model.get('id'), model.get('price'));
        var id = this.instanceModel.id;
        var path = '/tasks/' + id + '/confirm/thanks';
        Backbone.history.navigate(path, {trigger: true});
    }
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
