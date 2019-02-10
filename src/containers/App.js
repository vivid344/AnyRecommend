import {connect} from 'react-redux'
import App from '../components/App'
import {changeValue} from '../actions/AppAction'

//stateにある値をthis.propsで受け取れるように受け取りたい値をここで宣言
//受け取るReducerの指定→Reducer内に存在する値を指定し，取得
function mapStateToProps({appReducer}) {
    return {
        inputValue: appReducer.inputValue,
    };
}

//Actionで定義したものをthis.propsで受け取れるように受け取りたいActionをここで宣言
function mapDispatchToProps(dispatch) {
    return {
        changeValue(value) {
            dispatch(changeValue(value))
        }
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(App)
