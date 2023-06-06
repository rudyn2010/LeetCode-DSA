/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let seen = Array(grid.length).fill().map(() => Array(grid[0].length).fill(false)),
        islands = 0;

    for (let i = 0; i < grid.length; i++){
        for (let k = 0; k < grid[0].length; k++){
            if (seen[i][k]){
                continue;
            }
            if (grid[i][k] === '1'){
                dfs(i,k);
                islands += 1;
            } 
        }
    }

    function dfs(y, x){

        seen[y][x] = true;

        if (y + 1 < grid.length && grid[y + 1][x] === '1' && seen[y + 1][x] === false){
           dfs(y + 1, x);
        }
        if (y - 1 >= 0 && grid[y - 1][x] === '1' && seen[y - 1][x] === false){
            dfs(y - 1, x)
        }
        if (x - 1 >= 0 && grid[y][x - 1] === '1' && seen[y][x - 1] === false){
            dfs(y, x - 1)
        }
        if (x + 1 < grid[0].length && grid[y][x + 1] === '1' && seen[y][x + 1] === false){
            dfs(y, x + 1)
        }
    }

    return islands;
};