/**
 * Access the Create Instance Series.
 *
 * @exports controller.createInstance
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
            'view/page/createInstance',
            'view/page/createCustomer',
            'view/page/createInstanceThanks',
            'view/item/customer',
            'view/item/instance'

            //jquery ui
        ],
        function (
                $,
                Backbone,
                event,
                track,
                createInstance,
                createCustomer,
                createInstanceThanks,
                customer,
                instance) {


var CreateInstanceController = Backbone.Marionette.Controller.extend({

    region: null,

    customerView: null,
    instanceView: null,
    customerModel: null,
    instanceModel: null,

    $currPage: null,
    createInstancePage: null,
    createCustomerPage: null,
    createInstanceThanksPage: null,


    initialize: function () {
        this.region = new Backbone.Marionette.Region({
            el: '.alt-content'
        });

        this.initializeObjects();
        this.initializePages();

        this.customerModel.once(event.SAVE, function () {
            Backbone.history.navigate('/tasks/create/thanks', {trigger: true});
        });
        this.instanceModel.once(event.SAVE, function () {
            Backbone.history.navigate('/users/create', {trigger: true});
        });
    },

    initializeObjects: function () {
        this.customerView = SignUpCustomerView();
        this.instanceView = TaskInstanceSaveView();
        this.customerModel = this.customerView.model;
        this.instanceModel = this.instanceView.model;

        this.customerModel.on('change:id', function (model) {
            var id = model.get('id');
            var email = model.get('email');
            this.instanceModel.set('customer_id', id);
        }, this);
    },

    initializePages: function () {
        this.createInstancePage = createInstance.CreateInstancePageView();
        this.createCustomerPage = createCustomer.CreateCustomerPageView();
        this.createInstanceThanksPage = createInstanceThanks
                .CreateInstanceThanksPageView();

        var pages = [
            this.createInstancePage,
            this.createCustomerPage,
            this.createInstanceThanksPage
        ];

        $.each(pages, function (index, view) {
            // $.show() and $.fadeIn() revert to the last display state.
            view.$el.detach().css('display', 'block');
        });
    },

    transitionPages: function (newPage) {
        this.region.show(newPage);
        track.viewPage(window.location.pathname);

        return newPage;
    },

    loadCreateInstancePage: function () {
        this.transitionPages(this.createInstancePage);
    },

    loadCreateCustomerPage: function () {
        this.transitionPages(this.createCustomerPage);
    },

    loadCreateInstanceThanksPage: function () {
        this.transitionPages(this.createInstanceThanksPage);
    }
});


var TaskInstanceView = instance.getTaskInstanceViewClass();
function TaskInstanceSaveView(attributes, options) {
    var TaskInstanceSaveViewClass = TaskInstanceView.extend({

        addRequiredValidationRules: function () {
            this.$el.validate({
                rules: {
                    customer_title: 'required',
                    customer_description: 'required',
                    deadline_ts: 'required'
                }
            });
        }

    });

    return new TaskInstanceSaveViewClass(attributes, options);
}


var CustomerView = customer.getCustomerViewClass();
function SignUpCustomerView(attributes, options) {
    var SignUpCustomerViewClass = CustomerView.extend({

        initialize: function (attributes, options) {
            CustomerView.prototype.initialize.call(this, attributes, options);

            this.model.on('change:stripe_token', this.onAttributeChange, this);
        },

        addRequiredValidationRules: function () {
            console.log(this.$el);
            this.$el.validate({
                rules: {
                    first_name: 'required',
                    last_name: 'required',
                    email: 'required'
                }
            });
        },

        onAttributeChange: function (model, value, options) {
            this.save();
        }
    });

    return new SignUpCustomerViewClass(attributes, options);
}

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
