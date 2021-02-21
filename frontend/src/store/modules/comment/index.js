import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify} from '@/utils';

export default {
    namespaced: true,
    state: {
        comments: [],
        comment: {},
        loading: false,
        isCreateModalVisible: false
    },
    getters: {
        comment: (state) => state.comment,
        comments: (state) => state.comments,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible
    },
    mutations: {
        SET_STATE
    },
    actions: {
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
                dispatch('getComments'); //issueId here
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async getComment({ commit }, commentId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getComment(commentId);
                setState(commit, { comment: result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        }
    }
};