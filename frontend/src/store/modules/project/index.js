import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        projects: [],
        project: {},
        loading: false,
        unAssignedStuff: false,
        isCreateModalVisible: false,
        isAssignModalVisible: false,
        isUnAssignModalVisible: false
    },
    getters: {
        projects: (state) => state.projects,
        project: (state) => state.project,
        unAssignedStuff: (state) => state.unAssignedStuff,
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
                showErrorNotify(e.response.data.detail);
            }
        },
        async getProject({ commit }, projectId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getProject(projectId);
                const stat = await api.getProjectStatistics(projectId);
                setState(commit, { project: {...result, ...stat}, unAssignedStuff: false });
            } catch (e) {
                const assignedStuffOnlyDetail = 'You do not have permission to watch this project';
                const detail = e.response.data.detail;
                if (detail === assignedStuffOnlyDetail) {
                    setState(commit, { unAssignedStuff: true });
                }
                else {
                    showErrorNotify(detail);
                }

            } finally {
                setState(commit, { loading: false });
            }
        },
        async deleteProject({dispatch }, payload) {
            try {
                await api.deleteProject(payload);
                showSuccessNotify(`Проект удален`);
                dispatch('getProjects');
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        },
        async assignUser({ commit }, payload) {
            try {
                await api.assignUser(payload);
                showSuccessNotify(`Сотрудник назначен на проект`);
                setState(commit, { isAssignModalVisible: false });
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        },
        async unAssignUser({ commit }, payload) {
            try {
                await api.unAssignUser(payload);
                showSuccessNotify(`Сотрудник отстранен от проекта`);
                setState(commit, { isUnAssignModalVisible: false });
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        }
    }
};