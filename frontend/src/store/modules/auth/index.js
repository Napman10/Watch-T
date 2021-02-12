import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        username: null,
        token: localStorage.getItem("token")
    },

    getters: {
        token: (state) => state.token,
        username: (state) => state.username,
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
            state.isAuth = false;
            state.token = null;
            localStorage.removeItem('token')
            state.user = {};
        },
    },

    actions: {
        async login({ commit }, params) {
            try {
                const result = await api.login(params);
                localStorage.setItem("token", result.token);
                setState(commit, { token: result.token, username: result.name });
            } catch (e) {
                showErrorNotify("Неправильные данные входа");
            }
        }
    }
};