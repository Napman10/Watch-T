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
        isEdit: false,
        isChangePasswordVisible: false,
        isAddSkillvisible: false,
        skills: []
    },
    getters: {
        user: (state) => state.user,
        users: (state) => state.users,
        loading: (state) => state.loading,
        isCreateModalVisible: (state) => state.isCreateModalVisible,
        isEdit: (state) => state.isEdit,
        isChangePasswordVisible: (state) => state.isChangePasswordVisible,
        isAddSkillvisible: (state) => state.isAddSkillvisible,
        skills: (state) => state.skills
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
                showErrorNotify(e.response.data.detail);
            }
        },
        async getUser({ commit }, userId) {
            try {
                setState(commit, { loading: true });
                const result = await api.getUser(userId);
                const stat = await api.getUserStatistics(userId);
                setState(commit, {user: {...result, ...stat} });

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
                showErrorNotify(e.response.data.detail);
            }
        },
        async getSkills({commit}, payload) {
          try {
              const missedSkills = await api.missingSkills(payload)
              setState(commit, {skills: missedSkills})
          }  catch (e) {
              showErrorNotify(e);
          }
        },
        async deleteUser({dispatch}, payload){
            try {
                await api.deleteUser(payload);
                dispatch('getUsers');
            } catch (e) {
                showErrorNotify(e.response.data.detail);
            }
        }

    }
};