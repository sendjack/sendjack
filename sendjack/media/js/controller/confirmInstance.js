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
            'view/region',
            'view/page/confirmInstance',
            'view/page/cardCustomer',
            'view/page/confirmInstanceThanks'
        ],
        function (
                $,
                Backbone,
                event,
                track,
                customerModel,
                instanceModel,
                creditCardModel,
                region,
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
            this.region = region.AppRegion({
                el: '#page-container'
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

        // once the customer is pulled from server show the correct fields.
        this.customerModel.once(
                'change:control_group',
                function (model, value) {
                    this.confirmInstancePage.confirmInstanceObjectView.
                            setupControlAndTestFields(value);
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
        var id = model.id;

        track.postTask(id, model.get('price'));

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
