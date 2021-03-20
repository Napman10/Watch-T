import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        projects: [],
        project: {},
        loading: false,
        isCreateModalVisible: false,
        isAssignModalVisible: false,
        isUnAssignModalVisible: false
    },
    getters: {
        projects: (state) => state.projects,
        project: (state) => state.project,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible,
        isAssignModalVisible: (state) => state.isAssignModalVisible,
        isUnAssignModalVisible: (state) => state.isUnAssignModalVisible
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
                showErrorNotify(e);
            }
        },
        async addProject({ commit, dispatch }, payload) {
            try {
                await api.addProject(payload);
                showSuccessNotify(`Проект создан!`);
                setState(commit, { isCreateModalVisible: false });
                dispatch('getProjects');
            } catch (e) {
                showErrorNotify(e);
            }
        },
        async getProject({ commit }, projectId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getProject(projectId);
                setState(commit, { project: result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        },
        async assignUser({ commit }, payload) {
            try {
                await api.assignUser(payload);
                showSuccessNotify(`Сотрудник назначен на проект`);
                setState(commit, { isAssignModalVisible: false });
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async unAssignUser({ commit }, payload) {
            try {
                await api.unAssignUser(payload);
                showSuccessNotify(`Сотрудник отстранен от проекта`);
                setState(commit, { isUnAssignModalVisible: false });
            } catch (e) {
                showErrorNotify(e.message);
            }
        }
    }
};