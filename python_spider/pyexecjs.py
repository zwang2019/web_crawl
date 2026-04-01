import execjs
"""
1. Embedded JavaScript Engines

This is the most direct alternative if you want something more low-level, controllable, and performant. Typical options include PyMiniRacer and quickjs.

PyMiniRacer embeds the V8 engine directly into Python and supports reusable contexts.
quickjs provides a Python interface to the QuickJS engine, supports native type conversion between Python and JavaScript, and offers useful controls such as memory and time limits.

Compared to execjs—which relies on spawning an external runtime and parsing results—these approaches eliminate the extra process layer, making them generally faster and more predictable.

2. Using Node.js via subprocess

If your goal is to:

Work with complex npm ecosystems
Execute real-world JavaScript projects
Rely on Node-specific behavior

then using Node.js with Python’s subprocess is a better choice than execjs.

In this approach, you explicitly manage:

The Node process
Standard input/output
Timeouts and error handling

While this is heavier than embedded engines, it provides the best compatibility.

3. Executing in a Real Browser Environment

If your use case involves:

Anti-bot mechanisms
Token/signature generation
Browser fingerprinting
Code depending on window, document, or navigator

then the previous two approaches are insufficient.

In such cases, you should use Playwright.

page.evaluate() runs JavaScript directly in the browser context
add_init_script() allows you to inject scripts before page execution

This approach is heavier, but in many real-world scenarios, it is the only truly reliable solution.

Practical Selection Guide
Pure algorithms / encryption / simple signatures
→ Use quickjs or PyMiniRacer
Heavy dependencies / npm ecosystem / Node-specific logic
→ Use Node.js + subprocess
Browser-dependent logic / obfuscated scripts / environment checks
→ Use Playwright
"""

# eval method: evaluate a JavaScript code string and return the result
# runtime
runtime = execjs.get()
print(runtime)

ret = runtime.eval("new Date().getTime()")
print('timestamp from JS', ret)

ret_2 = runtime.eval("1 + 2")
print('eval: ', ret_2)

# compile method: compile a JavaScript code string into a context, and then call functions in that context
# create a JavaScript context by compiling a JavaScript code string
ctx = execjs.compile(
'''
function add(a, b) {
    return a + b;
}
'''
)
# call method: call a function in the compiled context
result = ctx.call("add", 1, 2)
print('compile: ', result)

# exec_ method: execute a JavaScript code string and return the result
exec_exec = execjs.get()  # get the default runtime
js_code = """
function multiply(a, b) {
    return a * b;
}
return multiply(3, 4);      //execute the function and return the result
"""
result = exec_exec.exec_(js_code)
print('exec_: ', result)

