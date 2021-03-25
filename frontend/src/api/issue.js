import { axios } from '@/utils';
import {headers} from "@/api/headers";

export const getIssues = async (params) => {
    return (
        await axios.get('api/issue/list', {
            params, headers: headers
        })
    ).data;
};

export const getIssue = async (id) => {
    return (await axios.get(`api/issue/${id}/`, {headers: headers})).data;
};

export const changeIssue = async (payload) => {
    const id = payload.id;
    return (await axios.put(`api/issue/${id}/`, payload, {headers: headers})).data;
};

export const addIssue = async (payload) => {
    return (await axios.post('api/issue/new', payload, {headers: headers})).data;
};

export const getChildren = async (params) => {
    return (await axios.get(`api/issue/childlist`, {params, headers: headers})).data;
}

export const deleteIssue = async (payload) => {
    const id = payload.id;
    return (await axios.delete(`api/issue/delete/${id}`, { payload, headers: headers})).data;
}

export const assignUserIssue = async (payload) => {
    const id = payload.id;
    return (await axios.put(`api/issue/${id}/`, payload, {headers: headers})).data;
}

export default {
    getChildren,
    assignUserIssue,
    getIssues,
    addIssue,
    getIssue,
    deleteIssue,
    changeIssue
};