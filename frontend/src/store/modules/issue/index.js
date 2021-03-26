import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';
import { textToMinutes } from '@/utils/transfer';

export default {
    namespaced: true,
    state: {
        issues: [],
        issue: {},
        history: [],
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
        isAssignModalVisible: false,
        isStatusModalVisible: false,
        unAssignedStuff: false
    },
    getters: {
        issue: (state) => state.issue,
        issues: (state) => state.issues,
        history: (state) => state.history,
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
        isAssignModalVisible: (state) => state.isAssignModalVisible,
        isStatusModalVisible: (state) => state.isStatusModalVisible,
        unAssignedStuff: (state) => state.unAssignedStuff
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
                setState(commit, { issue: result, unAssignedStuff: false });
                dispatch('getChildren', {'id': issueId});
                dispatch('getComments', issueId);
                dispatch('getTracks', issueId);
                dispatch('getIssueHistory', {'issue_id': issueId});
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
        async editIssue({commit, dispatch}, payload) {
          try {
              await api.changeIssue(payload);
              dispatch('getIssue', payload.issue_id);
              setState(commit, { isStatusModalVisible: false });
              location.reload();
          } catch (e) {
              showErrorNotify(e.response.data.detail);
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
        async deleteComment({dispatch }, payload){
            try {
                await api.deleteComment(payload);
                dispatch('getIssue', payload.issue_id);
            } catch (e){
                const err = "You can't delete this comment";
                const detail = e.response.data.detail;
                if (detail !== err) {
                    showErrorNotify(detail);
                }
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
                showErrorNotify(e.response.data.detail);
            }
        },
        async deleteTrack({dispatch }, payload){
            try {
                await api.deleteTrack(payload);
                dispatch('getIssue', payload.issue_id);
            } catch (e){
                const err = "You can't delete this track";
                const detail = e.response.data.detail;
                if (detail !== err) {
                    showErrorNotify(detail);
                }
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
                setState(commit, { isAssignModalVisible: false });
                location.reload();
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        },
        async getIssueHistory({commit}, filter) {
            try {
                const result = await api.getIssueHistory(filter);
                setState(commit, { history: result });
            } catch (e) {
                showErrorNotify(e.message);
            }
        }
    }
};