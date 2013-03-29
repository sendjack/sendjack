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
            'view/item/base',
            'model/instance'

            //jquery ui
        ],
        function ($, Backbone, ModelBinder, base, instance) {


var TaskView = base.getTaskViewClass();

var TaskInstanceView = TaskView.extend({

    el: '.instance-view',

    editBindings: function (bindings) {
        // TODO: maybe move this to TaskView?

        this._setBindingConverter(bindings.instructions, this.convertJSON);
        this._setBindingConverter(bindings.properties, this.convertJSON);
        this._setBindingConverter(bindings.deadline_ts, this.convertDeadline);

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
