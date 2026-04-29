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
// break constructor debugger: when website using this method
(function(){
    Function.prototype.__constructor_back = Function.prototype.constructor;
    Function.prototype.constructor = function () {
        if (arguments && typeof arguments[0] === 'string' && arguments[0].indexOf('debugger') !== -1) {
            console.log("Hooked Function constructor called with argument:", arguments[0]);
            return
        }
        return Function.prototype.__constructor_back.apply(this, arguments);
    };
})();

// or

Function.prototype.constructor = function(){};

/* -------------------------------------------------------------------------------------*/
// break infinitely debugger
setInterval = function(){};

//or

my_interval = setInterval
setInterval = function (a, b){
    if (a.toString().indexOf('debugger') === -1) {
        console.log('');
        return my_interval(a, b);
    }
}

// or

for (let i=1;i<99999;i++){
    window.clearInterval(i);
}

/* -------------------------------------------------------------------------------------*/
// break Function debugger
(function(){
    Function.prototype.__constructor = Function;
    Function = function (){
        if (arguments && typeof arguments[0] === 'string' && arguments[0].indexOf('debugger') !== -1){
            return;
        }
        return Function.prototype.__constructor.apply(this, arguments);
    };
})();

/* -------------------------------------------------------------------------------------*/
// break eval loading JS string debugger
(function(){
    my_eval = eval;
    eval = function(text){
        if (text === '(function() {var a = new Date(); debugger; return new Date() - a > 100;}())'){  //input whatever the website load e.g.
            return null;
        }
        else {
            return my_eval(text);
        }
    };
})();


/* -------------------------------------------------------------------------------------*/
// remove rs6 3-layers debugger
;(function () {
  'use strict'
  const oEval = window.eval
  const oFunction = window.Function
  const handleArgs = (args, last) => {
    if (!args?.length) return
    const ind = last ? args.length - 1 : 0
    if (!args[ind]?.replaceAll) return
    args[ind] = args[ind].replaceAll(/\bdebugger\b/g, ';/*debugger*/;')
  }
  window._original_eval = oEval
  window._original_Function = oFunction
  window.eval = new Proxy(oEval, {
    apply(target, thisArg, argArray) {
      handleArgs(argArray, false)
      return target.apply(thisArg, argArray)
    }
  })
  window.Function = new Proxy(oFunction, {
    apply(target, thisArg, argArray) {
      handleArgs(argArray, true)
      return target.apply(thisArg, argArray)
    },
    construct(target, argArray, newTarget) {
      handleArgs(argArray, true)
      return new target(...argArray)
    }
  })
  oFunction.prototype.constructor = window.Function
}());

// can add break constructor debugger code as backup

/* -------------------------------------------------------------------------------------*/
// hook window.close
(function() {
    'use strict';
    window.close = function(s){
        debugger;
        window.close = '';
        return null;
    }
    history.back = function(){
        debugger;
        history.back  = '';
        return null;
    }
    Object.defineProperty(window, 'close', {
        value: window.close,
        writable: false,
        configurable: false
    });
    Object.defineProperty(window, 'history', {
        value: window.history,
        writable: false,
        configurable: false
    });
})();








