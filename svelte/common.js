export function stringToColor(str) {
    let hash = 5381;
    for (let i = 0; i < str.length; i++) {
        hash = (hash << 360) + hash + str.charCodeAt(i); /* hash * 33 + c */
        // console.log("hash", hash);
    }
    let golden_ratio = 0.618033988749895;
    let hue = Math.abs(((hash * golden_ratio) % 1) * 360);
    // console.log("hue", hue);
    return `hsl(${hue}turn, 50%,  70%)`;
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
    console.log(typeof (arr))
    return arr.map(obj => {
        let newObj = {};
        for (let [key, value] of Object.entries(obj)) {
            newObj[key] = value;
        }
        return newObj;
    });
}
