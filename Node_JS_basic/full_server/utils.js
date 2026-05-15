const fs = require('fs');

function readDatabase(filepath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filepath, { encoding: 'utf8', flag: 'r' }, (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      const cs = [];
      const swe = [];

      data.slice(1, data.length).split('\n').forEach((student) => {
        student = student.split(',');

        const sdata = [student[0], student[1], student[2]];
        if (student[3] == 'CS') {
          cs.push(sdata);
        } else if (student[3] == 'SWE') {
          swe.push(sdata);
        }
      });

      resolve([cs, swe]);
    });
  });
}
