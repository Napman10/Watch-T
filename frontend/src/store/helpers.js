import { lodash as _ } from '@/utils';

export function SET_STATE(context, data) {
    console.log(data)
    if (Array.isArray(data)) {
        data.map(({ state, payload }) => (context[state] = payload));
    } else if (!Object.keys(data).includes('state')) {
        Object.entries(data).forEach(([state, value]) => _.set(context, state, value));
    } else {
        const { state, payload } = data;
        context[state] = payload;
    }
}

export const setState = (commit, data) => commit('SET_STATE', data);