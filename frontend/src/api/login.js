import { axios } from '@/utils';
import {headers} from "@/api/headers";

export const login = async (payload) => {
    return (await axios.post('/auth/token/login/', payload)).data;
};

export const logout = async (payload) => {
    return (await axios.post('/auth/token/logout/', payload, {headers: headers})).data;
};

export default {
    login,
    logout
};