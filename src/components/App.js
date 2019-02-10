import React, {Component} from 'react';
import Search from "./Search/Search";
import Detail from "./Detail/Detail";
import Similar from "./Similar/Similar";

class App extends Component {
    //thisを関数内でも使えるように定義
    constructor(props) {
        super(props);
        this.change = this.change.bind(this);
    }

    //値が変更した際に呼ばれる関数
    change(e) {
        this.props.changeValue(e.target.value)
    }

    //値を入力したら，その文字がフォームの上に出力される
    render() {
        return (
            <div className="App">
                <Search/>
                <Detail/>
                <Similar/>
            </div>
        );
    }
}

export default App;
