import React, { Component } from "react";
import './style.css';

class ListRender extends Component {

    render() {
        return (
            <ul>
                {this.props.data.map(item => <li>{item}</li>)}
            </ul>
        );
    }
}

export default ListRender;