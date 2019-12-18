import React, { Component } from "react";
import axios from 'axios';
import ListRender from "components/ListRender";

class UserRepositories extends Component {

    state = {
        repNames: []
    }

    componentDidMount() {
        let url = "https://api.github.com/users/" + this.props.userName + "/repos";
        axios.get(url).then(responce => {
            let repNames = responce.data.map(item => item.name);
            this.setState({repNames});
        })
    }

    render() {

        return (
            <div>
                <h1>{this.props.userName}  repositories:</h1>
                <ListRender data={this.state.repNames} />
            </div>
        );
    }
}


export default UserRepositories;