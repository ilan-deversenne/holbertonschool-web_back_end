const fs = require('node:fs/promises');

const countStudents = async (filename) => fs.readFile(
  filename,
  { encoding: 'utf8', flag: 'r' },
).then((data) => {
  let lines = 0;
  const cs = []; const
    swe = [];

  data.split('\n').forEach((line) => {
    if (line.length < 1) return;
    if (line.split(',')[0].length < 1) return;

    lines += 1;

    if (line.split(',')[3] === 'CS') cs.push(line.split(',')[0]);
    if (line.split(',')[3] === 'SWE') swe.push(line.split(',')[0]);
  });

  if (lines > 0) lines -= 1;

  console.log(`Number of students: ${lines}`);
  console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
  console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
}).catch(() => {
  throw new Error('Error: Cannot load the database');
});

module.exports = countStudents;
