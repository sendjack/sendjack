/**
 * A model of a Template.
 */
define(
        [
            // libraries
            'backbone'

            // modules
            // jqueryui
        ],
        function(Backbone) {


var TemplateModel = Backbone.Model.extend({
    urlRoot: '/a/template'
});

return {
    TemplateModel: function (attributes, options) {
        return new TemplateModel(attributes, options);
    }
};


});
