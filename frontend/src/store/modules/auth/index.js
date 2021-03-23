import api from '@/api';
import {SET_STATE, setState} from '@/store/helpers';
import { showErrorNotify } from '@/utils';


export default {
    namespaced: true,
    state: {
        token: localStorage.getItem("token"),
        me: localStorage.getItem("me")
    },

    getters: {
        token: (state) => state.token,
        me: (state) => state.me
    },

    mutations: {
        SET_STATE,
        setState,
    },

    actions: {
        async login({ commit }, params) {
            try {
                const result = await api.login(params);
                localStorage.setItem("token", result.auth_token );
                setState(commit, { token: result.auth_token });

                const user = await api.getMe(result.auth_token);
                const role = user.role;
                localStorage.setItem("myRole", role );
                setState(commit, {"myRole": role});

                location.reload();
            } catch (e) {
                showErrorNotify("Неправильные данные входа");
            }
        },
        async logout({commit}, params){
            try {
                await api.logout(params);
                setState(commit, { token: null});
                localStorage.removeItem('token');
                setState(commit, {me: {}});
                localStorage.removeItem('me');
                location.href = '/';
            } catch (e) {
                showErrorNotify(e);
            }
        }
    }
};