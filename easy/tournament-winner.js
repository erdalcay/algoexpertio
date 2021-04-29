/**
 * 
 *  Question: Given the names of the teams and the results of each game
 *  in a tournament, find the team that wins the tournament.
 * 
 *  Each game has a winner, there is no tie.
 *  Winner of each game gains 3 points, while loser gets 0.
 * 
 *  Tournament has to have a winner.
 * 
 *  @function tournamentWinner
 *
 *  @param {Array<Array<string>>} competitions
 *    Two dimensional array with each member being an array of the two teams 
 *    that have played a game.
 *    
 *    The order of home and away teams are consistent and always at index 0 and 1 respectively.
 * 
 *  @param {Array<number>} results
 *    Results for each game in the form of binary values.
 *    0 - the away team wins
 *    1 - the home team wins.
 * 
 *    The order of the game results in the results array is the same as competitions array.
 * 
 *  @return {string}
 *    The name of the team that wins the tournament.
 * 
 */

export default function tournamentWinner(competitions, results) {
  let maxScore = 0;
  let winner = '';

  competitions.reduce((acc, val, i) => {
    let gameWinner = val[results[i] ? 0 : 1];
    gameWinner in acc || (acc[gameWinner] = 0);
    acc[gameWinner] += 3;
    acc[gameWinner] > maxScore ? (
      maxScore = acc[gameWinner], winner = gameWinner) : void 0;
    return acc;
  }, {});

  return winner;
}
