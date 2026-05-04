export default function getStudentIdsSum(students) {

    return students.reduce((sum, data) => { return sum + data.id }, 0);
}
