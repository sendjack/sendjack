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
            'view/object/customer',
            'view/object/instance'

            //jquery ui
        ],
        function ($, Backbone, event, track, customer, instance) {


var CreateInstanceSeriesView = Backbone.View.extend({

    customerView: null,
    instanceView: null,
    customerModel: null,
    instanceModel: null,

    $currPage: null,
    $instanceCreatePage: null,
    $customerCreatePage: null,
    $instanceCreateThanksPage: null,


    initialize: function (router) {
        this.setElement('.alt-content');

        this.initializeObjects();
        this.initializePages();

        this.customerModel.once(event.SAVE, function () {
            router.navigate('/tasks/create/thanks', {trigger: true});
        });
        this.instanceModel.once(event.SAVE, function () {
            router.navigate('/users/create', {trigger: true});
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
        this.$instanceCreatePage = this.$el.find('#instance-create-page');
        this.$customerCreatePage = this.$el.find('#customer-create-page');
        this.$instanceCreateThanksPage = this.$el.find(
                '#instance-create-thanks-page');

        var pages = [
            this.$instanceCreatePage,
            this.$customerCreatePage,
            this.$instanceCreateThanksPage
        ];

        $.each(pages, function (index, $page) {
            // $.show() and $.fadeIn() revert to the last display state.
            $page.detach().css('display', 'block').hide();
        });
    },

    transitionPages: function (newPage) {
        // all this junk is necessary to fade the next page in.
        if (this.$currPage) {
            this.$currPage.detach();
        }
        this.$currPage = newPage;
        this.$el.append(newPage);
        newPage.fadeIn();

        track.viewPage(window.location.pathname);

        return newPage;
    },

    loadInstanceCreatePage: function () {
        this.transitionPages(this.$instanceCreatePage);
    },

    loadCustomerCreatePage: function () {
        this.transitionPages(this.$customerCreatePage);
    },

    loadInstanceCreateThanksPage: function () {
        this.transitionPages(this.$instanceCreateThanksPage);
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

/** Make sure CreateInstanceSeriesView is a singleton. */
var createInstanceSeriesView = null;

return {
    CreateInstanceSeriesView: function (router) {
        if (createInstanceSeriesView === null) {
            createInstanceSeriesView = new CreateInstanceSeriesView(router);
        }

        return createInstanceSeriesView;
    }
};


});
