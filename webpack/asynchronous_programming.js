const MyPromise = new Promise((resolve, reject) => {
    let c = false;
    if (c){
        resolve('success');
    }
    else {
        reject('fail')
    }
})

console.log(MyPromise)

res = MyPromise.then((value) => {
    console.log(value);
}).catch((err) => {
    console.log(err);
}).finally(() => {
    console.log('finished');
});

/* -------------------------------------------------------------------------------------*/

function mock_doing(sth, time) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(sth);
        }, time);
    })
}

var task_1 = mock_doing('first step', 1000)
console.log(task_1);
var done_task_1 = task_1.then((res) => {console.log(res)});

setTimeout(() => {console.log(done_task_1);}, 2000);


/* -------------------------------------------------------------------------------------*/

const p1 = new Promise((resolve) => {setTimeout(resolve, 2000, 'first')});
const p2 = new Promise((resolve) => {setTimeout(resolve, 3000, 'second')});

Promise.all([p1, p2]).then((res) => {console.log(res)});
Promise.race([p1, p2]).then((res) => {console.log(res)});

/* -------------------------------------------------------------------------------------*/
// Candy
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function task1(){
    await sleep(5000);
    return 'task 1 finished'
}

async function task2(){
    await sleep(6000);
    return 'task 2 finished'
}

async function mock_task() {
    console.time('time spend');
    const [res1, res2] = await Promise.all([task1(), task2()])
    console.log(res1);
    console.log(res2);
    console.timeEnd('time spend');
}
mock_task();