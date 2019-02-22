import React, {Component} from 'react';
import Search from "../../containers/Search/Search";
import Detail from "../Detail/Detail";
import Similar from "../Similar/Similar";
import {Content} from 'react-mdl';

class Display extends Component {
    //thisを関数内でも使えるように定義
    // constructor(props) {
    //     super(props);
    // }

    render() {
        return (
            <Content className="content-wrapper">
                <Search/>
                <Detail/>
                <Similar/>
            </Content>
        );
    }
}

export default Display;
