/**
 * A model of a Task Instance.
 *
 * @exports model.instance
 *
 * @requires Backbone
 */
define(
        [
            // libraries
            'backbone'

            // modules
            // jqueryui
        ],
        function(Backbone) {


var TaskInstanceModel = Backbone.Model.extend({
    urlRoot: '/a/task'
});

return {
    TaskInstanceModel: function (attributes, options) {
        return new TaskInstanceModel(attributes, options);
    }
};


});
