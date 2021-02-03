import cloneDeep from 'lodash/cloneDeep';
import merge from 'lodash/merge';
import sortBy from 'lodash/sortBy';
import orderBy from 'lodash/orderBy';
import get from 'lodash/get';
import setWith from 'lodash/setWith';
import keyBy from 'lodash/keyBy';
import difference from 'lodash/difference';
import isEmpty from 'lodash/isEmpty';
import set from 'lodash/set';
import filter from 'lodash/filter';
import some from 'lodash/some';

const lodash = {
    cloneDeep,
    merge,
    sortBy,
    orderBy,
    get,
    setWith,
    keyBy,
    difference,
    isEmpty,
    set,
    filter,
    some
};

window.lodash = lodash;
window._ = lodash;

export { lodash };