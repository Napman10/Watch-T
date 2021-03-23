import {isAdmin, isCreator, isExecutor} from "@/utils/roler";

export function template(func){
    return func({role: Number(localStorage.getItem('myRole'))})
}

export function meAdmin(){
    return template(isAdmin);
}

export function meCreator() {
    return template(isCreator);
}

export function meExecutor() {
    return template(isExecutor);
}
