function convert(s: string, numRows: number): string {
  if (numRows === 1) return s; // Edge case if only 1 row

  let move = 1, row = 0;
  const res: string[] = new Array(numRows).fill(""); // Initialize an array of empty strings

  for (let i = 0; i < s.length; i++) {
    res[row] += s[i];

    if (row === numRows - 1) {
      move = -1;
    } else if (row === 0) {
      move = 1;
    }

    row = (row + move) % numRows;
  }

  return res.join("");
};



