/**
 * 
 *  Question: Given a binary search tree and a target integer, 
 *  find the closest node value to the target integer.
 *  
 *  @function findClosestValueInBST
 *
 *  @param {Object} tree
 *  @param {number} tree.value
 *  @param {Object|null} tree.left
 *  @param {Object|null} tree.right
 *    Binary search tree with @value - @left - @right properties.
 * 
 *  @param {number} target
 *    The number to which the closest number in the tree is being searched.
 * 
 *  @return {number}
 *    The closest-to-the-target value found in the tree.
 * 
 */

export default function findClosestValueInBST(tree, target) {
  let currentNode = tree;
  let closest = target;
  let minDifference = Math.abs(target - currentNode.value);

  while (currentNode) {
    const difference = target - currentNode.value;
    const absDifference = Math.abs(difference);
    
    absDifference < minDifference ? (
      minDifference = absDifference, closest = currentNode.value
    ) : void 0;
    
    difference === 0 && (void currentNode.value)
    difference > 0 ? (currentNode = currentNode.right) : (currentNode = currentNode.left);

  }

  return closest;
}