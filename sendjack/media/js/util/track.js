/**
 * Track actions with MixPanel.
 *
 * @exports track
 *
 * @requires $
 * @requires MP
 *
 */
define(
        [
            // libraries
            'jquery',
            'mp'

            // modules
            // jquery ui
        ],
        function ($) {


// get MixPanel token from meta data.
var token = $('meta[name=mixpanel-token]').attr('content');

// for the life of me, I cannot get MixPanel to integrate with RequireJS.
// this identifies your website when calling any mixpanel event.
mixpanel.init(token);
mixpanel.set_config({
    debug: true,
    test: true,
    verbose: true
});

// MixPanel events
var EVENT = {
    VIEW_PAGE: "View Page",

    SIGN_UP: "Sign Up",
    ADD_CREDIT_CARD: "Add Credit Card",

    UPDATE_TASK: "Update Task", // User updates a Task's properties

    SUBMIT_TASK: "Submit Task", // User requests Task CREATED
    POST_TASK: "Confirm Task", // User requests Task POSTED
    APPROVE_TASK: "Approve Task", // User approves Task
    REJECT_TASK: "Reject Task" // User rejects Task
};

// MixPanel properties
var PROPERTY = {
    PAGE: "page",
    CONTROL_GROUP: "control group",
    TASK_ID: "task id",
    PRICE: "price",
    FIRST_TASK_PRICE: "price"
};

var track = (function () {
    var that = {};

    /**
     * Track any event.
     */
    function trackEvent(event, properties) {
        mixpanel.track(event, properties);
    }

    /**
     * Initialize customer with Jackalope ID and persistent properties.
     */
    that.initCustomer = function (customerID, email, controlGroup) {
        mixpanel.alias(customerID);
        if (email) {
            mixpanel.name_tag(email);
        }

        var superProperties = {};
        console.log(controlGroup);
        superProperties[PROPERTY.CONTROL_GROUP] = controlGroup;
        mixpanel.register(superProperties);
    };

    /**
     * Sign up user with one time SIGN_UP.
     */
    that.signUp = function (customerID, email, controlGroup) {
        console.log("TRACK sign up", customerID, email);
        that.initCustomer(customerID, email, controlGroup);

        
        var properties = {};
        trackEvent(EVENT.SIGN_UP, properties);
    };

    /**
     * Login user to make sure their actions are associated across sessions.
     */
    that.login = function (customerID) {
        // TODO
        // double-check but you should call identify here.
        // then probably want to track it too.
        // then update super properties.
    };

    /**
     * Add a credit card to a customer's account.
     */
    that.addCreditCard = function (firstTaskPrice) {
        var properties = {};
        properties[PROPERTY.FIRST_TASK_PRICE] = firstTaskPrice;
        trackEvent(EVENT.ADD_CREDIT_CARD, properties);
    };

    /**
     * Track a VIEW_PAGE.
     */
    that.viewPage = function (page) {
        var properties = {};
        properties[PROPERTY.PAGE] = page;
        trackEvent(EVENT.VIEW_PAGE, properties);
    };

    /**
     * Track a SUBMIT_TASK.
     */
    that.submitTask = function (taskID) {
        var properties = {};
        properties[PROPERTY.TASK_ID] = taskID;
        trackEvent(EVENT.SUBMIT_TASK, properties);
    };

    /** Track a POST_TASK. */
    that.postTask = function (taskID, price) {
        var properties = {};
        properties[PROPERTY.TASK_ID] = taskID;
        properties[PROPERTY.PRICE] = price;
        trackEvent(EVENT.POST_TASK, properties);
    };

    /** Track a APPROVE_TASK. */
    that.approveTask = function (taskID, price) {
        var properties = {};
        properties[PROPERTY.TASK_ID] = taskID;
        properties[PROPERTY.PRICE] = price;
        trackEvent(EVENT.APPROVE_TASK, properties);
    };

    /** Track a REJECT_TASK. */
    that.rejectTask = function (taskID, price) {
        var properties = {};
        properties[PROPERTY.TASK_ID] = taskID;
        properties[PROPERTY.PRICE] = price;
        trackEvent(EVENT.REJECT_TASK, properties);
    };

    return that;
})();

return track;


});
