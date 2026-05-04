export default function hasValuesFromArray(set, array) {

    let has = true;
    array.map((val) => { if (!set.has(val)) has = false });

    return has;
}
