import React, {Component} from 'react';
import Search from "./Search/Search";
import Detail from "./Detail/Detail";
import Similar from "./Similar/Similar";

class App extends Component {
    //thisを関数内でも使えるように定義
    constructor(props) {
        super(props);
    }

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
