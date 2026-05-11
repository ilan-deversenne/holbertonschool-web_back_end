const fs = require('node:fs')

module.exports = function(filename) {
    fs.readFile(filename, 'utf8', (err, data) => {
        if (err) {
            throw new Error('Cannot load the database')
            return
        }

        let lines = 0
        let cs = [], swe = []

        data.split("\n").forEach((line) => {
            if (line.length < 1) return

            lines++
            if (line.split(',')[3] == 'CS') cs.push(line.split(',')[0])
            if (line.split(',')[3] == 'SWE') swe.push(line.split(',')[0])
        })
        lines--

        console.log(`Number of students: ${lines}`)
        console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`)
        console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`)
    })
}
