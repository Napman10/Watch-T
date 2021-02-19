import { axios } from '@/utils';
import {headers} from "@/api/headers";

export const getUsers = async (params) => {
    return (
        await axios.get('api/user/list/', {
            params, headers: headers
        })
    ).data;
};

export const getUser = async (id) => {
    return (await axios.get(`api/user/${id}`, {headers: headers})).data;
};

export const addUser = async (payload) => {
    return (await axios.post('api/user/', payload, {headers: headers})).data;
};

export default {
    getUsers,
    addUser,
    getUser
};