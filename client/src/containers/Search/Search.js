import {connect} from 'react-redux'
import Search from '../../components/Search/Search'
import {connectTest} from '../../actions/AppAction'

//stateにある値をthis.propsで受け取れるように受け取りたい値をここで宣言
//受け取るReducerの指定→Reducer内に存在する値を指定し，取得
function mapStateToProps({appReducer}) {
    return {
        connectValue: appReducer.connectValue,
    };
}

//Actionで定義したものをthis.propsで受け取れるように受け取りたいActionをここで宣言
function mapDispatchToProps(dispatch) {
    return {
        connectTest() {
            dispatch(connectTest())
        }
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Search)
