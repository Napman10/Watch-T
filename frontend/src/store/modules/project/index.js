import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        projects: [],
        project: {},
        loading: false,
        isCreateModalVisible: false
    },
    getters: {
        projects: (state) => state.projects,
        project: (state) => state.project,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible
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
        },
        async addProject({ commit, dispatch }, payload) {
            try {
                const result = await api.addIssue(payload);
                showSuccessNotify(`Проект создан!`);
                setState(commit, { isCreateModalVisible: false });
                dispatch('getProjects');
            } catch (e) {
                showErrorNotify(e.message);
            }
        }
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