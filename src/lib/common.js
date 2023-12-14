export function stringToColor(str) {
    let hash = 5381;
    for (let i = 0; i < str.length; i++) {
        hash = (hash << 5) + hash + str.charCodeAt(i); /* hash * 33 + c */
        // console.log("hash", hash);
    }
    let golden_ratio = 0.618033988749895;
    let hue = Math.abs(((hash * golden_ratio) % 1) * 360);
    // console.log("hue", hue);
    return `hsl(${hue}, 50%,  70%)`;
}