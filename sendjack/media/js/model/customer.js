/**
 * A model of a Customer.
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

var CustomerModel = BaseModel.extend({
    urlRoot: '/a/customer'
});

return {
    CustomerModel: function (attributes, options) {
        return new CustomerModel(attributes, options);
    }
};


});

