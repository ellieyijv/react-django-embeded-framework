import React, { Component, Fragment, lazy, Suspense } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import Alerts from './layout/Alerts';

import Leads from './leads/Leads';
import Form from './leads/Form';
// import About from './layout/About';

import { transitions, positions, Provider as AlertProvider } from 'react-alert';
import AlertTemplate from 'react-alert-template-basic';
import { Provider } from 'react-redux';
import store from '../store';

// const About = lazy(() => import(/*webpackChunkName:"about" */'./layout/About'));

//ErrorBoundary
//componentDidCatch

const alertOptions = {
  timeout: 3000,
  position: positions.BOTTOM_CENTER,
}

class App extends Component {
  state = {
    hasError: false,
  };

  // componentDidCatch() {
  //   this.setState({
  //     hasError: true,
  //   })
  // }
  static getDerivedStateFromError() {
    return {
      hasError: true,
    }
  }
  render() {
    if (this.state.hasError) {
      return <div>error</div>
    }
    return (
      // <div>
      //   <Suspense fallback={<div>loading</div>}>
      //     <About></About>
      //   </Suspense>
      // </div>
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
          <Fragment>
            <Header />
            <Alerts />
            <div className="container">
              <Form />
              <Leads />
            </div>
          </Fragment>
        </AlertProvider>
      </Provider>
    )
  }
}


ReactDOM.render(<App />, document.getElementById('app'));