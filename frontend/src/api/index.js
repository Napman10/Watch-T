import issue from '@/api/issue';
import login from '@/api/login';
import project from '@/api/project';
import user from "@/api/user";

const api = {
    ...issue,
    ...login,
    ...project,
    ...user
};

export default api;