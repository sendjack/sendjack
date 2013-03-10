/**
 * A base model to subclass from.
 */
define(
        [
            // libraries
            'backbone',

            // modules
            'event'
            // jqueryui
        ],
        function(Backbone, event) {


/** Change Backbone sync to fire 'CREATE' events. */
var sync = Backbone.sync;
Backbone.sync = function(method, model, options) {
    sync.apply(this, arguments).done(function (resp, status, xhr) {
        // TODO: update our CRUD handler and change this to 201 only
        var properCreateStatusCond = xhr.status === 201;
        var altCreateStatusCond = (xhr.status === 200 && method === 'create');
        if (properCreateStatusCond || altCreateStatusCond) {
            model.trigger(event.CREATE, model, options);
        }
    });
};


var BaseModel = Backbone.Model.extend({
    /**
     * True if the model has changed since a sync event.
     */
    dirty: false,

    initialize: function (attributes, options) {
        this.on('change:id', this.fetch, this);

        this.on('change', this.makeDirty, this);
        this.on('sync', this.clearDirty, this);
        this.on(event.CREATE, this.onCreate, this);
    },

    makeDirty: function (model, options) {
        this.dirty = true;
    },

    clearDirty: function (model, resp, options) {
        this.dirty = false;
    },

    isDirty: function () {
        return this.dirty;
    },

    save: function (attributes, options) {
        var that = this;
        var updatedOptions = options || {};

        var successFunction = updatedOptions.success;
        var onSaveSuccess = function (model, response, successOptions) {
            that.trigger(event.SAVE, model, successOptions);
            if (successFunction) {
                successFunction(model, response, successOptions);
            }
        };

        var errorFunction = updatedOptions.error;
        var onSaveError = function (model, xhr, errorOptions) {
            if (errorFunction) {
                errorFunction(model, xhr, errorOptions);
            }
        };

        updatedOptions.success = onSaveSuccess;
        updatedOptions.error = onSaveError;

        console.log("SAVING:");
        console.log(this.toJSON());

        Backbone.Model.prototype.save.call(this, attributes, updatedOptions);
    }
});

return {
    getBaseModelClass: function () {
        return BaseModel;
    }
};


});


