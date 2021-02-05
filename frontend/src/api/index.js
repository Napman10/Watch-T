import issue from '@/api/issue';
import login from '@/api/login';
import project from '@/api/project';

const api = {
    ...issue,
    ...login,
    ...project
};

export default api;