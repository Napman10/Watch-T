import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';


export default {
    namespaced: true,
    state: {
        issues: [],
        issue: {},
        comments: [],
        comment : {},
        loading: false,
        isCreateModalVisible: false,
        editCommentModalVisible: false,
        descIssueModalVisible: false,
        descProjectIssueModalVisible: false
    },
    getters: {
        issue: (state) => state.issue,
        issues: (state) => state.issues,
        comment: (state) => state.comment,
        comments: (state) => state.comments,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible,
        editCommentModalVisible: (state) => state.editCommentModalVisible,
        descIssueModalVisible: (state) => state.descIssueModalVisible,
        descProjectIssueModalVisible: (state) => state.descProjectIssueModalVisible
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
        async getIssue({ commit, dispatch}, issueId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getIssue(issueId);
                setState(commit, { issue: result });
                dispatch('getComments', issueId);
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        },
        async getComments({ commit }, issueId) {
            try {
                const result = await api.getComments(issueId);
                setState(commit, { comments: result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
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
        }
    }
};