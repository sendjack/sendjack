/**
 * Access the TaskInstanceView.
 *
 * @exports view.instance
 *
 * @requires $
 * @requires Backbone
 * @requires ModelBinder
 * @requires view.base
 * @requires model.instance
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',
            'modelbinder',

            //modules
            'view/object/base',
            'model/instance'

            //jquery ui
        ],
        function ($, Backbone, ModelBinder, base, instance) {


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
        // TODO: maybe move this to TaskView?

        bindings.instructions.converter = this.convertJSON;
        bindings.properties.converter = this.convertJSON;
        bindings.deadline_ts.converter = this.convertDeadline;

        return bindings;
    },

    convertDeadline: function (direction, value) {
        var converted;

        if (direction === Backbone.ModelBinder.Constants.ViewToModel) {
            converted = (new Date(value)).toISOString();
        } else if (direction === Backbone.ModelBinder.Constants.ModelToView) {
            converted = (new Date(value)).toLocaleDateString();
        }

        return converted;
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
