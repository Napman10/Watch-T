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
    return (await axios.get(`api/project/${id}`, {headers: headers})).data;
};

export const editProject = async (payload) => {
    const id = payload.id;
    console.log(payload)
    return (await axios.put(`api/project/${id}`, payload, {headers: headers})).data;
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

export const deleteProject = async (payload) => {
    const id = payload.id;
    return (await axios.delete(`api/project/delete/${id}`, { payload, headers: headers})).data;
}

export const getProjectStatistics = async (id) => {
    return (await axios.get(`api/project/statistics/${id}`, {headers: headers})).data;
};

export default {
    assignUser,
    getProjects,
    addProject,
    getProject,
    unAssignUser,
    deleteProject,
    getProjectStatistics,
    editProject
};