/**
 * 
 *  Question: Return the two integer values that adds up to the target sum amongst the distinct values in an array.
 * 
 *  @function twoNumberSum
 *
 *  @param {Array<number>} nums
 *    List of distinct integers
 *  @param {number} targetSum
 *    Target value to which the two integers we are looking for are expected to sum up to
 * 
 *  @return {Array<number>|Array}
 *    Array of the two integers that add up to the @targetSum
 *    Or an empty array in case of `not found`
 * 
 */


export default function twoNumberSum(nums, targetSum) {
  const visitedNums = {};

  for (const num of nums) {
    const residual = targetSum - num;
    if (visitedNums[residual]) return [residual, num];
    visitedNums[num] = true;
  }

  return [];
}
