import React from 'react';
import App from './containers/App/App';
import {render} from 'react-dom';
import {createStore, applyMiddleware} from 'redux';
import {Provider} from 'react-redux';
import reducers from './reducers/Reducer';
import logger from 'redux-logger';
import 'react-mdl/extra/material.css';
import 'react-mdl/extra/material.js';
import { BrowserRouter, Route } from 'react-router-dom'
import Setting from "./components/Setting/Setting";
import createSagaMiddleware from 'redux-saga'
import rootSaga from './sagas';

const sagaMiddleware = createSagaMiddleware();

//reducerとミドルウェアをつなげる
const store = createStore(
    reducers,
    applyMiddleware(logger, sagaMiddleware)
);

// run saga
sagaMiddleware.run(rootSaga);

render(
    <Provider store={store}>
        <BrowserRouter>
            <div>
                <Route exact path='/' component={App} />
                <Route path='/setting' component={Setting} />
            </div>
        </BrowserRouter>
    </Provider>,
    document.getElementById('root')
);
