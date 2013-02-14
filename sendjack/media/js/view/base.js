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
    model: null,
    modelBinder: null,

    /**
     * Initialize the ObjectView.
     * @param {String} selector Define the el.
     * @param {String} urlPath Define the url path that matches this object.
     * @param {Object} model Bind to this model.
     */
    initialize: function (selector, urlPath, model) {
        this.setElement(selector);
        this.urlPath = urlPath;

        this.$el.find('[name=id]').attr('disabled', 'disabled');

        this.model = this.setupModel(model);

        this.modelBinder = new Backbone.ModelBinder();
        this.modelBinder.bind(this.model, this.el, this.getBindings());

        var thatModel = this.model;
        this.model.on('change', function () {
            console.log(thatModel.toJSON());
        });

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
    },

    convertingToModel: function (direction) {
        return direction === 'ViewToModel';
    },

    convertingToView: function (direction) {
        return direction === 'ModelToView';
    },

    /**
     * If we want to handle bindings differently and/or more generically, these
     * two links should be helpful:
     *      https://github.com/theironcook/Backbone.ModelBinder
     *          #quickly-create-and-modify-bindings
     *          #the-power-of-jquery
     */
    getBindings: function (boundAttribute) {
        var attr = boundAttribute || 'name';

        var bindings = this.modelBinder.createDefaultBindings(this.el, attr);

        return this.editBindings(bindings);
    },

    /**
     * Views extending ObjectView may override to edit default bindings.
     *
     * For example:
     *
     *      bindings['phone'].converter = this._phoneConverterFunction;
     *      delete bindings['complicatedAttribute'];
     */
    editBindings: function (bindings) {
        return bindings;
    }

});


var TaskView = ObjectView.extend({

    convertSteps: function (direction, value) {
        var converted;
        console.log(direction);
        console.log(value);
        //if (this.convertingToModel(direction)) {

        //} else if (this.convertingToView(direction)) {

        //}

        return converted;
    }

});

return {
    getObjectViewClass: function () {
        return ObjectView;
    },

    getTaskViewClass: function () {
        return TaskView;
    }
};


});
