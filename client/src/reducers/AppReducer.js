//stateの初期化
const initState = {
    inputValue: '',
    connectValue: '',
};

//呼ばれたActionによって行う処理の分岐
export default function appReducer(state = initState, action) {
    switch (action.type) {
        case 'CHANGE_VALUE':
            return { //この書き方でstateを引用しつつ，一致した箇所は書き換えるという記述
                ...state,
                inputValue: action.value
            };
        case 'CONNECT_VALUE':
            return {
                ...state,
                connectValue: action.value
            };

        default:
            return state;
    }
}
