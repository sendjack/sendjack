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
            'view/instance',
            'view/customer',
            'view/payment'

            // jquery ui
        ],
        function ($, Backbone, instance, customer, payment) {


var TaskInstancePostPage = Backbone.View.extend({

    $currGrid: null,
    customerView: null,
    creditCardView: null,
    taskInstanceView: null,

    initialize: function () {
        this.setElement('.task-instance-post-page');

        this.taskInstanceView = TaskInstancePostView();

        // wait until after the instance data is fetched to grab customer id.
        var that = this;
        this.taskInstanceView.model.on('change:customer_id', function (model) {

            // Create the Customer View with the customer_id
            var customerID = model.get('customer_id');
            that.customerView = customer.CustomerView({model_id: customerID});

            // Create the credit card view with the Customer Model
            var $creditCard = that.$el.find('#credit-card-grid');
            that.creditCardView = payment.CreditCardView(
                    {
                        el: $creditCard,
                        customerModel: that.customerView.model
                    });

            //customerView.model.on('change:stripe_token', that.render, that);
        });

          
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

        _events['click #credit-card-grid .submit-button'] = 'save';
        _events['click .submit-button'] = 'render';

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

    save: function () {
        this.creditCardView.save();
        this.taskInstanceView.setStatus("created");
        this.taskInstanceView.save();
    }

});

var TaskInstanceView = instance.getTaskInstanceViewClass();
function TaskInstancePostView() {
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

    return new TaskInstancePostViewClass();
}

return {
    TaskInstancePostPage: function () {
        return new TaskInstancePostPage();
    }
};


});
