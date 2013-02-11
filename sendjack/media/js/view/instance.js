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
                instance.TaskInstanceModel());
    }
});

return {
    TaskInstanceView: function () {
        return new TaskInstanceView();
    }
};


});

