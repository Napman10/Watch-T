export function div(val, by){
    return (val - val % by) / by;
}

export function textToMinutes(stringTime) {
    let correctFormat = stringTime.match(/^\d*н?\s*\d*д?\s*\d*ч?\s*\d*[мин]?\s*/)
    if (correctFormat) {
        let minutes = stringTime.match(/\d*мин/);
        let hours = stringTime.match(/\d*ч/);
        let days = stringTime.match(/\d*д/);
        let weeks = stringTime.match(/\d*н/);

        minutes = minutes ? Number(minutes[0].replace('мин', '')) : 0;
        hours = hours ? Number(hours[0].replace('ч', '')) : 0;
        days = days ? Number(days[0].replace('д', '')) : 0;
        weeks = weeks ? Number(weeks[0].replace('н', '')) : 0;

        return Math.ceil(minutes + 60 * hours + 8 * 60 * days + 5 * 8 * 60 * weeks);
    }
    return 0;
}

export function minutesToText(minutes){
    const toHour = 60;
    const toDay = toHour * 8;
    const toWeek = toDay * 5;

    const weeks = div(minutes, toWeek);
    minutes -= weeks * toWeek;

    const days = div(minutes, toDay);
    minutes -= days * toDay;

    const hours = div(minutes, toHour);
    minutes -= hours * toHour;

    let result = "";
    if (weeks !== 0){
        result += weeks + 'н ';
    }
    if (days !== 0) {
        result += days + 'д ';
    }
    if (hours !== 0){
        result += hours + 'ч ';
    }
    if (minutes !== 0) {
        result += minutes + 'мин ';
    }
    if (result === ""){
        return "-";
    }
    else {
        return result;
    }
}

export function parsePert(str) {
    let splits = str.split("-");
    const result = (3 * textToMinutes(splits[0]) + 2 * textToMinutes(splits[1])) / 5
    return minutesToText(result);
}