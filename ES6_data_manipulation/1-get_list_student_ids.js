export default function getListStudentIds(students) {
    if (!Array.isArray(students)) return [];
    return students.map((val) => { return val.id });
}
