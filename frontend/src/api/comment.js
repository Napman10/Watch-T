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

export default {
    getComments,
    addComment,
    getComment
};