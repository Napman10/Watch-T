import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify, showSuccessNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        users: [],
        user: {},
        loading: false,
        isCreateModalVisible: false,
        isEdit: false
    },
    getters: {
        user: (state) => state.user,
        users: (state) => state.users,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible,
        isEdit: (state) => state.isEdit
    },
    mutations: {
        SET_STATE
    },
    actions: {
        async getUsers({ commit }, filter) {
            try {
                const result = await api.getUsers(filter);
                setState(commit, { users: result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        },
        async addUser({ commit, dispatch }, payload) {
            try {
                await api.addUser(payload);
                showSuccessNotify(`Пользователь создан!`);
                setState(commit, { isCreateModalVisible: false });
                dispatch('getUsers');
            } catch (e) {
                showErrorNotify(e.message);
            }
        },
        async getUser({ commit }, userId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getUser(userId);
                setState(commit, { user: result });
            } catch (e) {
                showErrorNotify(e.message);
            } finally {
                setState(commit, { loading: false });
            }
        },
        async editUser({commit}, payload) {
            try {
                await api.editUser(payload);
                showSuccessNotify(`Сохранено`);
                setState(commit, {isEdit: false});
                location.reload()
            } catch (e) {
                showErrorNotify(e.message)
            }
        },
        async deleteUser({dispatch}, payload){
            try {
                await api.deleteUser(payload);
                dispatch('getUsers');
            } catch (e) {
                showErrorNotify(e.message);
            }
        }

    }
};