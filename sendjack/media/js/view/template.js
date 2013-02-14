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


var TaskView = base.getTaskViewClass();

var TaskTemplateView = TaskView.extend({

    initialize: function () {
        TaskView.prototype.initialize.call(
                this,
                '#template',
                'template',
                template.TaskTemplateModel());
    },

    editBindings: function (bindings) {
        bindings.steps.selector = '[class~=sub-value]';
        bindings.steps.converter = this.convertSteps;
        return bindings;
    }

});

return {
    TaskTemplateView: function () {
        return new TaskTemplateView();
    }
};


});
