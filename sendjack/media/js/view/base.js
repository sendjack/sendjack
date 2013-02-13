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

    urlPath: null,

    /**
     * Initialize the ObjectView.
     * @param {String} selector Define the el.
     * @param {String} urlPath Define the url path that matches this object.
     * @param {Object} model Bind to this model.
     * @param {Dict} bindings (Optional) Use this mapping to bind fields.
     */
    initialize: function (selector, urlPath, model, bindings) {
        this.setElement(selector);
        this.urlPath = urlPath;

        this.$el.find('[name=id]').attr('disabled', 'disabled');

        this.model = this.setupModel(model);

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
    },

    /**
     * Make sure model matches URL and fetch any data if not New.
     */
    setupModel: function (model) {
        // set up model and if it has an id, then fetch data from server.
        // if the model corresponds to the url with id, then grab that info.
        var urlArray = document.URL.split('/');
        var model_type = urlArray[3];
        var model_id = urlArray[4];
        if (!model.isNew()) {
            model.fetch();
        } else if (model_type === this.urlPath &&
                model_id !== undefined) {
            model.set('id', model_id);
            model.fetch();
        }
        
        return model;
    }
});

return {
    getObjectViewClass: function () {
        return ObjectView;
    }
};


});
