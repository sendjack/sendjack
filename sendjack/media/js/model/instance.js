/**
 * A model of a Task Instance.
 *
 * @exports model.instance
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

var TaskInstanceModel = BaseModel.extend({
    urlRoot: '/a/task'
});

return {
    TaskInstanceModel: function (attributes, options) {
        return new TaskInstanceModel(attributes, options);
    }
};


});
