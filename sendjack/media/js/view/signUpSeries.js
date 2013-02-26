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
            'util/track',
            'view/customer',
            'view/instance'

            //jquery ui
        ],
        function ($, Backbone, event, track, customer, instance) {


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
            var id = model.get('id');
            var email = model.get('email');
            track.signUp(id, email);
            instanceModel.set('customer_id', id);
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

        track.viewPage(window.location.href);
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
