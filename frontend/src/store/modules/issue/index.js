import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        issues: [],
        loading: false,
        isCreateModalVisible: false,
        issue: {},
        // selectedPatient: {}
    },
    getters: {
        issues: (state) => state.issues,
    },
    mutations: {
        SET_STATE,
        SELECT_PATIENT(state, patient) {
            state.selectedPatient = { ...patient };
        }
    },
    actions: {
        async getIssues({ commit }, filter) {
            try {
                setState(commit, { loading: true });
                const result = await api.getIssue(filter);
                if (!result.isSuccess) {
                    return showErrorNotify(result.errorMessage);
                }
                setState(commit, { directions: result.result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        },
        async addIssue({ commit, dispatch }, payload) {
            try {
                const result = await api.addIssue(payload);
                if (!result.isSuccess) {
                    return showErrorNotify(result.errorMessage);
                }
                showSuccessNotify(`Задание создано! Id: ${result.result}`);
                setState(commit, { isCreateModalVisible: false });
                dispatch('getIssues');
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async getIssue({ commit }, issueId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getIssue(issueId);
                if (!result.isSuccess) {
                    return showErrorNotify(result.errorMessage);
                }
                setState(commit, { direction: result.result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        }
    }
};