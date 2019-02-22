import { call, put, takeEvery } from 'redux-saga/effects'
import * as client from '../../apis/Test/TestApi'; // エンドポイントをclientとして一括登録
import {connectValue} from '../../actions/AppAction'


function* getTitleRequest(action) {
    const { body, error } = yield call(client.testApi);
    if (error) {
        // サーバに接続できない場合
        // yield put(failureGetAllBoard());
        // const logoutTask = yield fork(logoutRequest);
        // yield join(logoutTask);
    } else {
        if (body) {
            const title = yield body.data[0]['title'];
            if (title) {
                // 正常にレスポンスを受け取った場合
                yield put(connectValue(title));
            } else {
                // レスポンスが空の場合
                // yield put(failureGetAllBoard());
            }
        }
    }
}


const saga = [
    takeEvery("CONNECT_TEST", getTitleRequest)
];

export default saga;
