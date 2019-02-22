import { all } from 'redux-saga/effects';
import TestSaga from './Test/TestSaga';

export default function* rootSaga() {
    yield all([
        ...TestSaga,
    ]);
}
