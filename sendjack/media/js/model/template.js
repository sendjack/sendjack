/**
 * A model of a Task Template.
 */
define(
        [
            // libraries
            'backbone'

            // modules
            // jqueryui
        ],
        function(Backbone) {


var TaskTemplateModel = Backbone.Model.extend({
    urlRoot: '/a/template'
});

return {
    TaskTemplateModel: function (attributes, options) {
        return new TaskTemplateModel(attributes, options);
    }
};


});
