import React from 'react';
import App from './containers/App';
import {render} from 'react-dom';
import {createStore, applyMiddleware} from 'redux';
import {Provider} from 'react-redux';
import reducers from './reducers/Reducer';
import logger from 'redux-logger';

//reducerとミドルウェアをつなげる
const store = createStore(
    reducers,
    applyMiddleware(logger)
);

render(
    <Provider store={store}>
        <App/>
    </Provider>,
    document.getElementById('root')
);
