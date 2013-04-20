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
            'util/track',
            'model/base'

            // jqueryui
        ],
        function(track,base) {


// Get access to the superclass without instantiating an instance.
var BaseModel = base.getBaseModelClass();

var TaskInstanceModel = BaseModel.extend({
    urlRoot: '/a/instances',

    onCreate: function (model, options) {
        track.submitTask(model.get('id'));
    },
    
    save: function (attributes, options) {
        BaseModel.prototype.save.call(this, attributes, options);
    }
});

return {
    TaskInstanceModel: function (attributes, options) {
        return new TaskInstanceModel(attributes, options);
    }
};


});
