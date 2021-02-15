import { axios } from '@/utils';
import {headers} from "@/api/headers";

export const getUsers = async (params) => {
    return (
        await axios.get('api/user/list', {
            params, headers: headers
        })
    ).data;
};

// export const getIssue = async (issueId) => {
//     return (await axios.get(`api/issue/${issueId}`)).data;
// };
//
export const addUser = async (payload) => {
    return (await axios.post('api/user/', payload, {headers: headers})).data;
};

export default {
    getUsers,
    addUser
};