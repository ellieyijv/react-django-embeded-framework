import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addLead } from '../../actions/leads';

export class Form extends Component {
    state = {
        name: '',
        email: '',
        message: ''
    }

    static propTypes = {
        addLead: PropTypes.func.isRequired
    }
    onChange = e => this.setState({ [e.target.name]: e.target.value });

    onSubmit = e => {
        e.preventDefault();
        const { name, email, message } = this.state;
        const lead = { name, email, message };
        this.props.addLead(lead);
    }

    render() {
        const { name, email, message } = this.state
        return (
            <Fragment>
                <form onSubmit={this.onSubmit} className="mt-5">
                  <div className="row">
                    <div className="col">
                      <input type="text" className="form-control" placeholder="name" value={name} name="name"
                        onChange={this.onChange} />
                    </div>
                    <div className="col">
                      <input type="email" className="form-control" placeholder="Email" value={email} name="email"
                        onChange={this.onChange} />
                    </div>
                    <div className="col">
                      <input type="textarea" className="form-control" placeholder="Message" value={message} name="message"
                        onChange={this.onChange} />
                    </div>
                    <div className="col">
                        <button type="submit" className="btn btn-sm btn-primary">Submit</button>
                    </div>

                  </div>
                </form>
            </Fragment>
        )
    }

}

export default connect(null, { addLead })(Form);