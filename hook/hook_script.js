// save original methods
my_parse = JSON.parse
my_stringify = JSON.stringify

// rewrite methods, can be rewritten as callable functions
// write breakpoint in this method (with breakpoint logic, e.g. if)
// return original method result, or modify it as you wish
JSON = {
    parse: function (text) {
        console.log("Hooked JSON.parse called with argument:", text);
        return my_parse(text);
    },
    stringify: function (value) {
        console.log("Hooked JSON.stringify called with argument:", value);
        return my_stringify(value);
    }
}

// stringify: for request encryption: for RSA/AES encryption. obj stringify to str then encrypt
// parse: when response has been decrypted, for response decryption: for RSA/AES decryption. decrypt to str then parse to obj

j_s = '{"name": "alice"}'

console.log("Result of JSON.parse: ", JSON.parse(j_s));



/* -------------------------------------------------------------------------------------*/
// XHR request hook
(function() {
    var my_open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function(method,url,async) {
        if (url.indexOf("data") !== -1){
            console.log("Hooked XMLHttpRequest.open called with arguments:", method, url);
            debugger;
        }
        return my_open.apply(this, arguments);
    }
})();

/* -------------------------------------------------------------------------------------*/
// hook header when header has encryption.
(function(){
    var sh = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key === 'chromosome' || key === 'Token') {
            console.log("Hooked XMLHttpRequest.setRequestHeader called with arguments:", key, value);
            debugger;
        }
        return sh.apply(this, arguments);
    }
})();

/* -------------------------------------------------------------------------------------*/
// hook cookie when cookie has encryption and changes in each request. (most used)
(function (){
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
        set: function (val) {
            if (val.indexOf('ads-tracker-baidu') !== -1) {
                console.log('Hook cookie set->', val);
                debugger;
            }
            cookieTemp = val;
            return val;
        },
        get: function () {
            return cookieTemp;
        }
    });
})();

/* -------------------------------------------------------------------------------------*/
// methods empty
function deg(){
    debugger;
}
deg = function(){};

setInterval = function(){};
setTimeout = function(){};

/* -------------------------------------------------------------------------------------*/
// hook window, window.close anti debug
(function (){
    window.close = function (arg) {
        console.log("Hooked window.close called with argument:", arg);
        debugger;
        return null;
    }
})();

/* -------------------------------------------------------------------------------------*/
// hook history, history.back anti debug
(function(){
    history.back = function () {
        console.log("Hooked history.back called");
        debugger;
        return null;
    }
})();

/* -------------------------------------------------------------------------------------*/






