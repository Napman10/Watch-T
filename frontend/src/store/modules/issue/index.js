import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';
import { textToMinutes } from '@/utils/transfer';

export default {
    namespaced: true,
    state: {
        issues: [],
        issue: {},
        comments: [],
        comment : {},
        tracks: [],
        track: {},
        children: [],
        loading: false,
        isCreateModalVisible: false,
        editCommentModalVisible: false,
        descIssueModalVisible: false,
        descProjectIssueModalVisible: false,
        isAssignModalVisible: false
    },
    getters: {
        issue: (state) => state.issue,
        issues: (state) => state.issues,
        comment: (state) => state.comment,
        comments: (state) => state.comments,
        tracks: (state) => state.tracks,
        track: (state) => state.track,
        children: (state) => state.children,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible,
        editCommentModalVisible: (state) => state.editCommentModalVisible,
        descIssueModalVisible: (state) => state.descIssueModalVisible,
        descProjectIssueModalVisible: (state) => state.descProjectIssueModalVisible,
        isAssignModalVisible: (state) => state.isAssignModalVisible
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
            payload.want_time = textToMinutes(payload.want_time);
            try {
                await api.addIssue(payload);
                showSuccessNotify(`Задание создано!`);
                setState(commit, { isCreateModalVisible: false });
                dispatch('getIssues');
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        },
        async getIssue({ commit, dispatch}, issueId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getIssue(issueId);
                setState(commit, { issue: result });
                dispatch('getChildren', {'id': issueId});
                dispatch('getComments', issueId);
                dispatch('getTracks', issueId);
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
        async deleteIssue({dispatch }, payload) {
            try {
                await api.deleteIssue(payload);
                showSuccessNotify(`Задание удалено`);
                dispatch('getIssues');
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        },
        async getComments({ commit }, issueId) {
            try {
                const result = await api.getComments(issueId);
                setState(commit, { comments: result });
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async addComment({dispatch }, payload) {
            try {
                await api.addComment(payload);
                dispatch('getIssue', payload.issue_id);
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async editComment({dispatch }, payload){
            try {
                await api.editComment(payload);
                dispatch('getIssue', payload.issue_id);
            } catch (e){
                showErrorNotify(e.message);
            }
        },
        async deleteComment({dispatch }, payload){
            try {
                await api.deleteComment(payload);
                dispatch('getIssue', payload.issue_id);
            } catch (e){
                showErrorNotify(e.message);
            }
        },
        async getTracks({ commit }, issueId) {
            try {
                const result = await api.getTracks(issueId);
                setState(commit, { tracks: result });
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async addTrack({dispatch }, payload) {
            payload.minutes = textToMinutes(payload.minutes);

            try {
                await api.addTrack(payload);
                dispatch('getIssue', payload.issue_id);
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async deleteTrack({dispatch }, payload){
            try {
                await api.deleteTrack(payload);
                dispatch('getIssue', payload.issue_id);
            } catch (e){
                showErrorNotify(e.message);
            }
        },
        async getChildren({ commit }, filter) {
            try {
                const result = await api.getChildren(filter);
                setState(commit, { children: result });
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async assignUser({ commit }, payload) {
            try {
                await api.assignUserIssue(payload);
                showSuccessNotify(`Задача назначена на сотрудника`);
                setState(commit, { isAssignModalVisible: false });
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        },
    }
};