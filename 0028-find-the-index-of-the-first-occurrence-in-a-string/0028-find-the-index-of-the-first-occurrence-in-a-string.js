/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    
    if (haystack === "") {
        return -1 
    };
    
    let start = 0;
    let end = needle.length
    
    //while (start < haystack.length) {
    while ((haystack.length - start) >= needle.length - 1) {
        let word = haystack.slice(start, end);
        if (word === needle) {
            return start
        };
        start += 1
        end += 1
    };
    return -1
};

/* First edge case is to check if haystack is an empty.
Next loop through haystack length starting at 0 and use 
.slice to verify word. 2nd arg passed into method is 
non-inclusive*/