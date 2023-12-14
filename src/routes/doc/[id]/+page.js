import ioClient from 'socket.io-client';
/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params, url }) {
    let endpoint = `http://localhost:5000/doc/${params.id}`
    let author = url.searchParams.get('author') || generateUsername()
    let data = await fetch(`${endpoint}?author=${author}`)
    let json = await data.json()
    const io = ioClient(`http://localhost:5000`);
    io.on('connect', () => console.log("we made it"))
    console.log(json)
    return {
        json, io, id: params.id, author, renew: async () => {
            let data = await fetch(`${endpoint}?author=${author}`)
            let json = await data.json()
            return json
        }
    }
}



function generateUsername() {
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