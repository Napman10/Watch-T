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

export const addIssue = async (payload) => {
    return (await axios.post('api/issue/new', payload, {headers: headers})).data;
};

export const getChildren = async (params) => {
    return (await axios.get(`api/issue/childlist`, {params, headers: headers})).data;
}

export default {
    getChildren,
    getIssues,
    addIssue,
    getIssue
};