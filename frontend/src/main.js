import Vue from 'vue';
import App from './App.vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/ru-RU';
import store from '@/store';
Vue.config.productionTip = false;

Vue.use(ElementUI, { locale });
Vue.use(ElementUI);
Vue.use(require('vue-moment'));


new Vue({
  render: h => h(App),
  store: store,
  router: require('./router/index').default
}).$mount('#app')
