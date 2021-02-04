import Moment from 'moment';
import 'moment/locale/ru';
import { extendMoment } from 'moment-range';

const moment = extendMoment(Moment);
window.moment = moment;

/**
 * Constant datetime format moment.
 * @type <moment['HTML5_FMT']>
 * @property DATE 'YYYY-MM-DD'
 * @property DATETIME_LOCAL 'YYYY-MM-DDTHH:mm'
 * @property DATETIME_LOCAL_SECONDS 'YYYY-MM-DDTHH:mm:ss'
 * @property DATETIME_LOCAL_MS 'YYYY-MM-DDTHH:mm:ss.SSS'
 * @property MONTH 'YYYY-MM'
 * @property TIME 'HH:mm'
 * @property TIME_MS 'HH:mm:ss.SSS'
 * @property TIME_SECONDS 'HH:mm:ss'
 * @property WEEK 'GGGG-[W]WW'
 * @property DATETIME_LOCAL_HYMAN: 'DD.MM.YYYY HH:mm'
 */
export const FORMAT_TYPE = {
    ...moment.HTML5_FMT,
    DATETIME_LOCAL_HYMAN: 'DD.MM.YYYY HH:mm',
    DATETIME_LOCAL_HYMAN_SECONDS: 'DD.MM.YYYY HH:mm:ss'
};

moment.HTML5_FMT = Object.assign(moment.HTML5_FMT, FORMAT_TYPE);

export { moment };