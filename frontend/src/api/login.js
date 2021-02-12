import { axios } from '@/utils';

export const login = async (payload) => {
    return (await axios.post('/api/user/login/', payload)).data;
};

export default {
    login,
};