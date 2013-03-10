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
            'view/item/base',
            'model/template'

            //jquery ui
        ],
        function ($, base, template) {


var TaskView = base.getTaskViewClass();

var TaskTemplateView = TaskView.extend({

    el: '#template',

    initialize: function () {
        TaskView.prototype.initialize.call(this);
    },

    editBindings: function (bindings) {
        // TODO: maybe move this to TaskView?

        bindings.instructions.converter = this.convertJSON;
        bindings.properties.converter = this.convertJSON;

        return bindings;
    }

});

return {
    TaskTemplateView: function () {
        return new TaskTemplateView();
    }
};


});
