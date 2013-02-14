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
            'view/customer',
            'view/instance'

            //jquery ui
        ],
        function ($, Backbone, customer, instance) {


var SignUpSeriesContent = Backbone.View.extend({

    $currPage: null,
    pageList: [],

    initialize: function () {
        this.setElement('.alt-content');

        var customerView = customer.CustomerView();
        var instanceCreateView = instance.TaskInstanceView();

        var customerModel = customerView.model;
        var instanceModel = instanceCreateView.model;

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

        customerModel.on('change:id', this.render, this);
        instanceModel.on('change:id', this.render, this);

        // TODO: add support for inserting new step fields on focus.

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

return {
    SignUpSeries: function () {
        return new SignUpSeriesContent();
    }
};


});
