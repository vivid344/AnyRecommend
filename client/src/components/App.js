import React, {Component} from 'react';
import Search from "./Search/Search";
import Detail from "./Detail/Detail";
import Similar from "./Similar/Similar";
import { Layout, Header, Content } from 'react-mdl';

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
                        </Header>
                        <Content className="content-wrapper">
                            <Search/>
                            <Detail/>
                            <Similar/>
                        </Content>
                    </Layout>
                </div>
            </div>
        );
    }
}

export default App;
