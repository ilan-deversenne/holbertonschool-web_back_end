export default function cleanSet(set, startString) {

    let res = "";
    set.forEach((val) => { if (val.startsWith(startString) && startString != '') res += `${val.replace(startString, '')}-` });

    return res.slice(0, -1);
}
