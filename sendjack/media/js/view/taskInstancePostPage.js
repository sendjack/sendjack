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
            'util/track',
            'view/instance',
            'view/customer',
            'view/payment'

            // jquery ui
        ],
        function ($, Backbone, event, track, instance, customer, payment) {


var TaskInstancePostPage = Backbone.View.extend({

    $currGrid: null,
    taskInstanceView: null,
    customerView: null,

    initialize: function () {
        this.setElement('.task-instance-post-page');

        // the TaskInstancePostView will handle test v control.
        this.taskInstanceView = TaskInstancePostView();

        // wait until after the instance data is fetched to grab customer id.
        var that = this;

        this.taskInstanceView.model.on('change:price', function (model) {
            if (!model.previous('price')) {
                model.set('status', 'processed');
            }
        });

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
                    that.onCreditCardTokenReceived,
                    that);

            var taskStatus = model.get('status');

            // once the customer is pulled from server show the correct fields.
            that.customerView.model.once(
                    'change:control_group',
                    function (model) {
                        var isControlGroup = model.get('control_group');
                        that.taskInstanceView.setupControlAndTestFields(
                                isControlGroup,
                                taskStatus);
                    },
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

        track.viewPage(window.location.pathname);
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

    onCreditCardTokenReceived: function (model, options) {
        // when customer view is saved then update task view
        this.customerView.model.once(
                event.SAVE,
                this.onCreditCardAdded,
                this);

        this.customerView.save();
    },

    onCreditCardAdded: function (model, options) {
        var taskInstanceModel = this.taskInstanceView.model;

        track.addCreditCard(taskInstanceModel.get('price'));

        taskInstanceModel.set('status', 'confirmed');
        taskInstanceModel.once(event.SAVE, this.onCreatedTask, this);
        this.taskInstanceView.save();
    },

    onCreatedTask: function (model, options) {
        track.postTask(model.get('id'), model.get('price'));
        this.render();
    }
});


var TaskInstanceView = instance.getTaskInstanceViewClass();
function TaskInstancePostView(attributes, options) {
    var TaskInstancePostViewClass = TaskInstanceView.extend({

        setupControlAndTestFields: function (isControlGroup, taskStatus) {
            if (isControlGroup) {
                this.initializeControlFields(taskStatus);
            } else {
                this.initializeTestFields(taskStatus);
            }
        },

        initializeControlFields: function (taskStatus) {
            this.initializeShownControlFields(taskStatus);
            this.initializeDisabledControlFields(taskStatus);
        },

        initializeTestFields: function (taskStatus) {
            this.initializeShownTestFields(taskStatus);
            this.initializeDisabledTestFields(taskStatus);
        },

        initializeShownControlFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('.template-id').hide();

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('.custom-properties').hide();
                this.$el.find('.custom-property').hide();
                this.$el.find('.output-type').hide();
                this.$el.find('.output-method').hide();
                this.$el.find('.category-tags').hide();
                this.$el.find('.industry-tags').hide();
                this.$el.find('.skill-tags').hide();
                this.$el.find('.equipment-tags').hide();
            }

            this.$el.find('.field.title').hide();
            this.$el.find('.steps').hide();
            this.$el.find('.step').hide();
        },

        initializeDisabledControlFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('[name=customer_title]')
                        .attr('disabled', 'disabled');
                this.$el.find('[name=customer_description]')
                        .attr('disabled', 'disabled');

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('[name=notes]').attr('disabled', 'disabled');
                this.$el.find('[name=deadline_ts]')
                        .attr('disabled', 'disabled');

                this.$el.find('[name=price]').attr('disabled', 'disabled');
            }
        },

        initializeShownTestFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('.template-id').hide();

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('.custom-properties').hide();
                this.$el.find('.custom-property').hide();
                this.$el.find('.output-type').hide();
                this.$el.find('.output-method').hide();
                this.$el.find('.category-tags').hide();
                this.$el.find('.industry-tags').hide();
                this.$el.find('.skill-tags').hide();
                this.$el.find('.equipment-tags').hide();
            }

            this.$el.find('.customer-title').hide();
            this.$el.find('.customer-description').hide();
        },

        initializeDisabledTestFields: function (taskStatus) {
            if (taskStatus !== 'created') {
                this.$el.find('[name=title]').attr('disabled', 'disabled');
                // TODO: can hidden inputs be disabled?
                //this.$el.find('[name=steps]').attr('disabled', 'disabled');
                this.$el.find('[name=step]').attr('disabled', 'disabled');

                // TODO: put these in a superclass TaskInstancePostView.
                this.$el.find('[name=notes]').attr('disabled', 'disabled');
                this.$el.find('[name=deadline_ts]').attr('disabled', 'disabled');

                this.$el.find('[name=price]').attr('disabled', 'disabled');
            }
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
