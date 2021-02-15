export const headers = {
    'Content-Type': 'application/json',
    'Authorization': "Token " + localStorage.getItem('token')
};

export default {
    headers
};