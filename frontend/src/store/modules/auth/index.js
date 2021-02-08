import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        token: localStorage.getItem("token")
    },

    getters: {
        token: (state) => state.token
        // username: (state) => state.user.username,
        // email: (state) => state.user.email,
        // isActive: (state) => state.user.is_active,
        // isStaff: (state) => state.user.is_staff,
        // photo: (state) => state.user.photo,
        // role: (state) => state.user.role,
    },

    mutations: {
        SET_STATE,
        setState,
    },

    actions: {
        async login({ commit }, params) {
            try {
                const result = await api.login(params);
                localStorage.setItem("token", result.token);
                setState(commit, { token: result.token });
            } catch (e) {
                showErrorNotify("Неправильные данные входа");
            }
        },
        async logout({commit}, params){
            try {
                await api.logout(params);
                setState(commit, { token: null, isAuth: false });
                localStorage.removeItem('token');
            } catch (e) {
                showErrorNotify("ERR");
            }
        }
    }
};