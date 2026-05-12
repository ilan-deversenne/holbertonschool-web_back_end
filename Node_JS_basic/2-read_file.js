const fs = require('node:fs');

const countStudents = (filename) => {
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) throw new Error('Cannot load the database');

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
    lines -= 1;

    console.log(`Number of students: ${lines}`);
    console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
    console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
  });
};

module.exports = countStudents;
