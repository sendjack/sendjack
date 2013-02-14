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
            'view/customer'

            // jquery ui
        ],
        function ($, Backbone, instance, customer) {


var TaskInstancePostPage = Backbone.View.extend({

    $currGrid: null,

    initialize: function () {
        this.setElement('.task-instance-post-page');

        var taskInstanceView = TaskInstancePostView();

        // wait until after the instance data is fetched to grab customer id.
        var customerView;
        taskInstanceView.model.on('sync', function (model) {
            var customerID = model.get('customer_id');
            customerView = customer.CustomerView({model_id: customerID});
        });
          
        // remove the grids so we can show them one by one
        var $taskInstanceGrid = this.$el.find('#task-instance-grid').detach();
        var $creditCardGrid = this.$el.find('#credit-card-grid').detach();

        // all this junk is necessary to fade the next page in.
        // $.show() and $.fadeIn() revert to the last display state.
        $taskInstanceGrid.css('display', 'block').hide();
        $creditCardGrid.css('display', 'block').hide();
        this.$el.find('.grid-container')
            .append($taskInstanceGrid)
            .append($creditCardGrid);

        this.$currGrid = $taskInstanceGrid.fadeIn();
        this.$nextGrid = $creditCardGrid;
        this.$el.css('display', 'block');
        //this.render();
    },

    events: function () {
        var _events = {};

        _events['click .submit-button'] = 'render';

        return _events;
    },

    render: function () {
        this.$currGrid.hide();
        this.$nextGrid.fadeIn();
        return this;
    }

});

var TaskInstanceView = instance.getTaskInstanceViewClass();
function TaskInstancePostView() {
    var TaskInstancePostViewClass = TaskInstanceView.extend({

        initialize: function () {
            TaskInstanceView.prototype.initialize.call(this);
           
            // TODO: makea a list of disabled fields
            this.$el.find('.value[name=steps]').attr('disabled', 'disabled');
            this.$el.find('.value[name=deadline_ts]').attr('disabled', 'disabled');
        },

        getBindings: function () {
            return {
                steps: '[name=steps]',
                deadline_ts: {
                    selector: '[name=deadline_ts]',
                    converter: this.tsConverter
                },
                price: '[name=price]'
            };
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
