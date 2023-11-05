/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise(async (res, rej) => {
        let len = functions.length, count = 0;
        const ans = new Array(len);
        functions.forEach(async (func, ind) => {
            try {
                let val = await func();
                ans[ind] = val;
                count++
                if (count === len) res(ans);
            } catch (err) {
                rej(err);
            } 
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */