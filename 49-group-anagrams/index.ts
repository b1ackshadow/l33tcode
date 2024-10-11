function groupAnagrams(strs: string[]): string[][] {
  const mapping = new Map<string, string[]>();

  for (const word of strs) {
    let sortedWord = word.split('').sort().join('')
    console.log(sortedWord)
    let updatedArr = mapping.get(sortedWord) || [];

    updatedArr.push(word)
    mapping.set(sortedWord, updatedArr);

  }
  return Array.from(mapping.values());

}

let input = ["a"];
const result = groupAnagrams(input);
console.log(result);
