import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        projects: [],
        project: {}
    },
    getters: {
        projects: (state) => state.projects
    },
    mutations: {
        SET_STATE
    },
    actions: {
        async getProjects({ commit }, filter) {
            try {
                const result = await api.getProjects(filter);
                setState(commit, { projects: result });
            } catch (e) {
                showErrorNotify(e.message);
            }
        }
        // async addIssue({ commit, dispatch }, payload) {
        //     try {
        //         const result = await api.addIssue(payload);
        //         if (!result.isSuccess) {
        //             return showErrorNotify(result.errorMessage);
        //         }
        //         showSuccessNotify(`Задание создано! Id: ${result.result}`);
        //         setState(commit, { isCreateModalVisible: false });
        //         dispatch('getIssues');
        //     } catch (e) {
        //         showErrorNotify(e.message);
        //     }
        // },
        // async getIssue({ commit }, issueId) {
        //     try {
        //         setState(commit, { loading: true });
        //         const result = await api.getIssue(issueId);
        //         if (!result.isSuccess) {
        //             return showErrorNotify(result.errorMessage);
        //         }
        //         setState(commit, { direction: result.result });
        //     } catch (e) {
        //         showErrorNotify(e.message);
        //     } finally {
        //         setState(commit, { loading: false });
        //     }
        // }
    }
};