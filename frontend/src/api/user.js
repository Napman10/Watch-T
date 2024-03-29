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

export const getUserStatistics = async (id) => {
    return (await axios.get(`api/user/statistics/${id}`, {headers: headers})).data;
};

export const addUser = async (payload) => {
    return (await axios.post('api/user/', payload, {headers: headers})).data;
};

export const editUser = async (payload) => {
    const id = payload.id;
    return (await axios.put(`api/user/${id}`, payload, {headers: headers})).data;
}

export const deleteUser = async (payload) => {
    const id = payload.id;
    return (await axios.delete(`api/user/${id}`, { payload, headers: headers})).data;
}

export const missingSkills = async (params) => {
    return (
        await axios.get('api/user/missing_skills/', {
            params, headers: headers
        })
    ).data;
}


export const getMe = async (token) => {
    return (await axios.get(`api/user/me`, { headers: {
        'Content-Type': 'application/json',
        'Authorization': "Token " + token
    }}))
        .data;
}

export default {
    getUsers,
    getMe,
    addUser,
    getUser,
    editUser,
    deleteUser,
    getUserStatistics,
    missingSkills
};