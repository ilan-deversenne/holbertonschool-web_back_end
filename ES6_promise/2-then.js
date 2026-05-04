export default function handleResponseFromAPI(promise) {

    return promise.then((val) => console.log('Got a response from the API')).catch((err) => Error());
}
