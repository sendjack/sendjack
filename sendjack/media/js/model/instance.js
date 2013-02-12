/**
 * A model of a Task Instance.
 */
define(
        [
            // libraries
            'lodash',
            'backbone'

            // modules
            // jqueryui
        ],
        function(_, Backbone) {


var TaskInstanceModel = Backbone.Model.extend({
    urlRoot: '/a/task',

    initialize: function (attributes, options) {
        var that = this;
        var customerModel = options.customerModel;
        customerModel.on('change:id', function (model) {
            that.set('customer_id', model.get('id'));
        });
    }
});

return {
    TaskInstanceModel: function (customerModel, attributes, options) {

        options = _.extend(options || {}, {customerModel: customerModel});
        return new TaskInstanceModel(attributes, options);
    }
};


});
