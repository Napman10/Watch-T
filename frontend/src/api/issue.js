import { axios } from '@/utils';

export const getIssues = async (params) => {
    return (
        await axios.get('api/issue', {
            params
        })
    ).data;
};

// export const getIssue = async (issueId) => {
//     return (await axios.get(`api/issue/${issueId}`)).data;
// };
//
// export const addIssue = async (payload) => {
//     return (await axios.post('api/issue', payload)).data;
// };

export default {
    getIssues
};