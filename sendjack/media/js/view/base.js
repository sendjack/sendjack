/**
 * Provide a base class for object views.
 *
 * @exports view.base
 *
 * @requires $
 * @requires Lodash
 * @requires Backbone
 * @requires ModelBinder
 *
 */
define(
        [
            //libraries
            'jquery',
            'lodash',
            'backbone',
            'modelbinder'

            //modules
            //jquery ui
        ],
        function ($, _, Backbone, ModelBinder) {


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

    /**
     * If we want to handle bindings differently and/or more generically, these
     * two links should be helpful:
     *      https://github.com/theironcook/Backbone.ModelBinder
     *          #quickly-create-and-modify-bindings
     *          #the-power-of-jquery
     */
    getBindings: function (boundAttribute) {
        var attribute = boundAttribute || 'name';

        return this.editBindings(
            Backbone.ModelBinder.createDefaultBindings(this.el, attribute));
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

    initialize: function (selector, urlPath, model) {
        ObjectView.prototype.initialize.call(this, selector, urlPath, model);

        _.bindAll(this);

        this.model.on('change:steps', this.replaceSteps);
        this.model.on('change:custom_properties', this.replaceCustomProperties);
    },

    /**
     * Override ObjectView.save() to silently remove from the model any named
     * attributes we don't want posted to the server on submit. The canonical
     * example here will be any fields which exist in groups that compose some
     * aggregate field to be passed as a JSON array or object (step,
     * custom_property, etc.).
     */
    save: function () {
        this.model.unset('step', {silent: true});
        this.model.unset('custom_property_key', {silent: true});
        this.model.unset('custom_property_value', {silent: true});

        this.model.save();
    },

    events: function () {
        //var _events = {};
        var _events = ObjectView.prototype.events.call(this);

        _events['focus .step'] = 'appendInputOnFocus';
        //_events['keydown .step'] = 'insertInputOnTab';
        _events['change [name=step]'] = 'updateSteps';

        _events['focus .custom-property'] = 'appendInputOnFocus';
        //_events['keydown [name=custom_property_value]'] = 'insertInputOnTab';
        _events['change [name^=custom_property_]'] = 'updateCustomProperties';

        return _events;
    },

    convertJSON: function (direction, value) {
        var converted;

        if (direction === Backbone.ModelBinder.Constants.ModelToView) {
            converted = JSON.stringify(value);
        } else if (direction === Backbone.ModelBinder.Constants.ViewToModel) {
            converted = JSON.parse(value);
        }

        return converted;
    },

    appendInputOnFocus: function (event) {
        var targetEl = $(event.currentTarget);

        // if this is the last item in the list, grow the list.
        if (targetEl.is(':last-child')) {
            this.insertEmptyCloneAfter(targetEl);
        }
    },

    insertInputOnTab: function (event) {
        // TODO: handle SHIFT+TAB (9=TAB; 16=SHIFT)

        // check whether TAB was pressed
        if (event.which === 9) {
            // insert after the step whose input has focus
            this.insertEmptyCloneAfter($(event.currentTarget));
        }
    },

    insertEmptyCloneAfter: function (el) {
        // TODO: is this deep a copy warranted?
        var nextEl = el.clone(true, true);

        // make sure the value for each input in the clone are empty
        nextEl.children(':input').val('');

        // add the new one to the dom's list after the current one
        nextEl.insertAfter(el);
    },

    updateSteps: function (event) {
        this.updateInputSet(
            $(event.currentTarget).parent().parent().children(),
            '[name=steps]',
            '[name=step]');
    },

    updateCustomProperties: function (event) {
        this.updateInputSet(
            $(event.currentTarget).parent().parent().children(),
            '[name=custom_properties]',
            '[name=custom_property_value]',
            '[name=custom_property_key]');
    },

    updateInputSet: function (els, setSelector, valueSelector, keySelector) {
        var set = [];

        var inputEls, value, key;
        for (var i=0; i < els.length; i=i+1) {
            inputEls = els.eq(i).children();

            value = inputEls.filter(valueSelector).val();

            // an undefined key selector is valid. it's an optional parameter.
            if (typeof keySelector !== 'undefined') {
                key = inputEls.filter(keySelector).val();
            } else {
                key = null;
            }

            // if a key selector has been specified and a valid key exists,
            // store the value, which may be empty, in a list of dicts. if not,
            // only care about non-empty values, and store them in a 1-D list.
            if (key !== null && key !== '') {
                set[i] = {};
                set[i][key] = value;
            } else if (value !== null && value !== '') {
                set[i] = value;
            }
        }

        this.$el.find(setSelector).val(JSON.stringify(set)).change();
    },

    replaceSteps: function (model, value, options) {
        if (value !== null) {
            this.replaceInputs('.step', value, false);
        }
    },

    replaceCustomProperties: function (model, value, options) {
        if (value !== null) {
            this.replaceInputs('.custom-property', value, true);
        }
    },

    replaceInputs: function (inputsSelector, inputValues, fromDicts) {
        var el = this.resetInputs(inputsSelector);

        for (var i=0; i < inputValues.length; i=i+1) {
            this.replaceInput(el, inputValues[i], fromDicts);
        }

    },

    resetInputs: function (inputsSelector) {
        var els = this.$el.find(inputsSelector);
        els.slice(0, -1).remove();
        return els.filter(':last');
    },

    replaceInput: function (containerEl, inputValue, isDict) {
        var newEl = containerEl.clone(true, true);

        if (isDict) {
            for (var key in inputValue) {
                if (inputValue.hasOwnProperty(key)) {
                    newEl.children(':input').first().val(key);
                    newEl.children(':input').last().val(inputValue[key]);
                }
            }
        } else {
            newEl.children(':input').last().val(inputValue);
        }

        newEl.insertBefore(containerEl);
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
