/**
 * A model of a Task Template.
 *
 * @exports model.template
 *
 * @requires model.base
 */
define(
        [
            // libraries

            // modules
            'model/base'

            // jqueryui
        ],
        function(base) {


// Get access to the superclass without instantiating an instance.
var BaseModel = base.getBaseModelClass();

var TaskTemplateModel = BaseModel.extend({
    urlRoot: '/a/template'
});

return {
    TaskTemplateModel: function (attributes, options) {
        return new TaskTemplateModel(attributes, options);
    }
};


});
