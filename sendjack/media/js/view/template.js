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
                template.TaskTemplateModel({id: 1}));
    }
});

return {
    TaskTemplateView: function () {
        return new TaskTemplateView();
    }
};


});
