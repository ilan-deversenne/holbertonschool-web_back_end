export default function cleanSet(set, startString) {
    if (!startString || startString == '') return '';

    let res = "";
    set.forEach((val) => { if (val.startsWith(startString)) res += `${val.replace(startString, '')}-` });

    return res.slice(0, -1);
}
