//Actionの定義
export const changeValue = (value) => ({
    type: 'CHANGE_VALUE',
    value,
});

export const connectValue = (value) => ({
    type: 'CONNECT_VALUE',
    value,
});

export const connectTest = () => ({
    type: 'CONNECT_TEST'
});
