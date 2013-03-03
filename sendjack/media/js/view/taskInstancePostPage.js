/**
 * Access the Task Instance Post Page.
 *
 * @exports view.taskInstancePostPage
 *
 * @requires $
 * @requires Backbone
 * @requires view.instance
 * @requires view.customer
 *
 */
define(
        [
            // libraries
            'jquery',
            'backbone',

            // modules
            'event',
            'view/instance',
            'view/customer',
            'view/payment'

            // jquery ui
        ],
        function ($, Backbone, event, instance, customer, payment) {


var TaskInstancePostPage = Backbone.View.extend({

    $currGrid: null,
    taskInstanceView: null,
    customerView: null,

    initialize: function () {
        this.setElement('.task-instance-post-page');

        this.taskInstanceView = TaskInstancePostView();


        // wait until after the instance data is fetched to grab customer id.
        var that = this;
        this.taskInstanceView.model.on('change:customer_id', function (model) {

            // Create the Customer View with the customer_id
            var customerID = model.get('customer_id');
            that.customerView = PostCustomerView({model_id: customerID});

            // Create the credit card view with the Customer Model
            var $creditCard = that.$el.find('#credit-card-grid');
            var creditCardView = payment.CreditCardView(
                    {
                        el: $creditCard,
                        customerModel: that.customerView.model
                    });

            // when credit card view is saved then update customer view
            // credit card isn't model backed so the event is tied to the view
            creditCardView.once(
                    event.SAVE,
                    that.updateCustomer,
                    that);

        });

        // when task instance view is saved then render next page
        this.taskInstanceView.model.once(event.SAVE, this.render, this);

          
        // remove the grids so we can show them one by one
        this.gridList = [
            this.$el.find('#task-instance-grid').detach(),
            this.$el.find('#credit-card-grid').detach(),
            this.$el.find('#thank-you-grid').detach()
        ];
        
        // all this junk is necessary to fade the next page in.
        // $.show() and $.fadeIn() revert to the last display state.
        $.each(this.gridList, function (index, $grid) {
            $grid.css('display', 'block').hide();
            that.$el.find('.contrast-section').append($grid);
        });


        // TODO: add support for inserting new step fields on focus.

        this.render();
    },

    events: function () {
        var _events = {};

        //_events['click #task-insance-grid .submit-button'] = 'renderCreditCard';
        //_events['click #credit-card-grid .submit-button'] = 'renderThankYou';

        return _events;
    },

    render: function () {
        this.$el.show();
        if (this.$currGrid !== null) {
            this.$currGrid.hide();
        }

        this.$currGrid = this.gridList.shift();
        this.$currGrid.fadeIn();

        return this;
    },

    updateCustomer: function () {
        // when customer view is saved then update task view
        this.customerView.model.once(
                event.SAVE,
                this.updateTaskInstance,
                this);

        this.customerView.save();
    },

    updateTaskInstance: function (color) {
        console.log(color);
        this.taskInstanceView.setStatus("created");
        this.taskInstanceView.model.once(event.SAVE, this.render, this);
        this.taskInstanceView.save();
    }
});


var TaskInstanceView = instance.getTaskInstanceViewClass();
function TaskInstancePostView(attributes, options) {
    var TaskInstancePostViewClass = TaskInstanceView.extend({

        initialize: function () {
            TaskInstanceView.prototype.initialize.call(this);
           
            // TODO: make an iterable of fields to hide/disable?

            this.$el.find('.customer-title').hide();
            this.$el.find('.customer-description').hide();

            this.$el.find('.value[name=title]').attr('disabled', 'disabled');
            // TODO: each?
            this.$el.find('.value[name=step]').attr('disabled', 'disabled');
            this.$el.find('.value[name=deadline_ts]')
                    .attr('disabled', 'disabled');
            this.$el.find('.value[name=price]').attr('disabled', 'disabled');
        }

    });

    return new TaskInstancePostViewClass(attributes, options);
}


var CustomerView = customer.getCustomerViewClass();
function PostCustomerView(attributes, options) {
    var PostCustomerViewClass = CustomerView.extend({
        
        addRequiredValidationRules: function () {
            this.$el.validate({
                rules: {
                    first_name: 'required',
                    last_name: 'required',
                    email: 'required',
                    card_number: 'required',
                    card_expiry_month: 'required',
                    card_expiry_year: 'required',
                    cvc: 'required'
                }
            });
        }
    });

    return new PostCustomerViewClass(attributes, options);
}

return {
    TaskInstancePostPage: function () {
        return new TaskInstancePostPage();
    }
};


});
