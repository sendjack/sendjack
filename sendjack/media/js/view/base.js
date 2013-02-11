/**
 * Provide a base class for object views.
 *
 * @exports view.base
 *
 * @requires $
 * @requires Backbone
 * @requires ModelBinder
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',
            'modelbinder'

            //modules
            //jquery ui
        ],
        function ($, Backbone, ModelBinder) {


var ObjectView = Backbone.View.extend({

    initialize: function (id, model) {
        this.setElement(id);

        this.$el.find('[name=id]').attr('disabled', 'disabled');

        this.model = model;
        if (!this.model.isNew()) {
            this.model.fetch();
        }

        this._modelBinder = new Backbone.ModelBinder();
        this._modelBinder.bind(this.model, this.el);
        
         
        this.render();
    },

    events: function () {
        var _events = {};

        _events['click .submit-button'] = 'save';

        return _events;
    },

    render: function () {
        return this;
    },

    save: function () {
        this.model.save();
    }
});

return {
    getObjectViewClass: function () {
        return ObjectView;
    }
};


});

