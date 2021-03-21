import { axios } from '@/utils';
import {headers} from "@/api/headers";

export const getProjects = async (params) => {
    return (
        await axios.get('api/project/list', {
            params, headers: headers
        })
    ).data;
};

export const getProject = async (id) => {
    return (await axios.get(`api/project/${id}`, {headers: headers}));
};

export const addProject = async (payload) => {
    return (await axios.post('api/project/new', payload, {headers: headers})).data;
};

export const assignUser = async (payload) => {
    return (await axios.post('api/project/assign/', payload, {headers: headers})).data;
}

export const unAssignUser = async (payload) => {
    return (await axios.delete(`api/project/assign/?project_id=${payload.project_id}&user=${payload.user}`,
        {payload, headers: headers})).data;
}

export default {
    assignUser,
    getProjects,
    addProject,
    getProject,
    unAssignUser
};