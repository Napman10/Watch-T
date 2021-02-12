import { axios } from '@/utils';


const headers = {
    'Content-Type': 'application/json',
    'Authorization': `JWT ${localStorage.getItem('token')}`
}

export const getIssues = async (params) => {
    return (
        await axios.get('api/issue/list', {
            params, headers: headers
        })
    ).data;
};

// export const getIssue = async (issueId) => {
//     return (await axios.get(`api/issue/${issueId}`)).data;
// };
//
export const addIssue = async (payload) => {
    return (await axios.post('api/issue/new', payload, {headers: headers})).data;
};

export default {
    getIssues,
    addIssue
};