import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject'; 

export default function handleProfileSignup(firstName, lastName, fileName) {

    let result = [];
    return Promise.allSettled([ signUpUser(firstName, lastName), uploadPhoto(fileName) ])
        .then((values) => { return [ {status: values[0].status, value: values[0].value}, {status: values[0].status, value: values[0].value} ] });
}
