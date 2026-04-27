export default function appendToEachArrayValue(array, appendString) {
  for (const el of array) {
    array[array.indexOf(el)] = appendString + el;
  }

  return array;
}
