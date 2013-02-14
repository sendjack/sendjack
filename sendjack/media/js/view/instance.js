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


var TaskView = base.getTaskViewClass();

var TaskInstanceView = TaskView.extend({

    initialize: function () {
        TaskView.prototype.initialize.call(
                this,
                '#instance',
                'task',
                instance.TaskInstanceModel());
    },

    editBindings: function (bindings) {
        bindings.steps.selector = '[class~=sub-value]';
        bindings.steps.converter = this.convertSteps;
        bindings.deadline_ts.converter = this.convertDeadline;
        return bindings;
    },

    convertDeadline: function (direction, value) {
        var converted;

        if (this.convertingToModel(direction)) {
            converted = (new Date(value)).toISOString();
        } else if (this.convertingToView(direction)) {
            converted = (new Date(value)).toLocaleDateString();
        }

        return converted;
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
