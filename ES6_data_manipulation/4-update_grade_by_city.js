export default function updateStudentGradeByCity(students, city, newGrades) {

    return students.filter(s => s.location === city).map((s) => { if (!s.grade) s.grade = 'N/A'; newGrades.map((g) => { if (s.id == g.studentId) s.grade = g.grade; return g; }); return s; });
}
