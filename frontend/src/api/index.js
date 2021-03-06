import comment from "@/api/comment";
import issue from '@/api/issue';
import login from '@/api/login';
import project from '@/api/project';
import track from "@/api/track";
import user from "@/api/user";

const api = {
    ...comment,
    ...issue,
    ...login,
    ...project,
    ...track,
    ...user
};

export default api;