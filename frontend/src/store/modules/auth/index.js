import api from '@/api';
import { SET_STATE, setState } from '@/store/helpers';
import { showErrorNotify } from '@/utils';

export default {
    namespaced: true,
    state: {
        user: {},
        isAuth: false,
        token: null
    },

    getters: {
        isAuth: (state) => state.isAuth,
        token: (state) => state.token,
        username: (state) => state.user.username,
        email: (state) => state.user.email,
        isActive: (state) => state.user.is_active,
        isStaff: (state) => state.user.is_staff,
        photo: (state) => state.user.photo,
        role: (state) => state.user.role,
    },

    mutations: {
        SET_STATE,
        setState,
        LOG_OUT(state) {
            state.isAuth = false;
            state.user = {};
            state.token = null;
        }
    },

    actions: {
        async login({ commit }, params) {
            try {
                const result = await api.login(params);
                console.log(result)
                setState(commit, { token: result.access });
                setState(commit, { isAuth: true });
            } catch (e) {
                showErrorNotify(e.message);
            }
        }
    }
};