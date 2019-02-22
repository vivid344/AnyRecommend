import React, {Component} from 'react';
import { Button } from 'react-mdl';

class Search extends Component {
    constructor(props) {
        super(props);
        this.connect = this.connect.bind(this);
    }

    connect() {
        this.props.connectTest();
    }

    render() {
        return (
            <div className="Search">
                <Button onClick={this.connect}>テストで通信するよ</Button>
                <div>
                    {this.props.connectValue}
                </div>
            </div>
        );
    }
}

export default Search;
