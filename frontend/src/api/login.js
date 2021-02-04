import { axios } from '@/utils';

export const login = async (payload) => {
    return (await axios.post('/auth/jwt/create', payload)).data;
};

export default {
    login
};