import axiosInstance from 'axios';

const axios = axiosInstance.create({
    baseURL: 'http://127.0.0.1:8000/',
    responseType: 'json',
    headers: {
        'Content-Type': 'application/json; charset=utf-8'
    }
});

window._http = axios;
window.axios = axios;

export { axios };