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
        this.model.save();
    },

    events: function () {
        //var _events = {};
        var _events = ObjectView.prototype.events.call(this);

        _events['focus .step'] = 'appendEmptyStepOnEndFocus';
        _events['keydown .step'] = 'insertEmptyStepOnTab';
        _events['change [name=step]'] = 'updateSteps';

        return _events;
    },

    appendEmptyStepOnEndFocus: function (event) {
        // find the step whose input has focus
        var step = $(event.currentTarget);

        // if this is the last step, grow the list
        if (step.is(':last-child')) {
            this.insertEmptyStepAfter(step);
        }
    },

    insertEmptyStepOnTab: function (event) {
        // TODO: handle SHIFT+TAB (9=TAB; 16=SHIFT)
        // check whether TAB was pressed
        if (event.which === 9) {
            // insert after the step whose input has focus
            var step = $(event.currentTarget);
            this.insertEmptyStepAfter(step);
        }
    },

    insertEmptyStepAfter: function (currentStep) {
        // TODO: is this deep a copy warranted?
        var newStep = currentStep.clone(true, true);

        // make sure the value of the new step is empty
        newStep.children().filter(':input').val('');

        // TODO: add support for displaying a number in the Step label.

        // add the new step to the list after the current step
        newStep.insertAfter(currentStep);
    },

    updateSteps: function (event) {
        var stepDivs = $(event.currentTarget).parent().parent().children();

        var steps = [];
        for (var i=0; i < stepDivs.length; i=i+1) {
            // don't add empty steps. the model doesn't need 'em.
            var step = $(stepDivs[i]).children('[name=step]').val();
            if (step) {
                steps[i] = step;
            }
        }

        // set the steps hidden input to be synched with the model.
        this.$el.find('[name=steps]').val(JSON.stringify(steps)).change();
    },

    convertSteps: function (direction, value) {
        var converted;

        if (direction === Backbone.ModelBinder.Constants.ModelToView) {
            converted = JSON.stringify(value);
        } else if (direction === Backbone.ModelBinder.Constants.ViewToModel) {
            converted = JSON.parse(value);
        }

        return converted;
    },

    replaceSteps: function (model, value, options) {
        if (value === null) {
            return;
        }

        var stepDivs = this.$el.find('.step');
        var lastStep = stepDivs.filter(':last');

        stepDivs.slice(0, -1).remove();

        var newStep;
        for (var i=0; i < value.length; i=i+1) {
            newStep = lastStep.clone(true, true);
            newStep.children().filter(':input').val(value[i]);
            newStep.insertBefore(lastStep);
        }
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
