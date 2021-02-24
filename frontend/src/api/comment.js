import { axios } from '@/utils';
import {headers} from "@/api/headers";

export const getComments = async (issueId) => {
    return (
        await axios.get(`api/issue/comment/list/?issue_id=${issueId}`, {
            headers: headers
        })
    ).data;
};

export const getComment = async (id) => {
    return (await axios.get(`api/issue/comment/${id}`, {headers: headers})).data;
};

export const addComment = async (payload) => {
    return (await axios.post('api/issue/comment/new/', payload, {headers: headers})).data;
};

export const editComment = async (payload) => {
    const id = payload.id;
    return (await axios.put(`api/issue/comment/${id}/update`, payload, {headers: headers})).data;
};

export const deleteComment = async (payload) => {
    const id = payload.id;
    return (await axios.delete(`api/issue/comment/${id}/delete`, {payload, headers: headers})).data;
};

export default {
    getComments,
    addComment,
    getComment,
    editComment,
    deleteComment
};