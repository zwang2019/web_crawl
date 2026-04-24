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


j_s = '{"name": "alice"}'

console.log("Result of JSON.parse:", JSON.parse(j_s));


