/**
 * Access the DocumentView.
 *
 * @exports DocumentView
 * @requires $
 * @requires Backbone
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',

            //modules
            'model/test'
        ],
        function ($, Backbone, test) {


var DocumentView = Backbone.View.extend({

    initialize: function () {
        this.setElement('#karma');
        this.model = test.TestModel();
        console.log(this.model);
        this.model.save({name: 'captain'},{
            success: function () {
                console.log('sync success');
            },
            error: function () {
                console.log('sync error');
            }
        });

    },

    render: function () {
        this.$el.show();
        return this;
    }
});

return {
    DocumentView: function () {
        return new DocumentView();
    }
};


});
