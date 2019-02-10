import { combineReducers } from 'redux'
import appReducer from './AppReducer'

//combineReducersで複数のReducerをまとめることが出来る
//このまま下にReducer追記でおk
const reducers = combineReducers({
    appReducer,
});

export default reducers
