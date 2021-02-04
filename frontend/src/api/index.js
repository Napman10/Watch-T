import issue from '@/api/issue';
import login from '@/api/login';

const api = {
    ...issue,
    ...login
};

export default api;