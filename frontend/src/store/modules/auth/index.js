import api from '@/api';
import {SET_STATE, setState} from '@/store/helpers';
import { showErrorNotify } from '@/utils';


export default {
    namespaced: true,
    state: {
        token: localStorage.getItem("token"),
        me: localStorage.getItem("me"),
        myId: localStorage.getItem("myId"),
        myName: localStorage.getItem("myName"),
        myRole: localStorage.getItem("myRole")
    },

    getters: {
        token: (state) => state.token,
        me: (state) => state.me,
        myId: (state) => state.myId,
        myName: (state) => state.myName,
        myRole: (state) => state.myRole
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
                const myId = user.id;
                const myName = user.username;

                localStorage.setItem("myRole", role );
                setState(commit, {"myRole": role});

                localStorage.setItem("myId", myId );
                setState(commit, {"myId": myId });

                localStorage.setItem("myName", myName );
                setState(commit, {"myName": myName });

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