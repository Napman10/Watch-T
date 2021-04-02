const guest = 0;
const dev = 1;
const manager = 2;
const lead = 3;
const admin = 4;

export function isAdmin(user){
    return user.role === admin;
}

export function isCreator(user){
    const role = user.role
    return role === admin || role === manager || role === lead;
}

export function isExecutor(user){
    const role = user.role;
    return role === admin || role === dev || role === lead;
}

export function isNotGuest(user) {
    const role = user.role;
    return role !== guest;
}