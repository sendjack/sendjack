/**
 * Access the Create Instance Series.
 *
 * @exports controller.createInstance
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
            'model/customer',
            'model/instance',
            'view/region',
            'view/page/search',
            'view/page/createInstance',
            'view/page/createCustomer',
            'view/page/createInstanceThanks'

            //jquery ui
        ],
        function (
                $,
                Backbone,
                event,
                customerModel,
                instanceModel,
                region,
                searchView,
                createInstanceView,
                createCustomerView,
                createInstanceThanksView) {


var CreateInstanceController = Backbone.Marionette.Controller.extend({

    region: null,

    customerModel: null,
    instanceModel: null,

    searchPage: null,
    createInstancePage: null,
    createCustomerPage: null,
    createInstanceThanksPage: null,

    pagesSelector: '#search-page, #create-instance-page, #create-customer-page, #create-instance-thanks-page',

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
        this.customerModel = customerModel.CustomerModel();
        this.instanceModel = instanceModel.TaskInstanceModel();

        // TODO: Set this somewhere else.
        this.instanceModel.set('status', 'created');
        this.customerModel.set('status', 'registered');

        this.instanceModel.on(
            'change:customer_title',
            function (model, value) {
                this.instanceModel.set('title', value);
            }, this);

        this.instanceModel.on(
            'change:customer_description',
            function (model, value) {
                this.instanceModel.set('summary', value);
            }, this);

        // TODO: Use Backbone relational for stuff like this.
        this.customerModel.on('change:id', function (model, value) {
            this.instanceModel.set('customer_id', value);

            if (!this.instanceModel.isNew()) {
                this.instanceModel.save();
            }
        }, this);

        
    },

    initializePages: function () {
        this.searchPage = searchView.SearchPageView({
            instanceModel: this.instanceModel
        });
        this.createInstancePage = createInstanceView.CreateInstancePageView({
            instanceModel: this.instanceModel
        });
        this.createCustomerPage = createCustomerView.CreateCustomerPageView({
            customerModel: this.customerModel
        });
        this.createInstanceThanksPage = createInstanceThanksView
                .CreateInstanceThanksPageView();
    },

    /**
     * Catch any transition events and navigate to next page.
     *
     * ORDER: Search --> Create Task --> Create Customer --> Thanks
     */
    initializeTransitions: function () {
        this.instanceModel.once(event.SAVE, function () {
            Backbone.history.navigate('/users/create', {trigger: true});
        });

        this.customerModel.once(event.SAVE, function () {
            Backbone.history.navigate('/tasks/create/thanks', {trigger: true});
        });
    },

    loadSearchPage: function () {
        this.region.show(this.searchPage);
    },

    loadCreateInstancePage: function () {
        this.region.show(this.createInstancePage);
    },

    loadCreateCustomerPage: function () {
        this.region.show(this.createCustomerPage);
    },

    loadCreateInstanceThanksPage: function () {
        this.region.show(this.createInstanceThanksPage);
    }
});


/** Make sure CreateInstanceController is a singleton. */
var createInstanceController = null;

return {
    CreateInstanceController: function () {
        if (createInstanceController === null) {
            createInstanceController = new CreateInstanceController();
        }

        return createInstanceController;
    }
};


});
