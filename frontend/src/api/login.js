import { axios } from '@/utils';

export const login = async (payload) => {
    return (await axios.post('/auth/token/login', payload)).data;
};

export default {
    login
};