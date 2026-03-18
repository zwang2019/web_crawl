console.log('hi');


// comment
/*  multi lines comments
    console.log('hi')

*/

console.log('using ; to end a line');


// var define variables in the global scope
var name = 'tim';
console.log(name);


// let define variables block scope
/*
if (true){
    var x = 3
    let y = 4
};
console.log(x);
console.log(y);

gives ReferenceError: y is not defined

 */


// const define constants, constants can't be changed

const SEED = 1;
console.log(SEED);

// Doing reverse engineering sometime needs define the key words. such as: var String = '333'

console.log(String(123));


// Rules of naming variables

var _0x123 = '123';
var $_sadfe = 'afeaf';
var name = 'cook';


// Data type

/*
string: 'aaa'
number: 1
boolean: true/false
null: null
undefined: var a
dictionary: {'name':'tim','age':88}
function: var a = function(){return 233;}
array: [1,2,3,4,5]

 */

// logic operator
// and &&
// or ||
// not !


// operator
// + - * / ** % += -= *=
console.log(Math.ceil(1.1));
console.log(Math.floor(1.9));

// ++x and x++, --y and y--
// ++x means x = x + 1, then return x
// x++ means return x, then x = x + 1
console.log('****************');

var x = 1;
console.log(++x);
console.log(x);

var y = 1;
console.log(y++);
console.log(y);

console.log('****************');

// ==
console.log(10 == 10);
console.log(10 == '10');
console.log(10 === '10');

console.log(10 != '10');
console.log(10 !== '10');

// ?
console.log('****************');
var x = 10;
var res = x > 11 ? x = 1 : x = 2; // if x > 9, then x = 1, else x = 2
console.log(res);


// string
/*
var a = 'hello';
var b = 'world';
var res_1 = a + ' ' + b;
var res_2 = `{a} ${b}`;
var res_3 = a.concat(' ', b)
 */

console.log('****************');
var a = 'hello';
var b = 'world';
var res_2 = `${a} ${b}`;
console.log(res_2);

console.log(res_2.length);
console.log(res_2.toUpperCase());
console.log(res_2.charAt(0));
console.log(res_2.slice(0,7)); // same as python

console.log(res_2.split(' '));
console.log(res_2.indexOf('l')) // find first l

var res_3 = a + ' ' + b + b
console.log(res_3.replace('world', 'tim')); // replace first world with tim
console.log(res_3.replace(/world/g, 'tim')); // replace all world with tim, g means global

console.log(('        ' + res_3).trim());
var c = 1;
console.log(c.toString());
console.log('****************');


// function

function name_1(){
    console.log('steve jobs');
}
name_1();


var name_2 = function(){
    console.log('tim cook');
};
name_2();

!function (){
    console.log('execute without calling');
}();

~function (){
    console.log('execute without calling');
}();

!function (a){
    a = a + 5;
    console.log(a);
    return a
}(function (){return 5}());


var d = function (a){
    a = a + 5;
    console.log(a);
    return a
}(function (){return 5}());

var aa;
!function (){
    function hh(){
        // loader
        return 666
    }
    aa = hh
}();

console.log(aa());

console.log('****************');


// for
var arr = ['a', 'b', 'c', 'd'];
for (let index in arr){
    console.log(index); // index
}

for (let index in arr){
    console.log(arr[index]); // value
}

for (let value of arr){
    console.log(value); // value
}

const map = new Map();
map.set('k1','v1');
map.set('k2','v2');

for (let [k,v] of map){
    console.log(k);
    console.log(v);
}


arr = ['a', 'b', 'c', 'd', 'e'];
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);  // 输出每个元素
}

console.log('****************');

// arrow function ()=>{}

var p = (arg) => {
    console.log(arg);
};
p(10);

console.log('****************');

// this 的用法
// 在全局上下文中，this 指向 window (浏览器) 或 global (Node.js)
console.log(this);  // 在浏览器中输出 Window 对象

console.log('****************');
// 在普通函数中，this 指向调用该函数的对象（严格模式下为 undefined）
function showThis() {
    console.log(this);
}
showThis();  // 全局调用，指向 window

console.log('****************');
// 在对象方法中，this 指向该对象
const obj = {
    name: 'tim',
    greet: function() {
        console.log('Hello, ' + this.name);
    }
};
obj.greet();  // 输出: Hello, tim

console.log('****************');
// 在构造函数中，this 指向新创建的实例
function Person(name) {
    this.name = name;
    this.sayHi = function() {
        console.log('Hi, ' + this.name);
    };
}
const person = new Person('cook');
person.sayHi();  // 输出: Hi, cook

console.log('****************');
// 在箭头函数中，this 继承自外层作用域
const arrowObj = {
    name : 'arrow',
    greet: () => {
        console.log('Hello, ' + this.name);  // this 指向全局或外层
    }
};
arrowObj.greet();  // 可能输出 undefined 或全局的 name

console.log('****************');
// 使用 call/apply/bind 改变 this
function introduce() {
    console.log('I am ' + this.name);
}
const user = { name: 'jobs' };
introduce.call(user);  // 输出: I am jobs

console.log('****************');

/*
const bbbbb = {
    name: 'steve',
    say: function () {
        setTimeout(()=>{
            console.log(this.name); // this 指向 bbbbb 对象
        }, 2000)
    }
}
bbbbb.say()

console.log('****************');
*/

// object
var person_1 = {
    name: 'Tim',
    job: 'CEO',
    age: 65
};

console.log(person_1.name)
console.log(person_1['job'])


res = JSON.stringify(person_1);
console.log(res, typeof res);

var person_back = JSON.parse(res);
console.log(person_back, typeof person_back);

// Syntactic sugar: Object destructuring
/*
var {job, age, salary} = person_1;
console.log(job, age, salary);
*/

// rename the destructed variable

var {job:occupation} = person_1;
console.log(occupation, person_1);


var {name= 'unknow', job= 'unknow', salary = 'unknow', gender = 'unknow'} = person_1;  // set default value
console.log(name, job,salary, gender);

var person_2 = {
    name: 'zzz',
    occupation: {
        company: 'apple',
        job: 'xxx',
    }
}

var {occupation:{company, job, salary}} = person_2;
console.log(company, job, salary);


function who ({name, job}){
    return [name, job]
}

console.log(who(person_1));


// break and continue same as C

console.log('****************');
// Exception handling

try {
    console.log(zzz());
}
catch (error){
    console.log('error: ' + error);
}


console.log('****************');

// import and export

module.exports = introduce;

console.log('****************');

// Syntactic sugar: ... spread operator

function sum_3 (x,y,z){
    return x+y+z;
}

var arr_3 = [6,6,8];

console.log(sum_3(...arr_3)); // spread operator, same as sum_3(arr_3[0], arr_3[1], arr_3[2])









