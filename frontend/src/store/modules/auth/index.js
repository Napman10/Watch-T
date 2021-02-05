import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        user: {},
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
        LOG_OUT(state) {
            state.user = {};
            state.token = null;
            state.isAuth = false;
            localStorage.removeItem('token');
        }
    },

    actions: {
        async login({ commit }, params) {
            try {
                const result = await api.login(params);
                localStorage.setItem("token", result.access);
                setState(commit, { token: result.access });
            } catch (e) {
                showErrorNotify("Неправильные данные входа");
            }
        }
    }
};