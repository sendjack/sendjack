/**
 * Provide a base class for item views.
 *
 * @exports view.item.base
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
            'underscore',
            'backbone',
            'modelbinder',

            //modules
            'event'
            //jquery ui
        ],
        function ($, _, Backbone, ModelBinder, event) {


var ObjectView = Backbone.View.extend({

    modelBinder: null,

    /**
     * Initialize the ObjectView.
     */
    initialize: function () {
        this.$el.find('[name=id]').attr('disabled', 'disabled');

        //this.model = this.setupModel(model);
        
        this.modelBinder = new Backbone.ModelBinder();
        this.modelBinder.bind(this.model, this.el, this.getBindings());

        // keep these separate as the 'required' should happen in the page
        // specific subclasses and the 'type-checking' should happen at the
        // model views.
        this.addRequiredValidationRules();
        this.addTypeCheckingValidationRules();

        var thatModel = this.model;
        this.model.on('change', function () {
            console.log(thatModel.toJSON());
        });

        this.render();
    },

    events: function () {
        var _events = {};

        _events['click .submit-button'] = 'onSubmit';

        return _events;
    },

    render: function () {
        return this;
    },

    isValid: function () {
        return this.$el.valid();
    },

    isValidAndSynced: function () {
        return (this.isValid() && this.model.isDirty());
    },

    onSubmit: function (event) {
        this.save();
    },

    save: function (attributes, options) {
        if (this.isValid()) {
            this.model.save(attributes, options);
        } else {
            console.log('this form is not valid');
        }
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
     * Add Type Checking validation rules.
     *
     * This should be overriden by each base subclass.
     */
    addTypeCheckingValidationRules: function () {
    },

    /**
     * Add Required validation rules.
     *
     * This should be overriden by the subclasses associated with specific
     * pages.
     */
    addRequiredValidationRules: function () {
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

    initialize: function () {
        ObjectView.prototype.initialize.call(this);

        _.bindAll(this);

        this.model.on('change:instructions', this.replaceInstructions);
        this.model.on('change:properties', this.replaceProperties);
    },

    /**
     * Override ObjectView.save() to silently remove from the model any named
     * attributes we don't want posted to the server on submit. The canonical
     * example here will be any fields which exist in groups that compose some
     * aggregate field to be passed as a JSON array or object (instruction,
     * property, etc.).
     */
    save: function () {
        this.model.unset('instruction', {silent: true});
        this.model.unset('property_key', {silent: true});
        this.model.unset('property_value', {silent: true});

        ObjectView.prototype.save.call(this);
    },

    events: function () {
        //var _events = {};
        var _events = ObjectView.prototype.events.call(this);

        _events['focus .instruction'] = 'appendInputOnFocus';
        //_events['keydown .instruction'] = 'insertInputOnTab';
        _events['change [name=instruction]'] = 'updateInstructions';

        _events['focus .property'] = 'appendInputOnFocus';
        //_events['keydown [name=property_value]'] = 'insertInputOnTab';
        _events['change [name^=property_]'] = 'updateProperties';

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
            // insert after the instruction whose input has focus
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

    updateInstructions: function (event) {
        this.updateInputSet(
            $(event.currentTarget).parent().parent().children(),
            '[name=instructions]',
            '[name=instruction]');
    },

    updateProperties: function (event) {
        this.updateInputSet(
            $(event.currentTarget).parent().parent().children(),
            '[name=properties]',
            '[name=property_value]',
            '[name=property_key]');
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

    replaceInstructions: function (model, value, options) {
        if (value !== null) {
            this.replaceInputs('.instruction', value, false);
        }
    },

    replaceProperties: function (model, value, options) {
        if (value !== null) {
            this.replaceInputs('.property', value, true);
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
