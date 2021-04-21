import {isAdmin, isCreator, isExecutor, isNotGuest, isDev} from "@/utils/roler";

export function template(func){
    return func({role: Number(localStorage.getItem('myRole'))})
}

export function meAdmin(){
    return template(isAdmin);
}

export function itsDev(user){
    return isDev(user)
}

export function meCreator() {
    return template(isCreator);
}

export function meExecutor() {
    return template(isExecutor);
}

export function meNotGuest() {
    return template(isNotGuest)
}

export function canTrack(executor) {
    return meCreator() || (meExecutor() && executor === localStorage.getItem('myName'));
}