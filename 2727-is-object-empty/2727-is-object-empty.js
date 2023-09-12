/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    
    if (typeof(obj) == "object") {
        return Object.keys(obj).length == 0
    }
    
    return obj.length == 0
};