/**
 * A model of a Customer.
 */
define(
        [
            // libraries

            // modules
            'event',
            'util/track',
            'model/base'

            // jqueryui
        ],
        function (event, track, base) {


// Get access to the superclass without instantiating an instance.
var BaseModel = base.getBaseModelClass();

var CustomerModel = BaseModel.extend({
    urlRoot: '/a/customers',

    onCreate: function (model, options) {
        console.log('happiness');
        track.signUp(model.get('id'), model.get('email'));
    },

    save: function (attributes, options) {
        BaseModel.prototype.save.call(this, attributes, options);
    }
});

return {
    CustomerModel: function (attributes, options) {
        return new CustomerModel(attributes, options);
    }
};


});

