//let arr = ["aa", "ab", "ba", "ac", "acc", "bc", "aaa", "bac", "cab"];
//arr = ["eat","tea","tan","ate","nat","bat"]
//arr = ["bdddddddddd"]
//
//const map = new Map();
//
//const freqHash = new Array(26).fill(0)
//
//for (const word of arr) {
//  let hash = newHash();
//  for(const c of word){
//    const code = c.charCodeAt(0) - 97;
//    hash[code] += 1;
//  }
//  console.log(hash)
//  const hashKey = hash.join("-")
//  const currentGroup = map.get(hashKey) || []
//  currentGroup.push(word)
//  map.set(hashKey, currentGroup)
//}
//
//
//
//
//
//

/* eslint quotes: ["error", "double"], curly: 2 */

function bin(n: number): string {
  return (n >>> 0).toString(2).padStart(6, "0");
}

function print(...s) {
  console.log(s.join(" "));
}

function println(...s) {
  print(...s);
  print();
}


//console.log(Array.from(map.entries()))


function sumOfSquares(n) {
  let sum = 0;
  while (n > 0) {
    const digit = n % 10;
    n = (n / 10) >>> 0;
    sum += digit * digit;
  }

  return sum;
}

function isHappy(n) {
  const visited = {};

  while (!visited[n]) {
    print(JSON.stringify(visited));
    visited[n] = true;
    n = sumOfSquares(n);
    println(n);
    if (n === 1) {
      return true;
    }
  }

  return false;
};


print(isHappy(4));
