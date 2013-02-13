/**
 * Access the TaskInstanceView.
 *
 * @exports view.instance
 *
 * @requires $
 * @requires view.base
 * @requires model.instance
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/base',
            'model/instance'

            //jquery ui
        ],
        function ($, base, instance) {


var ObjectView = base.getObjectViewClass();

var TaskInstanceView = ObjectView.extend({

    initialize: function (customerModel) {
        ObjectView.prototype.initialize.call(
                this,
                '#instance',
                'task',
                instance.TaskInstanceModel(customerModel),
                this.getBindings());
    },

    getBindings: function () {
        return {
            customer_title: '[name=customer_title]',
            customer_description: '[name=customer_description]',
            deadline_ts: {
                selector: '[name=deadline_ts]',
                converter: this.tsConverter
            }
        };
    },

    tsConverter: function (direction, value) {
        var converted_ts;
        if (direction === 'ViewToModel') {
            var view_date = new Date(value);
            converted_ts = view_date.toISOString();
        } else if (direction === 'ModelToView') {
            var model_date = new Date(value);
            converted_ts = model_date.toLocaleDateString();
        } else {
            console.log('what the hell');
        }

        return converted_ts;
    }
});

return {
    TaskInstanceView: function (customerModel) {
        return new TaskInstanceView(customerModel);
    }
};


});

