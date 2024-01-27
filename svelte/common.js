export function randColor() {
    const letters = '89ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 8)];
    }
    return color;
}


export function generateUsername() {
    const words = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "iceberg",
        "jackfruit",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "pineapple",
        "quince",
        "raspberry",
        "strawberry",
        "tangerine",
        "ugli",
        "victoria",
        "watermelon",
        "xigua",
        "yellow",
        "zucchini",
    ];
    let username =
        words[Math.floor(Math.random() * words.length)] +
        words[Math.floor(Math.random() * words.length)];
    return username;
}


export function convertKeys(arr) {
    return arr.map(obj => {
        let newObj = {};
        for (let [key, value] of Object.entries(obj)) {
            newObj[key] = value;
        }
        return newObj;
    });
}
