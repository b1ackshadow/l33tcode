// EASY

function strStr(haystack: string, needle: string): number {

  for (let i = 0; i <= haystack.length - needle.length; i++) {
    let counter = 0;
    while (counter < needle.length && haystack[i + counter] === needle[counter]) {
      counter++;
    }

    if (counter === needle.length) {
      return i;
    }
  }
  return -1;
};


let haystack = "sadbutsad", needle = "sad", Output = 0;

console.log(strStr(haystack, needle));
haystack = "leetcode"; needle = "leeto"; Output = -1;

console.log(strStr(haystack, needle));


