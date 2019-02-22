import * as request from 'superagent';

export function testApi() {
    return request
        .get(`http://0.0.0.0:5000/search`)
        .then(response => {
            const body = response.body;
            return {body};
        })
        .catch(error => {
            return {error};
        });　
}
