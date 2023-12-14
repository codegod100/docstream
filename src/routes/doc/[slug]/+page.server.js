
/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params, url }) {
    let slug = params.slug
    let endpoint = `http://localhost:5000/doc/${slug}`
    let author = url.searchParams.get('author') || generateUsername()
    let data = await fetch(`${endpoint}?author=${author}`)
    let json = await data.json()

    return {
        json, slug, author
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