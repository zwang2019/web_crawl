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

