import React, {Component} from 'react';
import { Link } from 'react-router-dom'

class App extends Component {
    //thisを関数内でも使えるように定義
    // constructor(props) {
    //     super(props);
    // }

    render() {
        return (
            <div>
                ほげええええ
                <Link to='/'>Home</Link>
            </div>
        );
    }
}

export default App;
