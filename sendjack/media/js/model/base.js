/**
 * A base model to subclass from.
 */
define(
        [
            // libraries
            'backbone'

            // modules
            // jqueryui
        ],
        function(Backbone) {


var BaseModel = Backbone.Model.extend({
    /**
     * True if the model has changed since a sync event.
     */
    dirty: false,

    initialize: function (attributes, options) {
        this.on('change', this.makeDirty, this);
        this.on('sync', this.clearDirty, this);
    },

    makeDirty: function (model, options) {
        this.dirty = true;
    },

    clearDirty: function (model, resp, options) {
        this.dirty = false;
    },

    isDirty: function () {
        return this.dirty;
    }
});

return {
    getBaseModelClass: function () {
        return BaseModel;
    }
};


});


