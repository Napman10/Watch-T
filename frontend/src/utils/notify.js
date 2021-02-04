import Vue from 'vue';

export function showSuccessNotify(text, options = {}) {
    Vue.prototype.$notify({
        title: 'Успешно',
        message: text,
        type: 'success',
        customClass: 'notify-success',
        ...options
    });
}

export function showErrorNotify(text, options = {}) {
    Vue.prototype.$notify({
        title: 'Ошибка',
        message: text,
        type: 'error',
        customClass: 'notify-error',
        ...options
    });
}