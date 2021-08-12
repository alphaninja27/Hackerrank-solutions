function modifyArray(nums) {
    var something = function(n){
        if(n%2==0)
            return n*2;
        else
            return n*3;
    }
    var newArray = nums.map(something);
    return newArray;
}