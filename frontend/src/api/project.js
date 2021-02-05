import { axios } from '@/utils';

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
// export const addIssue = async (payload) => {
//     return (await axios.post('api/project/new', payload)).data;
// };

export default {
    getProjects
};