/**
 * Access the Sign Up Pages.
 *
 * @exports view.signUpSeries
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
            'view/customer',
            'view/instance'

            //jquery ui
        ],
        function ($, Backbone, event, customer, instance) {


var SignUpSeriesContent = Backbone.View.extend({

    $currPage: null,
    pageList: [],

    initialize: function () {
        this.setElement('.alt-content');

        var customerView = SignUpCustomerView();
        var instanceView = TaskInstanceSaveView();

        var customerModel = customerView.model;
        var instanceModel = instanceView.model;

        customerModel.on('change:id', function (model) {
            instanceModel.set('customer_id', model.get('id'));
        });

        // remove the pages so we can show them one by one
        this.pageList = [
            this.$el.find('.sign-up-page').detach(),
            this.$el.find('.new-task-page').detach(),
            this.$el.find('.thank-you-page').detach()
        ];

        // all this junk is necessary to fade the next page in.
        // $.show() and $.fadeIn() revert to the last display state.
        var that = this;
        $.each(this.pageList, function (index, $page) {
            $page.css('display', 'block').hide();
            that.$el.append($page);
        });

        customerModel.once(event.SAVE, this.render, this);
        instanceModel.once(event.SAVE, this.render, this);
        this.render();
    },

    events: function () {
        var _events = {};

        //_events['click .submit-button'] = 'render';

        return _events;
    },

    render: function () {
        if (this.$currPage !== null) {
            this.$currPage.hide();
        }

        this.$currPage = this.pageList.shift();
        this.$currPage.fadeIn();

        return this;
    }
});


var TaskInstanceView = instance.getTaskInstanceViewClass();
function TaskInstanceSaveView(attributes, options) {
    var TaskInstanceSaveViewClass = TaskInstanceView.extend({

        initialize: function () {
            TaskInstanceView.prototype.initialize.call(this);

            // TODO: make an iterable of fields to hide/disable?

            console.log('askldfj alskdfj alsdkfj laksfdj');
            console.log(this.$el.find('.title'));
            this.$el.find('.title').hide();
            this.$el.find('.steps').hide();
            // TODO: each?
            this.$el.find('.step').hide();
            //this.$el.find('.custom-properties').hide();
            //this.$el.find('.custom-property').hide();
            //this.$el.find('.output-type').hide();
            //this.$el.find('.output-method').hide();
            this.$el.find('.price').hide();
            //this.$el.find('.category-tags').hide();
            //this.$el.find('.industry-tags').hide();
            //this.$el.find('.skill-tags').hide();
            //this.$el.find('.equipment-tags').hide();

            // TODO: these are wrong. they don't even use class=value
            this.$el.find('[name=title]').attr('disabled', 'disabled');
            // TODO: each?
            this.$el.find('[name=steps]').attr('disabled', 'disabled');
            this.$el.find('[name=step]').attr('disabled', 'disabled');
            this.$el.find('[name=price]').attr('disabled', 'disabled');
        },

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

            this.model.on('change:stripe_token', this.save, this);
        },

        addRequiredValidationRules: function () {
            this.$el.validate({
                rules: {
                    first_name: 'required',
                    last_name: 'required',
                    email: 'required'
                }
            });
        }
    });

    return new SignUpCustomerViewClass(attributes, options);
}

return {
    SignUpSeries: function () {
        return new SignUpSeriesContent();
    }
};


});
