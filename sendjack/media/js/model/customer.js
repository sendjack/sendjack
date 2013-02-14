/**
 * A model of a Customer.
 */
define(
        [
            // libraries
            'backbone'

            // modules
            // jqueryui
        ],
        function(Backbone) {


var CustomerModel = Backbone.Model.extend({
    urlRoot: '/a/customer'
});

return {
    CustomerModel: function (attributes, options) {
        return new CustomerModel(attributes, options);
    }
};


});

