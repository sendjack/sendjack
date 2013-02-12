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

    initialize: function (id, model, bindings) {
        this.setElement(id);

        this.$el.find('[name=id]').attr('disabled', 'disabled');

        // set up model and if it has an id, then fetch data from server.
        this.model = model;
        if (!this.model.isNew()) {
            this.model.fetch();
        }
        
        // set up view/model bindings.
        this._modelBinder = new Backbone.ModelBinder();
        if (bindings === null) {
            this._modelBinder.bind(this.model, this.el);
        } else {
            this._modelBinder.bind(this.model, this.el, bindings);
        }

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
