function wordPattern(pattern: string, s: string): boolean {
  let patternMap: any = {},
    wordMap: any = {};
  let wordList = s.split(" ");

  if (pattern.length !== wordList.length) {
    return false;
  }


  // given only single space between words and no trailing spaces. using split for convenience
  for (let i = 0; i < pattern.length; i++) {
    let p = pattern[i], w = wordList[i];
    if ((patternMap[p] !== w) || (wordMap[w] !== p)) {
      return false;
    }

    patternMap[pattern[i]] = wordList[i];
    wordMap[wordList[i]] = pattern[i];
  }

  return true;
}


let  pattern = "aaaa", s = "dog cat cat dog"

console.log(wordPattern(pattern,s))

