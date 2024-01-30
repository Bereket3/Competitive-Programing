/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort(function(a, b){return a-b})
    let curr_sum = nums.slice(0, 3).reduce((partialSum, a) => partialSum + a, 0);
    let out = curr_sum

    for(let i = 0; i < (nums.length - 2); i++){
        let left = i + 1;
        let right = nums.length - 1;
        while(left < right) {
            curr_sum = nums[left] + nums[i] + nums[right]
            if(Math.abs(curr_sum - target) < Math.abs(out - target)){
                out = curr_sum;
            }
            if (curr_sum > target){
                right--;
            } else {
                left++;
            } 
            if (curr_sum === target) {
                return target;
            }
        }
    }
    return out;
};