/**
 * A test model.
 */
define(
        [
            // libraries
            'jquery',
            'backbone'

            //modules
        ],
        function ($, Backbone) {


var TestModel = Backbone.Model.extend({
    urlRoot: '/backbone',

    defaults: {
        name: 'Fetus',
        age: 0
    }
});

return {
    TestModel: function (attributes, options) {
        return new TestModel(attributes, options);
    }
};


});
