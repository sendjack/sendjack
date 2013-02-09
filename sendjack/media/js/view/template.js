/**
 * Access the TemplateView.
 *
 * @exports TemplateView
 * @requires $
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',
            'modelbinder',

            //modules
            'model/template'

            //jquery ui
        ],
        function ($, Backbone, ModelBinder, template) {


var TemplateView = Backbone.View.extend({

    initialize: function () {
        this.setElement('#template');

        this.$el.find('[name=id]').attr('disabled', 'disabled');

        this.model = template.TemplateModel({id: 3});
        if (!this.model.isNew()) {
            this.model.fetch();
        }

        this._modelBinder = new Backbone.ModelBinder();
        this._modelBinder.bind(this.model, this.el);
        
         
        this.render();
    },

    events: function () {
        var _events = {};

        _events['click .submit-button'] = 'saveTemplate';

        return _events;
    },

    render: function () {
        return this;
    },

    saveTemplate: function () {
        this.model.save();
    }
});

return {
    TemplateView: function () {
        return new TemplateView();
    }
};


});
