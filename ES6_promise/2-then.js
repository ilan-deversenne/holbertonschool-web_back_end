export default function handleResponseFromAPI(promise) {

    return promise.then((val) => {
        console.log('Got a response from the API'); return { status: 200, body: 'success' }
        }).catch((err) => Error());
}
