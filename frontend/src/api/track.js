import { axios } from '@/utils';
import {headers} from "@/api/headers";

export const addTrack = async (payload) => {
    return (await axios.post('api/issue/track/create/', payload, {headers: headers})).data;
}

export const deleteTrack = async (payload) => {
    const id = payload.id;
    return (await axios.delete(`api/issue/track/${id}/delete`, {payload, headers: headers})).data;
}

export const getTracks = async (issueId) => {
    return (
        await axios.get(`api/issue/track/list/?issue_id=${issueId}`, {
            headers: headers
        })
    ).data;
};

export default {
    addTrack,
    deleteTrack,
    getTracks
}