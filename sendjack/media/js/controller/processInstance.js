/**
 * Access the Process Instance Page.
 *
 * @exports controller.processInstance
 *
 */
define(
        [
            //libraries
            'jquery',
            'backbone',

            //modules
            'model/instance',
            'view/page/processInstance'
        ],
        function (
                $,
                Backbone,
                instanceModel,
                processInstanceView) {

var ProcessInstanceController = Backbone.Marionette.Controller.extend({

    region: null,

    instanceModel: null,

    processInstancePage: null,

    pagesSelector: '#process-instance-page',

    initialize: function () {
        if ($(this.pagesSelector).length) {
            this.region = new Backbone.Marionette.Region({
                el: '#page-container'
            });

            this.initializeModels();
            this.initializePages();
            this.initializeTransitions();
        }
    },

    initializeModels: function () {
        this.instanceModel = instanceModel.TaskInstanceModel();

        this.instanceModel.on('change:price', function (model) {
            if (!model.previous('price')) {
                model.set('status', 'processed');
            }
        });

    },

    initializePages: function () {
        this.processInstancePage = processInstanceView.ProcessInstancePageView({
            instanceModel: this.instanceModel
        });
    },

    initializeTransitions: function () {

    },

    loadProcessInstancePage: function (instanceID) {
        var id = parseInt(instanceID, 10);
        if (this.instanceModel.isNew()) {
            this.instanceModel.resetID(id);
        }

        this.region.show(this.processInstancePage);
    }

});


/** Make sure ProcessInstanceController is a singleton. */
var processInstanceController = null;

return {
    ProcessInstanceController: function () {
        if (processInstanceController === null) {
            processInstanceController = new ProcessInstanceController();
        }

        return processInstanceController;
    }
};


});
