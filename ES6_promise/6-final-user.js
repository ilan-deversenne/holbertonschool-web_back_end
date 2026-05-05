import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject'; 

export default function handleProfileSignup(firstName, lastName, fileName) {

    return Promise.allSettled([ signUpUser(firstName, lastName), uploadPhoto(fileName) ])
        .then((values) => {
            console.log( [
                { status: values[0].status, value: values[0].value },
                { status: values[1].status, value: values[1].reason ? values[1].reason.toString() : values[1].value }
            ] )
        });
}
