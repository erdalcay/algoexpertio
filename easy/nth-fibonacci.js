/**
 * 
 *  Question: Find the nth Fibonacci number
 * 
 *  @function getNthFib
 *    Finds the nth number in the Fibonacci sequence
 *
 *  @param {number} n
 *    Order of the number in the sequence
 *    
 *  @return {number}
 *    Nth Fibonacci number
 * 
 */

 export default function getNthFib(n) {
  /**
   * Hard checking the first 3 (including special case for 0) numbers
   * in the sequence and reducing the number of steps
   * by two since the sequence generator starts at
   * step 3.
   */
  if (n < 2) return n;
  // First two step (+0) is skipped.
  n = n - 2;

  const sequence = fibSequence();

  while (n >= 0) {
    if (!n) return sequence.next().value;
    sequence.next();
    n--;
  }
}

/**
 * 
 * @function fibSequence
 *    Generator fn that populates the Fibonacci sequence
 *    
 *    Starts from the 3rd number in the sequence (including 0)
 * 
 * @yield {number}
 *    Next number in the sequence
 */
function * fibSequence() {
  let f0 = 0;
  let f1 = 1;
  while (true) {
    const fib = f0 + f1;
    yield fib;		
    f0 = f1;
    f1 = fib;
  }
}