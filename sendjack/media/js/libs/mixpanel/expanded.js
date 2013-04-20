(function (doc , mp) {
    window.mixpanel = mp;

    var scriptElem = doc.createElement("script");
    scriptElem.type = "text/javascript";
    scriptElem.async = !0;
    if ("https:" === doc.location.protocol) {
        scriptElem.src = "https:";
    } else {
        scriptElem.src = "http:";
    }
    scriptElem.src = scriptElem.src + '//cdn.mxpnl.com/libs/mixpanel-2.2.min.js';

    var scriptHTML = doc.getElementsByTagName("script")[0];
    scriptHTML.parentNode.insertBefore(scriptElem, scriptHTML);
    
    mp._i = [];

    mp.init = function (token, config, name) {
        function add(a, f) {
            var c = f.split(".");
            2 === c.length && (a = a[c[0]], f = c[1]);
            a[f] = function () {
                a.push([f].concat(Array.prototype.slice.call(arguments, 0)));
            };
        }
        var g = mp;
        if ("undefined" !== typeof f) {
            g = mp[f] = [];
        } else {
            f = "mixpanel";
        }
        g.people = g.people || [];
        var functions = [
            'disable',
            'track',
            'track_pageview',
            'track_links',
            'track_forms',
            'register',
            'register_once',
            'unregister',
            'identify',
            'alias',
            'name_tag',
            'set_config',
            'people.set',
            'people.increment',
            'people.track_charge',
            'people.append'
        ];

        for (var i=0; i < functions.length; i=i+1) {
            add(g, functions[i]);
        }

        mp._i.push([token, config, name]);
    };

    mp.__SV = 1.2;
})(document, window.mixpanel || []);

mixpanel.init("YOUR_TOKEN");
