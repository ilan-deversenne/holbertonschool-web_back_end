export default function getStudentsByLocation(students, city) {

    return students.filter(val => val.location === city);
}
