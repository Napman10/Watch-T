import { axios } from '@/utils';

export const login = async (payload) => {
    return (await axios.post('/api/user/obtain_token/', payload)).data;
};

export const logout = async (payload) => {
    return (await axios.post('/api/user/logout/', payload)).data;
};

export default {
    login,
    logout
};