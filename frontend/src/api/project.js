import { axios } from '@/utils';

const headers = {
    'Content-Type': 'application/json',
    'Authorization': localStorage.getItem('token')
}

export const getProjects = async (params) => {
    return (
        await axios.get('api/project/list', {
            params
        })
    ).data;
};

// export const getIssue = async (projectId) => {
//     return (await axios.get(`api/project/${projectId}`)).data;
// };
//
export const addProject = async (payload) => {
    return (await axios.post('api/project/new', payload, {headers: headers})).data;
};

export default {
    getProjects,
    addProject
};