import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        issues: [],
        issue: {},
        loading: false,
        isCreateModalVisible: false
    },
    getters: {
        issue: (state) => state.issue,
        issues: (state) => state.issues,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible
    },
    mutations: {
        SET_STATE
    },
    actions: {
        async getIssues({ commit }, filter) {
            try {
                const result = await api.getIssues(filter);
                setState(commit, { issues: result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        },
        async addIssue({ commit, dispatch }, payload) {
            try {
                await api.addIssue(payload);
                showSuccessNotify(`Задание создано!`);
                setState(commit, { isCreateModalVisible: false });
                dispatch('getIssues');
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
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