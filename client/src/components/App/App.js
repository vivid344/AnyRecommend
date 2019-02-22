import React, {Component} from 'react';
import Display from "../Display/Display";

import { Layout, Header } from 'react-mdl';
import { Link } from "react-router-dom";

class App extends Component {
    //thisを関数内でも使えるように定義
    // constructor(props) {
    //     super(props);
    // }

    render() {
        return (
            <div className="App">
                <div className="demo-big-content">
                    <Layout>
                        <Header title="アニメ推薦">
                            <Link to='/setting'>Setting</Link>
                        </Header>
                        <Display/>
                    </Layout>
                </div>
            </div>
        );
    }
}

export default App;
