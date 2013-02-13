/**
 * Access the TaskTemplateView.
 *
 * @exports view.template
 *
 * @requires $
 * @requires view.base
 * @requires model.template
 *
 */
define(
        [
            //libraries
            'jquery',

            //modules
            'view/base',
            'model/template'

            //jquery ui
        ],
        function ($, base, template) {


// Get access to the superclass without instantiating an instance.
var ObjectView = base.getObjectViewClass();

var TaskTemplateView = ObjectView.extend({

    initialize: function () {
        ObjectView.prototype.initialize.call(
                this,
                '#template',
                'template',
                template.TaskTemplateModel());
    },

    editBindings: function (bindings) {
        bindings.steps.converter = this.convertSteps;
        return bindings;
    },

    convertSteps: function (direction, value) {
        // TODO: FILL THIS IN!
        var converted;
        if (direction === 'ViewToModel') {
            var view_date = new Date(value);
            converted = view_date.toISOString();
        } else if (direction === 'ModelToView') {
            var model_date = new Date(value);
            converted = model_date.toLocaleDateString();
        }

        return converted;
    }

});

return {
    TaskTemplateView: function () {
        return new TaskTemplateView();
    }
};


});
