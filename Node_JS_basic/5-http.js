const fs = require('node:fs');
const http = require('http');

const countStudents = async (filename) => new Promise((resolve, reject) => {
  fs.readFile(filename, { encoding: 'utf8', flag: 'r' }, (err, data) => {
    if (err) reject(Error('Cannot load the database'));

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

    let students = '';
    students += `Number of students: ${lines}\n`;
    students += `Number of students in CS: ${cs.length}. List: ${cs.join(', ')}\n`;
    students += `Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`;

    resolve(students);
  });
});

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url == '/') {
    res.end('Holberton School!');

  } else if (req.url == '/students') {
    countStudents(process.argv[2]).then((students) => {
      res.end(`This is the list of our students\n${students}`);
    });
  } else {
    res.end();
  }
});

app.listen(1245, 'localhost');
module.exports = app;
