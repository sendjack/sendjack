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

    initialize: function () {
        ObjectView.prototype.initialize.call(
                this,
                '#instance',
                'task',
                instance.TaskInstanceModel(),
                this.getBindings());
    },

    getBindings: function () {
        return null;
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
    },

    setStatus: function (status) {
        this.model.set('status', status);
    }
});

return {
    TaskInstanceView: function (customerModel) {
        return new TaskInstanceView(customerModel);
    },

    getTaskInstanceViewClass: function () {
        return TaskInstanceView;
    }
};


});

