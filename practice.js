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

var arr_3 = [1,2,3];

console.log(sum_3(...arr_3)); // spread operator, same as sum_3(arr_3[0], arr_3[1], arr_3[2])

var arr_6 = [...arr_3,4,5,6];
console.log(arr_6);

var more_info = {
    location: 'US',
    gender: 'M'
}

var person_more_info = {...person, ...more_info}
console.log(person_more_info);

function f(...args) {
    console.log(args)
    return;
}

f(1,2,3,4);

arr_5 = [...'12345']

console.log('****************');


// deep copy and shallow copy: slice/concat/.../Array.from()

var myarray = ['a', 'b', 'c', 'd', 'e', [1, 2 ,3]];
new_array = myarray.slice();
myarray[0] = 'z';
myarray[5][3] = 4;
console.log(myarray);
console.log(new_array);  // affect the array before/after copy


var a_1 = [1,2,3,4,5,[1,2,3]]
a_2 = JSON.parse(JSON.stringify(a_1));
a_1[0] = 'z';
a_1[5][3] = 4;
console.log(a_1);
console.log(a_2);  // not affect the array before/after copy

console.log('****************');

// CUAD
myarray = ['a', 'b', 'c', 'd', 'e', [1, 2 ,3]];
myarray.push('f', 33, [4, 5, 6], {name: 'cook'});
console.log(myarray);
myarray.pop();
myarray.pop();
myarray.pop();
console.log(myarray);
myarray.unshift('z','x','c');
console.log(myarray);
myarray.shift();
myarray.shift();
console.log(myarray);
myarray.splice(2, 0, 'y', 'w'); // at index 2, delete 0 element, insert 'y' and 'w'
console.log(myarray);

console.log('****************');
// forEach;
var n_arr = [5,55,555,5555,55555];
n_arr.forEach(function (value, index, array){
    console.log(value, index, array);
    }
)

// map same as python

var doubled_arr = n_arr.map(function (value, index, array){
    return 2 * value;
})
console.log(doubled_arr);
console.log('****************');


// filter like map, return in maps if item > n; return item.

// reduce

var _2d_arr = [[1,2,3],[4,5,6],[7,8,9]];
var _1d_arr = _2d_arr.reduce(function (accumulator, currentValue){
    return accumulator.concat(currentValue);
}, [])
console.log(_1d_arr);
console.log('****************');

// find
var aaa = [2,3,5,7,11,13,17,19,23,29];
var res_aaa = aaa.find(function (value){
    return value > 10;
})
console.log(res_aaa); // find the first value > 10

fd_in = aaa.findIndex(e => e > 10);
console.log(fd_in);

console.log(aaa.indexOf(19));
console.log(aaa.includes(1));

console.log('****************');

// slice & concat & sort & reverse & join & toString
var arr_7 = [3,1,4,1,5,9];
console.log(arr_7.slice(2,5)); // slice from index 2 to 4
console.log(arr_7.concat([2,6,5])); // concat two arrays
console.log('****************');
console.log(arr_7.sort()); // sort the array, but not sort number correctly
console.log(arr_7.sort((a,b) => a - b)); // sort number correctly


console.log('****************');
console.log(arr_7.reverse()); // reverse the array
console.log(arr_7.join('-')); // join the array with '-'
console.log(arr_7.toString()); // convert the array to string

console.log('****************');








